from dad_gym_env import __version__
from dad_gym_env.envs import dad_env, headers

def test_version():
    assert __version__ == '0.1.0'

def test_dad_env():
    dad_env_1 = dad_env.DadEnv(
        "/home/beapen/project/beapen/dad-vec-sample.csv", #"/home/beapen/project/beapen/dad-vec-sample.csv",
        # http://www.health.gov.on.ca/en/pro/programs/ecfa/docs/qbp_gi.pdf
        # 2NM - Inspection large intestine
        # 2NK - Inspection small intestine
        # 2NA - Inspection esophagus
        # 2NF - Inspection stomach
        treatments=['2NM', '2NA', '2NA', '2NF']
        )
    #print(dad_env_1.metadata)
    #assert False == True

def test_get_index():
    print('AGRP_F_D: ', headers.HEADERS.index('AGRP_F_D')) # 2 / 2103
    print('GENDER: ', headers.HEADERS.index('GENDER')) # 3 / 2103
    print('ADM_CAT: ', headers.HEADERS.index('ADM_CAT')) # 5 / 2103
    print('DIS_DISP: ', headers.HEADERS.index('DIS_DISP')) # 8 / 2103
    print('A01: ', headers.HEADERS.index('A01')) # 10 / 2103
    print('Z99: ', headers.HEADERS.index('Z99')) # 1485 / 2103
    print('8ZZ: ', headers.HEADERS.index('8ZZ')) # 2098 / 2103
    print('TLOS_CAT: ', headers.HEADERS.index('TLOS_CAT')) # 2099 / 2103
