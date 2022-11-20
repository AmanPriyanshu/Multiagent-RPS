import numpy as np

class Agent:
	def __init__(self, loc):
		self.loc = loc
		self.create_new()

	def create_new(self):
		if np.random.random()<=0.33:
			agent_type = "rock"
		elif np.random.random()<=0.66:
			agent_type = "scissor"
		else:
			agent_type = "paper"
		self.agent_type = agent_type