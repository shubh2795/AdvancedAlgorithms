import gym
import numpy as np  # 1. Load Environment and Q-table structure
import rubiks_cube_gym
import png
from matplotlib import pyplot as plt


def traceBack(s):
    for i in range(0, 1000):
        #env.render()
        a = np.argmax(Q[s, :])
        (s, _, done, _) = env.step(a)
        if done:
            break
    if done:
        print("found goal in", i ,"moves")
    else:
        print("failed after 1000 moves")



env = gym.make('rubiks-cube-222-lbl-v0')
# Q = np.zeros([env.observation_space.n, env.action_space.n])

Q = np.zeros([env.observation_space.n, env.action_space.n], dtype=np.int16)
# env.obeservation.n, env.action_space.n gives number of states and action in env loaded# 2. Parameters of Q-leanring
eta = .628
gma = .9
epis = 10000
rev_list = []  # rewards per episode calculate# 3. Q-learning Algorithm
for i in range(epis):
    # Reset environment
    s = env.reset(scramble="R U R' U' R' F R2 U' R' U' R U R' F'")
    rAll = 0
    d = False
    j = 0
    # The Q-Table learning algorithm
    while j < 99:
        # env.render()
        j += 1
        # Choose action from Q table
        a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        # Get new state & reward from environment
        s1, r, d, _ = env.step(a)
        # Update Q-Table with new knowledge
        Q[s, a] += eta * (r + gma * np.max(Q[s1, :]) - Q[s, a])
        rAll += r
        s = s1
        if d:
            break
    rev_list.append(rAll)
    traceBack(s)
    # arr = env.render()

print("Reward Sum on all episodes " + str(sum(rev_list) / epis))
print("Final Values Q-Table", Q)
