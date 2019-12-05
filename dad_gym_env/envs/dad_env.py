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

    def step(self, action):
        pass
  
    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
