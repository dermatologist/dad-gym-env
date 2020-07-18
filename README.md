# DAD-GYM-ENV (Dadge - pronounced dadaji)
## Reinforcement Learning env based on Discharge Abstract Database

This is an experimental [OpenAI Gym](http://gym.openai.com/) environment for reinforcement learning based on Discharge Abstract Database. Reinforcement learning (RL) is an area of machine learning concerned with how software agents ought to take actions in an environment in order to maximize some notion of cumulative reward. For a list of interventions, Dadage gives a random patient state (demographics + comorbidities) and an action space of known combinations of interventions. The reward is (10 - Total Length of Stay class). This requires a one-hot encoded version of DAD. The code for creating this is [here:](https://github.com/dermatologist/hephaestus/blob/develop/src/hephaestus/utils/dad-vector.py). Please note that this repository does not contain any primary/derived data from discharge abstract database. The approach may be extendable to other similar databases.

This is an experimental system for demo purposes only. This is not tested and is unlikely to have practical use because of various factors. This is part of our research on machine learning models in healthcare and demonstrates a novel approach based on DAD. Next step is to design an agent using [dopamine](https://github.com/google/dopamine).

### How to use

Dadage uses [poetry](https://poetry.eustace.io/) for dependency management.
Use:

```
poetry install
```

There is a sample agent in tests: Provide the vectorized DAD file and list of CCI codes for interventions, and:

```
poetry run pytests tests -s
```

### Cite

Please cite if you use this concept in your research.  Here
is an example BibTeX entry:

```

@misc{eapenbr2019qrmine,
  title={Dadage - Reinforcement Learning environment based on discharge abstract database},
  author={Eapen, Bell Raj and contributors},
  year={2019},
  publisher={GitHub},
  journal = {GitHub repository},
  howpublished={\url{https://github.com/dermatologist/dad-gym-env}}
}

```


This software was designed and tested using Compute Canada resources.

#### Contact
* [Bell Eapen](https://nuchange.ca)

#### Disclaimer
*Parts of this material are based on the Canadian Institute for Health Information Discharge Abstract Database Research Analytic Files (sampled from fiscal years 2014-15). However the analysis, conclusions, opinions and statements expressed herein are those of the author(s) and not those of the Canadian Institute for Health Information.*
