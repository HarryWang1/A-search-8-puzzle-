from time import time
from Astar_search import Astar_search
from Astar_search2 import Astar_search2
from puzzle import Puzzle 
from puzzle2 import Puzzle2

## loading current state
state_file = open("Input7.txt","r")
state_file = state_file.readlines()
state = []
for num in state_file[0:4]:
    for elem in num:
        if elem.isdigit():
            state.append(int(elem))


user = int(input("Press 1 for sum of Manhattan distances of tiles from their goal position | Press 2 for sum of Manhattan distances + 2× # linear conflicts"))
if user == 1:

	Puzzle.num_of_instances = 0
	t0 = time()
	astar = Astar_search(state)
	t1 = time() - t0
	print('A*:',astar)
	print('space:', Puzzle.num_of_instances)
	print('time:', t1)
	
	print()
	print('------------------------------------------')

else:

	Puzzle2.num_of_instances = 0
	t0 = time()
	astar = Astar_search2(state)
	t1 = time() - t0
	print('A*:',astar)
	print('space:', Puzzle2.num_of_instances)
	print('time:', t1)
	print()
	print('------------------------------------------')