#!/usr/bin/env python
# coding: utf-8

# # 8 Queens Puzzle's Solution by Hill-Climbing Algorithm

# ## Initilization of states

# In[1]:


def print_grid(state):
    print("/=====|\n|",end='')
    for i in range(9):
        print(state[i],end='')
        if i%3==2: print("|\n|",end='')
        else: print(end=' ')
    print("=====/\n")


# In[51]:


initial_state = [
    1, 2, 3,
    8, 6, 0,
    7, 5, 4,
]

# Change the goal state according the system/puzzle
# The following goal state is mentioned by George F. Luger in his book
goal_state = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5,
]

# This look-up list reduces the time-complexity in h2 heuristics from O(n * n) to O(n)
goal_state_idx = [None for i in range(9)]

for idx, val in enumerate(goal_state):
    goal_state_idx[val] = idx

print(goal_state_idx)

# Multiple goal states is possible due to symmetry, hence, go with
# forward chaining (data-driven search) so that this solution can be extended to include symmetrical solutions.


# ## Heuristic function definitions

# In[3]:


# No. of tiles out of place heuristics
h1 = lambda state: sum(i != goal_state_idx[state[i]] for i in range(9)) # O(n)

h1(initial_state)


# In[4]:


# Manhattan distance from original place heuristics
def h2(state):
    """
    TC: O(n)
    """
    cost = 0;
    for idx in range(9): # O(n)
        val = state[idx]
        goal = goal_state_idx[val] # O(1)
        temp = abs(idx%3 - goal%3) + abs(idx//3 - goal//3)
        # modulo is column no. and floor division is row no.
        cost += temp

    return cost

h2(initial_state)


# In[5]:


# Combination of the above
h3 = lambda state: h1(state) + h2(state) # O(n * n)

h3(initial_state)


# ## Implementation of Algorithm

# In[6]:


def possibilities(index):
    """
    This function checks for the possible directions to move.

    If a direction is blocked, then the corresponding bit is
    unset using the bit mask for that direction.
    """

    UP    = 0b1000
    DOWN  = 0b0100
    LEFT  = 0b0010
    RIGHT = 0b0001

    moves = 0b1111; # up, down, left, right

    match index//3: # row
        case 0: moves ^= UP
        case 2: moves ^= DOWN
    match index%3: # column
        case 0: moves ^= LEFT
        case 2: moves ^= RIGHT

    return moves


# #### Implementation of Hill Climbing Technique
# 
# Since, there are only 4 possible directions to move and usually 2 or 3 possible moves are available from a state, this doesn't vary much with the implemented steepest ascent/descent algorithm (actually descent here) with the Stochastic First-Choice Hill-Climbing algorithm.

# In[7]:


def hill_climb(current_state, depth, heuristic,depth_limit=10):
    """
    TC: O(n + 4 * heuristic_TC
    function_cost = depth_cost + heuristic_cost

    Depth Limit(g(state)) is added so that the function terminates
    on time, if it has unbounded extrema.
    """

    if (depth > depth_limit): return current_state, float('inf')

    UP    = 0b1000
    DOWN  = 0b0100
    LEFT  = 0b0010
    RIGHT = 0b0001

    zero_index = current_state.index(0); # O(n)
    moves = possibilities(zero_index)

    next_state = None;
    cost = 1e9
    best_move = None

    if moves & UP:
        temp = list(current_state)
        temp[zero_index], temp[zero_index-3] = temp[zero_index-3], temp[zero_index]
        f = depth + heuristic(temp)
        if (f < cost):
            cost = f
            next_state = temp
            best_move = UP


    if moves & DOWN:
        temp = list(current_state)
        temp[zero_index], temp[zero_index+3] = temp[zero_index+3], temp[zero_index]
        f = depth + heuristic(temp)
        if (f < cost):
            cost = f
            next_state = temp
            best_move = DOWN

    if moves & LEFT:
        temp = list(current_state)
        temp[zero_index], temp[zero_index-1] = temp[zero_index-1], temp[zero_index]
        f = depth + heuristic(temp)
        if (f < cost):
            cost = f
            next_state = temp
            best_move = LEFT

    if moves & RIGHT:
        temp = list(current_state)
        temp[zero_index], temp[zero_index+1] = temp[zero_index+1], temp[zero_index]
        f = depth + heuristic(temp)
        if (f < cost):
            cost = f
            next_state = temp
            best_move = RIGHT



    return next_state, cost, best_move


# ## Hill-Climbing solution (Steepest Descent Variant)
# 
# We're using steepest descent, because the heuristic function gives the cost value, hence, we need to minimise the objective function. We chose **h2** heuristics (*manhattan distance*) as a preferred heuristics from trial and error.

# In[15]:


iterations = 20
curr_state = initial_state
prev_cost = float("inf")
depth = 0

print("INITIAL STATE".center(40,"_"))
print_grid(initial_state)
print("_"*40 + "\n")

for i in range(iterations):
    best_neighbour, best_cost, best_move = hill_climb(curr_state,depth,h2)
    best_neighbour = tuple(best_neighbour)

    if prev_cost <= best_cost:
        print(f"Found extrema at iteration no. {i+1}".rjust(40,'_'))
        break

    curr_state = best_neighbour
    prev_cost = best_cost
    depth += 1

print("CONVERGED SOLUTION STATE".center(40,"_"))
print_grid(curr_state)
print("ACTUAL GOAL STATE".center(40,"_"))
print_grid(goal_state)


# ### Random-Restart Hill-climbing
# 
# Since, to achieve a peak, we need to move along a saddle point to achieve it but it may not be always reachable from any given state.

# In[45]:


import random

""" TC: O(restarts * iterations) """

restarts = 4000 # no. of restarts
iterations = 20

random_initial_state = [i for i in range(9)]
overall_best_cost = float('inf')
overall_best_state = None

for restart in range(restarts):
    random.shuffle(random_initial_state)
    print(f"Random restart #{restart}")

    curr_state = random_initial_state
    prev_cost = float("inf")
    depth = 0
    
    # print("INITIAL STATE".center(40,"_"))
    # print_grid(initial_state)
    # print("_"*40 + "\n")
    
    for i in range(iterations):
        best_neighbour, best_cost, best_move = hill_climb(curr_state,depth,h2)
        best_neighbour = tuple(best_neighbour)
    
        if prev_cost <= best_cost:
            print(f"Found extrema at iteration no. {i+1}".rjust(40,'_'))
            break
    
        curr_state = best_neighbour
        prev_cost = best_cost
        depth += 1

    print_grid(curr_state)
    if (prev_cost < overall_best_cost):
        overall_best_cost = prev_cost
        overall_best_state = curr_state


# #### Best solution from random-restart hill-climbing algorithm
# 
# This algorithm may converge at the states, which can be corrected to goal state by *Double Reversal of adjacent tiles heuristics* which is mentioned in **Artificial Intelligence. Structures and Strategies for Complex Problem Solving** by *George F. Luger*.

# In[52]:


print("Total cost of converged state =",overall_best_cost)
print("CONVERGED SOLUTION STATE".center(40,"_"))
print_grid(overall_best_state)
print("ACTUAL GOAL STATE".center(40,"_"))
print_grid(goal_state)

