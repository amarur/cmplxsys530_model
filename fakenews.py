# Implementation of a SIR based model of 'fake news' propagation in social networks
# Anant Marur | amarur | 19237018
# CMPLXSYS 530, Lynette Shaw
# April 17, 2018
# usage: python fakenews.py <NUM_AGENTS> <NUM_CLUSTERS> <INTERACTION RATE> <SPREADING_RATE> <REFUSING_RATE> <STIFLING_RATE>

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import numpy as NP
import math
import networkx as nx 
import sys
import pycxsimulator
import argparse

class AgentTypes:
	Spreader = 0
	Ignorant = 1
	Stifler = 2

class Agent:
	def __init__(self, _ptxLeaning, _nodeNum):
		self.ptxLeaning = _ptxLeaning
		self.type = AgentTypes.Ignorant
		self.openMind = self.__setOM__()
		self.nodeNum = _nodeNum

	def listen(self, storyPtx, tellerPtx):
		sdiscrepancy = self.ptxLeaning - storyPtx
		tdiscrepancy = self.ptxLeaning - tellerPtx
		weightedSprRate = spreadingRate 
		if wStory:
			weightedSprRate += (1 - self.openMind) * (-1 * (math.fabs(sdiscrepancy) - 1) * min(spreadingRate, 1 - spreadingRate))
		if wTeller:
			weightedSprRate += (1 - self.openMind) * (-1 * (math.fabs(tdiscrepancy) - 1) * min(spreadingRate, 1 - spreadingRate))
		if RD.random() < weightedSprRate:
			self.type = AgentTypes.Spreader
		else:
			self.type = AgentTypes.	Stifler



	#private helpers
	def __setOM__(self):
		poissLamb = 10 - 6 * math.fabs(self.ptxLeaning)
		openMind = NP.random.poisson(poissLamb)/20.0
		if openMind > 1:
			openMind = 1
		return openMind



	

def init():
	global edges, socNet, pos 
	global storyPtx, ptxLeanings, agents
	global interactRate, spreadingRate
	global wStory, wTeller

	RD.seed()

	#initialize variables dependent on command line arguments
	parser = argparse.ArgumentParser(description='Simulate information propagation in a social network with adjustable considerations')
	parser.add_argument('nAgents_', type=int)
	parser.add_argument('clustSize_', type=int)
	parser.add_argument('intRate_', type=float)
	parser.add_argument('sprRate_', type=float)
	parser.add_argument('storyPtx_', type=float)
	parser.add_argument('--wStory_', action='store_true')
	parser.add_argument('--wTeller_', action='store_false')
	args=vars(parser.parse_args())
	numAgents = args['nAgents_']
	clusterSize = args['clustSize_']
	interactRate = args['intRate_']
	spreadingRate = args['sprRate_']
	storyPtx = args['storyPtx_']
	wStory = args['wStory_']
	wTeller = args['wTeller_']
	



	#initialize a clustered graph
	socNet = nx.gaussian_random_partition_graph(numAgents, clusterSize, 0.1 * clusterSize, 0.85, 0.05)

	#initialize the positioning of the graph nodes
	commIndex = 0
	nodeToComm = dict()
	for x in socNet.graph['partition']:
		for y in x:
			nodeToComm[y] = commIndex
		commIndex += 1
	pos = community_layout(socNet, nodeToComm)

	#initialize average political leaning for each cluster
	#todo: make normal distribution perhaps
	commPtx = dict()
	for i in range(0, commIndex + 1):
		commPtx[i] = NP.random.normal(scale=0.45)
	
	#initialize politican leanings
	ptxLeanings = list()
	for key, _ in nodeToComm.iteritems():
		ptx = commPtx[nodeToComm[key]]
		ptx += NP.random.normal(scale=0.15)
		if ptx < -1:
			ptx = -1
		elif ptx > 1:
			ptx = 1
		ptxLeanings.append(ptx)

	#initialize list of agent objects
	agents = list()
	for key, _ in nodeToComm.iteritems():
		agents.append(Agent(ptxLeanings[key], key))

	print(storyPtx)

	#pick a story seed
	agents[RD.sample(xrange(socNet.number_of_nodes()), 1)[0]].type = AgentTypes.Spreader

	#initialize edgelist
	edges = list(socNet.edges())

	





def draw():
	#initialize plot size
	#fig.clear()
	PL.clf()
	PL.axis('off')
	fig = PL.gcf()
	fig.set_size_inches(10, 10, forward=True)
	colors = list()
	widths = list()
	for agent in agents:
		if agent.type == AgentTypes.Spreader:
			colors.append('#ace600')
			widths.append(2)
		elif agent.type == AgentTypes.Stifler:
			colors.append('#000000')
			widths.append(2)
		else:
			colors.append('0.5')
			widths.append(0)

	#draw spreaders
	nx.draw_networkx_nodes(socNet, pos, node_size=75, node_color=NP.asarray(ptxLeanings), 
							vmin=-1, vmax=1, cmap=PL.get_cmap("coolwarm"), edgecolors=colors, linewidths=widths)
	nx.draw_networkx_edges(socNet, pos, width=0.2, alpha=0.5)
	#fig.show(socNet)

def step():
	numInteractions = int(interactRate * socNet.number_of_edges())
	for i in RD.sample(xrange(socNet.number_of_edges()), numInteractions):
		if((agents[edges[i][0]].type == AgentTypes.Spreader) and (agents[edges[i][1]].type == AgentTypes.Ignorant)):
			agents[edges[i][1]].listen(storyPtx, agents[edges[i][0]].ptxLeaning)
		if((agents[edges[i][1]].type == AgentTypes.Spreader) and (agents[edges[i][0]].type == AgentTypes.Ignorant)):
			agents[edges[i][0]].listen(storyPtx, agents[edges[i][1]].ptxLeaning)


def main():
	pycxsimulator.GUI().start(func=[init,draw,step])


def community_layout(g, partition):
	"""
	Compute the layout for a modular graph.


	Arguments:
	----------
	g -- networkx.Graph or networkx.DiGraph instance
		graph to plot

	partition -- dict mapping int node -> int community
		graph partitions


	Returns:
	--------
	pos -- dict mapping int node -> (float x, float y)
		node positions

	"""

	pos_communities = _position_communities(g, partition, scale=30.0)

	pos_nodes = _position_nodes(g, partition, scale=6)

	# combine positions
	pos = dict()
	for node in g.nodes():
		pos[node] = pos_communities[node] + pos_nodes[node]

	return pos

def _position_communities(g, partition, **kwargs):

	# create a weighted graph, in which each node corresponds to a community,
	# and each edge weight to the number of edges between communities
	between_community_edges = _find_between_community_edges(g, partition)

	communities = set(partition.values())
	hypergraph = nx.DiGraph()
	hypergraph.add_nodes_from(communities)
	for (ci, cj), edges in between_community_edges.items():
		hypergraph.add_edge(ci, cj, weight=len(edges))

	# find layout for communities
	pos_communities = nx.circular_layout(hypergraph, **kwargs)

	# set node positions to position of community
	pos = dict()
	for node, community in partition.items():
		pos[node] = pos_communities[community]

	return pos

def _find_between_community_edges(g, partition):

	edges = dict()

	for (ni, nj) in g.edges():
		ci = partition[ni]
		cj = partition[nj]

		if ci != cj:
			try:
				edges[(ci, cj)] += [(ni, nj)]
			except KeyError:
				edges[(ci, cj)] = [(ni, nj)]

	return edges

def _position_nodes(g, partition, **kwargs):
	"""
	Positions nodes within communities.
	"""

	communities = dict()
	for node, community in partition.items():
		try:
			communities[community] += [node]
		except KeyError:
			communities[community] = [node]

	pos = dict()
	for ci, nodes in communities.items():
		subgraph = g.subgraph(nodes)
		pos_subgraph = nx.spring_layout(subgraph, **kwargs)
		pos.update(pos_subgraph)

	return pos


if __name__ == "__main__":
	main()	