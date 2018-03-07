# Model Proposal for A SIR-based Model of the Spread of Political Misinformation through Social Networks

Anant Marur

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
The model aims to provide insight into how unreliable information propagates throughout a social network. Specifically, the model aims to emulate how unreliable publications harness the willingness of agents to believe political content shared by users with similar political leanings. This is an issue that is becoming increasingly prevalent with the rising importance of social media in information exchange, especially in the realm of politics.

&nbsp;  
### Justification
****
The relevant agents in this model are not those agents who derive their information primarily from a centralized, reputable news source. They are agents who primarily are fed their information by other agents, and following this trail upstream often yields what are clearly objectively untrustworthy news sources. What makes these news sources credible is no longer constitutive of the sources themselves – credibility is instead given by the ‘sharer’ of the information. It is due to this ‘network’ of credibility, that often creates contradictory perceptions of authenticity depending on how one comes across a specific source, that agent based modeling bubbles to the top as the best approach.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

Politically, social media often has an echo-chamber effect. Every agent, has their own customized stream of information being fed to them on social media. Moreover, this stream often creates a feedback loop back into their biases, which is one of the reasons politics is becoming so heavily polarized.

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_Description of the environment in your model. Things to specify *if they apply*:_

* _Boundary conditions (e.g. wrapping, infinite, etc.)_
* _Dimensionality (e.g. 1D, 2D, etc.)_
* _List of environment-owned variables (e.g. resources, states, roughness)_
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your environment
# This may be a set of "patches-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any patch methods/procedures you have. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 2) Agents
 
 _Description of the "agents" in the system. Things to specify *if they apply*:_
 
* _List of agent-owned variables (e.g. age, heading, ID, etc.)_
* _List of agent-owned methods/procedures (e.g. move, consume, reproduce, die, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your agents
# This may be a set of "turtle-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any agent methods/procedures you have so far. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_Description of the topology of who interacts with whom in the system. Perfectly mixed? Spatial proximity? Along a network? CA neighborhood?_
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. Step 1
2. Step 2
3. Etc...

&nbsp; 
### 4) Model Parameters and Initialization

_Describe and list any global parameters you will be applying in your model._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_
