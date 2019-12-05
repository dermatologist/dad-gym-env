from dad_gym_env import __version__
from dad_gym_env.envs import dad_env

def test_version():
    assert __version__ == '0.1.0'

def test_dad_env():
    dad_env_1 = dad_env.DadEnv("/home/beapen/project/beapen/dad-vec-sample.csv")
    print(dad_env_1.metadata)
    #assert False == True
