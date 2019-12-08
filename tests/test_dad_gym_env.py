from dad_gym_env import __version__
from dad_gym_env.envs import dad_env, headers
import pytest

"""
        http://www.health.gov.on.ca/en/pro/programs/ecfa/docs/qbp_gi.pdf
        2NM - Inspection large intestine
        2NK - Inspection small intestine
        2NA - Inspection esophagus
        2NF - Inspection stomach
        3OZ - Imaging intervention 

        "/home/beapen/project/beapen/dad-vec-sample.csv",
"""
@pytest.fixture
def new_env():
    dad_env_ = dad_env.DadEnv(
        "/home/beapen/projects/def-archer/beapen/dad-vec-sample.csv", 
        treatments=['2NA', '2NM', '2NK', '2NF', '3OZ']
        )
    return dad_env_

def test_version():
    assert __version__ == '0.1.0'
    

def test_dad_env(new_env):
    assert {'render.modes': ['human']} == new_env.metadata

def test_get_actions(new_env):
    assert new_env._get_actions() # List is not empty

def test_get_random_action(new_env):
    print("\n", new_env._get_actions(), "\n")
    print(new_env.get_random_action())

def test_get_random_state(new_env):
    print("\n", new_env._get_states(), "\n")
    print(new_env.get_random_state())    

def test_get_states(new_env):
    assert new_env._get_states().any()

# def test_get_index():
#     print('AGRP_F_D: ', headers.HEADERS.index('AGRP_F_D')) # 2 / 2103
#     print('GENDER: ', headers.HEADERS.index('GENDER')) # 3 / 2103
#     print('ADM_CAT: ', headers.HEADERS.index('ADM_CAT')) # 5 / 2103
#     print('DIS_DISP: ', headers.HEADERS.index('DIS_DISP')) # 8 / 2103
#     print('A01: ', headers.HEADERS.index('A01')) # 10 / 2103
#     print('Z99: ', headers.HEADERS.index('Z99')) # 1485 / 2103
#     print('8ZZ: ', headers.HEADERS.index('8ZZ')) # 2098 / 2103
#     print('TLOS_CAT: ', headers.HEADERS.index('TLOS_CAT')) # 2099 / 2103
