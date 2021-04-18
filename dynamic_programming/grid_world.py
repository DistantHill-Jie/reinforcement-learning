"""
Python  implementation of 4*4 Grid World game by Dynamic Programming 

"""

states = [i for i in range(16)]
state_values = [0 for _ in range(16)]

actions = ['n', 'e', 's', 'w'] # North, East, Sourth, West
ds_actions = {'n': -4, 'e': 1, 's': 4, 'w': -1} # contribution to state for each action

gamma = 1.00 # discount factor

def nextState(s, a):
    next_state = s

    # the boundary condition
    if (s%4 == 0 and a == 'w') or (s<4 and a == 'n') or ((s+1)%4 == 0 and a == 'e') or (s>11 and a == 's'):
        pass
    else:
        ds = ds_actions[a]
        next_state = s + ds
    return next_state

# reward of a state
def rewardOf(s):
    return 0 if s in [0, 15] else -1

def isTerminateState(s):
    return s in [0, 15]

def getSuccessors(s):
    successors = []
    if isTerminateState(s):
        return successors
    for a in actions:
        next_state = nextState(s, a)
        successors.append(next_state)
    return successors

def updateValue(s):
    successors = getSuccessors(s)
    newValue = 0
    num = 4
    reward = rewardOf(s)
    for next_state in successors:
        newValue += 1.00/num * (reward + gamma * state_values[next_state])

    return newValue

def performOneIteration():
    newValue = [0 for _ in range(16)]
    for s in states:
        newValue[s] = updateValue(s)
    global state_values
    state_values = newValue
    print(state_values)

def printValue(v):
    for i in range(16):
        print('{0:>6.2f}'.format(v[i]), end = " ")
        if (i+1) % 4 == 0:
            print('')
    print()


def main():
    max_iteration = 160
    cur_iteration = 0
    while cur_iteration <= max_iteration:
        print('Iteration No.{0}'.format(cur_iteration))
        performOneIteration()
        cur_iteration += 1
    printValue(state_values)



if __name__ == '__main__':
    main()

