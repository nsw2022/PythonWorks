import queue

class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self,i1,i2,moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board,self.goal,moves)
    
    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0,1,2]:
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0,3,6]:
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2,5,8]:
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6,7,8]:
            result.append(self.get_new_board(i, i+3, moves))
        return result
    
    def f(self):
        return self.h()+self.g()

    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(9)])
    
    def g(self):
        return self.moves
    
    def __lt__(self,other):
        return self.f() < other.f()
    
    def __str__(self):
        return "----------f(n)=" + str(self.f()) + "\n" + \
               "----------h(n)=" + str(self.h()) + "\n" + \
               "----------g(n)=" + str(self.g()) + "\n" + \
               str(self.board[:3]) + "\n" + \
               str(self.board[3:6]) + "\n" + \
               str(self.board[6:]) + "\n" + \
               "----------"

puzzle = [1,5,2,
          0,4,3,
          7,6,8
          ]
goal = [1,2,3,
        4,5,6,
        7,8,0]

open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle,goal))
closed_set = set()
moves=0
while not open_queue.empty():
    current = open_queue.get()
    print(current)
