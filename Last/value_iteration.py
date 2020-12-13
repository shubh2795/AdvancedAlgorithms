import numpy as np
import pprint
import gym
import rubiks_cube_gym
from look_ahead import *

pp = pprint.PrettyPrinter(indent=2)
env = gym.make('rubiks-cube-222-lbl-v0')


def value_iteration(_env, theta=0.0001, discount_factor=1.0):

    V = np.zeros(_env.observation_space.n, dtype = np.int16)
    while True:
        # Stopping condition
        delta = 0
        # Update each state...
        _env.nS =
        for s in range(_env.nS):
            # Do a one-step lookahead to find the best action
            A = one_step_lookahead(s, V)
            best_action_value = np.max(A)
            # Calculate delta across all states seen so far
            delta = max(delta, np.abs(best_action_value - V[s]))
            # Update the value function
            V[s] = best_action_value
            # Check if we can stop
        if delta < theta:
            break

    # Create a deterministic policy using the optimal value function
    policy = np.zeros([_env.nS, _env.nA])
    for s in range(_env.nS):
        # One step lookahead to find the best action for this state
        A = one_step_lookahead(s, V)
        best_action = np.argmax(A)
        # Always take the best action
        policy[s, best_action] = 1.0

    return policy, V


policy, v = value_iteration(env)

print("Policy Probability Distribution:")
print(policy)
print("")

print("Reshaped Grid Policy (0=up, 1=right, 2=down, 3=left):")
print(np.reshape(np.argmax(policy, axis=1), env.shape))
print("")

print("Value Function:")
print(v)
print("")

print("Reshaped Grid Value Function:")
print(v.reshape(env.shape))
print("")
