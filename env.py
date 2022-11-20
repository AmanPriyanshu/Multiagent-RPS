import cv2
import numpy as np
from agent import Agent

class Environment:
	def __init__(self, N=100, size=100):
		self.N = N
		self.size = size
		self.map = np.zeros((size, size, 3))

	def random_initialize(self, AgentClass, limit=1000):
		agents = []
		locs = []
		for n in range(self.N):
			loc = np.random.randint(0, self.size), np.random.randint(0, self.size)
			c = 0
			while str(loc[0])+"&&"+str(loc[1]) in locs and c<=limit:
				loc = np.random.randint(0, self.size), np.random.randint(0, self.size)
				c += 1
				if c==limit:
					raise Exception("Size of map too small! for the number of agents") 
			locs.append(str(loc[0])+"&&"+str(loc[1]))
			agent = AgentClass(loc)
			agents.append(agent)
		return agents

	def gen_map_at_time_t(self, agents):
		self.map = np.zeros((self.size, self.size, 3))
		for agent in agents:
			color = 0 if agent.agent_type=="rock" else 1 if agent.agent_type=="paper" else 2
			self.map[agent.loc[0], agent.loc[1], color] = 1

	def display_map(self):
		cv2.imshow('img', cv2.resize(self.map,(self.size*5,self.size*5)))
		cv2.waitKey(0) 
		cv2.destroyAllWindows()

if __name__ == '__main__':
	env = Environment()
	env.display_map()
	agents = env.random_initialize(Agent)
	env.gen_map_at_time_t(agents)
	env.display_map()