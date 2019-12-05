# core modules
import logging.config
import math
import pkg_resources
import random

# 3rd party modules
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
class DadEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    

    def __init__(self, dadvec_file, treatment_no = 1):
        super(DadEnv, self).__init__()
        self.NUMBER_FACTORS = 2000
        # Action spaces are discrete with # = n^2 interventions considered
        if treatment_no ^ 2 < 2:
            discrete_actions = 2
        else:
            discrete_actions = treatment_no ^ 2
        self.action_space = spaces.Discrete(discrete_actions)
        # Observation space is a vector of length number of factors
        self.observation_space = spaces.Box(
                                    low=0, high=1, 
                                    shape=(1,self.NUMBER_FACTORS), 
                                            dtype=np.uint8)

    def step(self, action):
        pass
  
    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
