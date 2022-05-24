# snake_game

## Simple snake game written in python using pygame library. Project created for the purpose of testing DQN algorithm

### To setup clone the repository. After cloning this repository create a virtual enviroment and install requirements

```console
python -m venv C:\your\directory\here
```

```console
C:\your\directory\here\Scripts\activate.ps1
```

```console
pip install -r requirements.txt
```

After setup if you want to simply play a game by yourself, run *run_game.py* file. You can choose here to either control snake or run a simple algorithm which avoids walls and tail and goes in the direction of the fruit. Aforementioned algorithm is in the *auto.py* file.

## Deep Reinforcment learning

This project's primary goal was to teach a computer to play a snake game. For this reason in *model.py* file is specified the structure of the neural network and in *dqn_agent.py* and *train.py* files are stored classes and functions used to train the agent.

Best model weights are stored in *model.pth* file. All enviroment functions are primary in *game.py* file. Additional classes and functions are in *additional_functions.py* and *game_objects.py* files.

Inputs for the algorithm are described in *additional_functions.py* in *get_state()* function.

To watch the trained agent run the *test.py* file.

Computer gets pretty good with avoiding walls, but is not consistent with following the fruit and sometimes runs itself into a corner. If I manage to improve this algorithm the new version will be uploaded to this github repository.
