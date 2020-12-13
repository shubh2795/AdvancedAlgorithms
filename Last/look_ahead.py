import numpy as np
import random


def my_reduce_State(cube):
    # takes a cube representation of the state and returns it as a reduced string
    return ''.join(TILE_MAP[tile] for tile in cube)


def my_move(cube, move_side, repetitions=1):
    # implements a move on cube (array representation)
    # returns the new state as a cube

    if move_side == "R":
        side_cubies_old = np.array([1, 3, 7, 15, 21, 23, 18, 10])
        face_cubies_old = np.array([[8, 9], [16, 17]])
    elif move_side == "L":
        side_cubies_old = np.array([2, 0, 11, 19, 22, 20, 14, 6])
        face_cubies_old = np.array([[4, 5], [12, 13]])
    elif move_side == "F":
        side_cubies_old = np.array([2, 3, 13, 5, 21, 20, 8, 16])
        face_cubies_old = np.array([[6, 7], [14, 15]])
    elif move_side == "B":
        side_cubies_old = np.array([0, 1, 9, 17, 23, 22, 12, 4])
        face_cubies_old = np.array([[10, 11], [18, 19]])
    elif move_side == "U":
        side_cubies_old = np.array([6, 7, 8, 9, 10, 11, 4, 5])
        face_cubies_old = np.array([[0, 1], [2, 3]])
    elif move_side == "D":
        side_cubies_old = np.array([14, 15, 12, 13, 18, 19, 16, 17])
        face_cubies_old = np.array([[20, 21], [22, 23]])

    side_cubies_new = np.roll(side_cubies_old, -2 * repetitions)
    face_cubies_new = np.rot90(face_cubies_old, 4 - repetitions).flatten()
    face_cubies_old = face_cubies_old.flatten()
    # make a copy of old state and make the changes
    cube1 = np.copy(cube)
    np.put(cube1, side_cubies_old, cube[side_cubies_new])
    np.put(cube1, face_cubies_old, cube[face_cubies_new])
    return cube1


def my_look_Ahead_All(env):
    # env has a state, generates all actions possible in this state and
    # returns a list of (nextState, reward, done, action, afterCube)
    allOutcomes = []
    for action in range(0, env.action_space.n):
        move = ["F", "R", "U"][action]
        cube1 = my_move(env.cube, move, 1)
        cube1_r = my_reduce_State(cube1)
        index = env.cube_states[cube1_r]
        reward, done = my_reward(cube1_r)
        allOutcomes.append((index, reward, done, action, cube1))
    return allOutcomes


def my_look_Back_All(env):
    # env has a state, generates all reverse actions possible in this state and
    # returns a list of (beforeState, reward, done, action, beforeCube)
    allOutcomes = []
    cube = env.cube
    cube_r = env.cube_reduced
    for action in range(0, env.action_space.n):
        move = ["F", "R", "U"][action]
        cube1 = my_move(cube, move, 3)
        cube1_r = my_reduce_State(cube1)
        index = env.cube_states[cube1_r]
        reward, done = my_reward(cube_r)  # based on current state
        allOutcomes.append((index, reward, done, action, cube1))
    return allOutcomes


def my_reward(cube_r):
    # scores a cube represented in reduced form (a string)
    if cube_r == "WWWWOOGGRRBBOOGGRRBBYYYY":
        return 100, True
    else:
        return -1, False


TILE_MAP = {
    0: 'W', 1: 'W', 2: 'W', 3: 'W',
    4: 'O', 5: 'O', 6: 'G', 7: 'G', 8: 'R', 9: 'R', 10: 'B', 11: 'B',
    12: 'O', 13: 'O', 14: 'G', 15: 'G', 16: 'R', 17: 'R', 18: 'B', 19: 'B',
    20: 'Y', 21: 'Y', 22: 'Y', 23: 'Y'

}