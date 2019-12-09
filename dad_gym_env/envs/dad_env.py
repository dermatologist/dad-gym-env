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


def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


class DadEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.dadvec_file = "/home/beapen/projects/def-archer/beapen/dad-vector.csv"
        self.treatments = ['2NA', '2NM', '2NK', '2NF', '3OZ']
        super(DadEnv, self).__init__()
        treatment_no = len(self.treatments)
        self.full_record = None
        self.df = None
        self.received_treatments = None
        self.observation = None
        self.reward = 5



    """
        Loads DAD file 
        self.received_treatments has all records who received the treatments specified.
    """

    # Getter must be defined first
    @property
    def dadvec_file(self):
        return self._dadvec_file

    @dadvec_file.setter
    def dadvec_file(self, dadvec_file):
        self._dadvec_file = dadvec_file

    @property
    def treatments(self):
        return self._treatments

    @treatments.setter
    def treatments(self, treatments):
        self._treatments = treatments

    def load_file(self):
        self.df = pd.read_csv(self.dadvec_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        # Create a blank table with the column headers
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
        # This is need to remove the copy warning in adding new column
        pd.options.mode.chained_assignment = None  # default='warn'
        self.received_treatments['Action'] = _actions
        self._actions = unique(_actions)
        return self._actions

    def get_random_action(self):
        return random.choice(self._actions)

    def _get_states(self):
        self._states = self.received_treatments.filter(DISEASES).to_numpy()
        return self._states

    def get_random_state(self):
        return random.choice(self._states)

    # function to get unique values

    """
    STEP function
    TODO: Document
    """

    def step(self, action):
        self.done = True
        self.info = {"action": action}

        # Create a blank table with the column headers
        # Candidates have received all treatments in an action
        # self.received_treatments have received one or more treatments in an action
        self.candidates = pd.DataFrame(columns=self.df.columns)

        for i in range(len(action)):
            if int(action[i]) == 1:
                isempty = self.candidates.empty
                # if empty add the first condition
                if isempty:
                    _df = self.received_treatments[self.received_treatments[self.treatments[i]] == '1']
                    self.candidates = _df
                else:
                    # else filter based on condition
                    self.candidates = self.candidates[self.candidates[self.treatments[i]] == '1']
        tlos = 0
        ct = 0
        for index, row in self.received_treatments.iterrows():
            tlos = tlos + int(row['TLOS_CAT'])
            ct = ct + 1
        average_tlos = tlos / ct
        self.reward = int(10 - average_tlos)

        print("Received: ", self.received_treatments.shape)
        print("Candidates: ", self.candidates.shape)

        if self.full_record is not None:
            _full_record = self.full_record[self.full_record['Action'] == action]
            isempty = _full_record.empty
            if not isempty:
                self.reward = 10 - (int(_full_record['TLOS_CAT'].iloc[0]))
        self.full_record = self.candidates.sample(n=1)
        self.observation = self.full_record.filter(DISEASES).to_numpy()
        return self.observation, self.reward, self.done, self.info

    def reset(self):
        (self._rows, self._cols) = self.load_file()
        self.NUMBER_FACTORS = len(DISEASES)
        self._get_actions()
        self.action_space = spaces.Discrete(2 if len(self._actions) == 1 else len(self._actions))
        # Observation space is a vector of length number of factors
        self._get_states()
        self.observation_space = spaces.Box(
            low=0, high=1,
            shape=(1, self.NUMBER_FACTORS),
            dtype=np.uint8)

    def render(self, mode='human'):
        print(f'Observtion: {self.observation}')
        print(f'Reward: {self.reward}')

    def close(self):
        pass
