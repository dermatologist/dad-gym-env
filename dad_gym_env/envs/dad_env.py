# core modules
import logging.config
import math
import pkg_resources
import random

# 3rd party modules
import numpy as np
import pandas as pd
from numpy import genfromtxt
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .headers import DISEASES
class DadEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, dadvec_file, treatments=[]):
        treatment_no = len(treatments)
        super(DadEnv, self).__init__()

        self.dadvec_file = dadvec_file
        self.treatments = treatments
        (self._rows, self._cols) = self.load_file()
        self.NUMBER_FACTORS = len(DISEASES)
        self._get_actions()
        self.action_space = spaces.Discrete(2 if len(self._actions) == 1 else len(self._actions))
        # Observation space is a vector of length number of factors
        self._get_states()
        self.observation_space = spaces.Box(
                                    low=0, high=1, 
                                    shape=(len(self._states),self.NUMBER_FACTORS), 
                                            dtype=np.uint8)
    
    
    
    """
        Loads DAD file 
        self.received_treatments has all records who received the treatments specified.
    """    
    def load_file(self):
        self.df = pd.read_csv(self.dadvec_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        self.received_treatments = pd.DataFrame(columns=self.df.columns)
        # print(self.df.shape) # (100, 2103)
        for treatment in self.treatments:
            _df = self.df[self.df[treatment] == '1']
            isempty = self.received_treatments.empty
            if isempty:
                self.received_treatments = _df
            else:
                self.received_treatments.append(_df, ignore_index=True)
        return self.received_treatments.shape


    def _get_actions(self):
        _actions = []
        _action = ''
        for index, row in self.received_treatments.iterrows():
            for treatment in self.treatments:
                _action = _action + row[treatment]
            _actions.append(_action)
            _action = ''
        self._actions = self.unique(_actions)
        return(self._actions)

    def _get_states(self):
        self._states = self.received_treatments.filter(DISEASES).to_numpy()
        return self._states
    
    # function to get unique values 
    def unique(self, list1): 
        # insert the list to the set 
        list_set = set(list1) 
        # convert the set to the list 
        unique_list = (list(list_set)) 
        return unique_list

    def step(self, action):
        pass
  
    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
