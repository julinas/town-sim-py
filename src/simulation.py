# BSD 3-Clause License
#
# Copyright (c) 2018, Augmented Design Lab
# All rights reserved.
import copy
import time

from agent import Agent
from landscape import Landscape
from lot import Lot
import gc

class Simulation:
	def __init__(self, size=200):
		self.landscape = Landscape(size, size, self)
		self.agents = []
		for i in range(100): #200
			self.add_agent(Agent(self.landscape, self))

	def step(self, phase, maNum=10, miNum=400, byNum=2000, brNum=5000):
		killlist = []
		for agent in self.agents:
			agent.step(self.landscape)
			if agent.water < 0 or agent.resource < 0:
				killlist.append(agent)
		for agent in killlist:
			self.kill(agent)
		gc.collect()
		self.landscape.step(phase, maNum, miNum, byNum, brNum)

	def add_agent(self, agent):
		self.agents.append(agent)

	def kill(self, agent):
		self.agents.remove(agent)
		self.landscape.remove_agent(agent)

	def view(self, step):
		return self.landscape.view(step)

	def output(self, filename):
		self.landscape.output(filename)
