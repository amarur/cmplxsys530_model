# Model Proposal for A SIR-based Model of the Spread of Political Misinformation through Social Networks

Anant Marur

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018

&nbsp; 

__*LS COMMENTS:*__
*This is completely fine conceptual start. At this point in the course, however, it is really important to have some code or at the very least pseudocode developed (hence the prompts for this assignment). Model building can be a complicated process that involves a lot of trial and error along with a lot of time required for model verification and analysis. This is especially true for folks who might not be coming from a strong programming background. As such, if you want to be ready to present in April, I'd highly encourage you to put some time in now to make sure you'll have something to talk about.*

&nbsp; 

### Goal 
*****
 
The model aims to provide insight into how unreliable information propagates throughout a social network. Specifically, the model aims to emulate how biased or inaccurate information spreads through politically homogeneous clusters in a social network and creates an echo chamber effect. This is an issue that is becoming increasingly prevalent with the rising importance of social media in information exchange, especially in the realm of politics.


&nbsp;  
### Justification
****
The relevant agents in this model are not those agents who derive their information primarily from a centralized, reputable news source. They are agents who primarily are fed their information by other agents, and following this trail upstream often yields what are clearly objectively untrustworthy news sources. What makes these news sources credible is no longer constitutive of the sources themselves – credibility is instead given by the ‘sharer’ of the information. It is due to this ‘network’ of credibility, that often creates contradictory perceptions of authenticity depending on how one comes across a specific source, that agent based modeling bubbles to the top as the best approach.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

Politically, social media often has an echo-chamber effect. Every agent, has their own customized stream of information being fed to them on social media. Agents typically give more credence to those with similar beliefs, which often creates a feedback loop back into their biases, which is one of the reasons politics is becoming so heavily polarized. 
Consequently, I expect to see misinformation spread extremely quickly throughout homogeneous clusters. On the flip side, more heterogeneous sections of the network will be much less susceptible to allowing the misinformation propagation. 

&nbsp; 

__*LS COMMENTS:*__
*As currently described below, it looks like spread but not cluster belief homogeneity is being incorporated, which seems to be a key dynamic of interest for you. Figuring out how to computationally implement this feature - both in terms of correlating belief with network structure and incorporating it into the information transmission process - will be critical for this project.*



## Model Outline
****
&nbsp; 
### 1) Environment

The environment of the model consists of a network connecting the agents (which can be thought of as nodes in an undirected graph). The environment is negligible other than the connections between the nodes, as the agents are not moving, and all other external effects on agents’ behavior are controlled by the global variables. 

&nbsp; 

### 2) Agents
 
 Agents represent users in a social network. In the network, they are represented as nodes.
 
* __Variables__
	- _Political Leaning_: Every agent has a political leaning that exists on a scale from -1 (conservative) to 1 (liberal). Initially, this variable will be static. Time allowing, I may iterate the model to make  this variable slightly decrease with the acceptance of conservative misinformation, and the opposite for liberal misinformation.

	- _Classification_: Each agent is classified as a Spreader, Ignorant, or Stifler. An agent’s classification is the primary influence on its behavior in interactions with other agents. 
		1. _Spreaders_: As the name implies, they spread information. They have the following interactions:
			- Contact with a Spreader: nothing
			- Contact with an Ignorant: Either:
				- Convert them to a Spreader with a probability equal to the Spreading Rate (global variable).
				- Convert them to to a Stifler with a probability equal to the Refusing Rate (global variable).
		2. _Ignorants_: Those who have not internalized a rumor. They have no effect on whoever they interact with.
		3. _Stiflers_: Those who actively stop the spread of misinformation.
			- Contact with a Stifler: Turn into a Stifler themselves with a probability equal to the Stifling Rate (global variable).

&nbsp;

__*LS COMMENTS:*__
*How are you conceiving of "stifling" as spreading? In the standard SIR model, stifling might be seen as "resistant" which is not something is usually understood as passing between agents. Totally ok to incorporate that here, but will need to motivate it more.*


* __Methods__:The only method for agents in this model is interaction with neighbors, the specifics of which are explained above.


__*LS COMMENTS:*__
*Though the variables mention the spread process, need more details in here that layout exactly how that spread will happen and how it will incorporate the respective agent variables. Also, in order to get at your process of interest, will need to make sure to specifiy exactly how political leaning will be interacting with the political content of information (which itself will need to be handled with its own variable) in its spread.*

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

The only method for agents in this model is interaction with neighbors, the specifics of which are explained above.Agents will interact with each of their neighbors (adjacent nodes) on a given step. The network is static (at least in the first iteration of the model), so each agent will interact with the same agents on each step. In a future iteration, I may introduce random interactions with 2nd level neighbors as well.

__*LS COMMENTS:*__
*Need to specify what type of network structure will be used here and how you will be generating it.*


**_Action Sequence_**

On a given step, every single agent will iterate through each of its neighbor nodes and interact with them. However, any pair of agents will only interact once. That is to say, if A interacts with B while iterating, then when B iterates to A during its cycle, they will not repeat their interaction. Otherwise, we would only see every other actual cycle, which would muddle the results. I will use the NetworkX python library to implement the graph. The ordering in which the agents do their neighbor interactions will be randomly determined on each step (as long as this is fast, otherwise they will go in order each time). 

&nbsp; 
### 4) Model Parameters and Initialization

* __Global Variables__: Spreading Rate, Refusing Rate, Stifling Rate. Their roles are explained above in the ‘Agents’ section.
* __Initialization__: There will be two modes, clustered and random. In both modes, agents will have no more neighbors than a quarter of the total amount of agents, in order to simulate a real social network (this is a very generous upper limit). In a future iteration, a small fraction of agents may be designated as influencers (representing public figures and publications themselves), who will be exempt from the upper bound.
	- _Clustered mode_: this mirrors the real world. People surround themselves on social media primarily with those who share their views, meaning political leanings will be clustered together. I will implement this mode first, since it is more useful. The degree to which this occurs will be varying (likely random) across the network, to simulate real world conditions. To initialize this mode, I will first randomly assign agents their political leanings. After that, while creating connections, I will create a connection with increased likelihood when agents are closer to each other on the spectrum.
	- _Random mode_: Random mode: agents are placed in the network regardless of their political leaning, creating a more homogenous mix.

__*LS COMMENTS:*__
*Refer to this week's lectures for how to computationally implement these sorts of networks in a principled manner.*
*Initialization will also need to involve choices about number of agents, proportion that start as "stiflers", "spreaders" etc. and their positions in the network, and information that will be entered into the system.*

&nbsp; 

### 5) Assessment and Outcome Measures

Quantitative measures to measure the success of the model will include measuring the propagation rate within homogeneous vs. heterogeneous clusters, as well as graphs of the trends between the global variables and the propagation rate. Qualitative measurements will include observing the clustered behavior, as well as seeing if the model reaches any sort of equilibrium, and if so, under what circumstances.

&nbsp; 

### 6) Parameter Sweep

All of the global variables will be on a scale from 0 to 1, and all will be able to be altered when the model is run to observe their various effects on behavior. I’m especially interested to see how the Stifling Rate affects homogenous and heterogenous clusters of the network differently, and if stiflers embedded in homogenous clusters are able to have any effect at all.  

__*LS COMMENTS:*__
*I would suggest also thinking about network structure and size as type of parameter in its own right*
