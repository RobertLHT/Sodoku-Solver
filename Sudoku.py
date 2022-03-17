import numpy as np

class sudoku:

    # Initialize puzzle board and answer board
    def __init__(self):

        # In order to generate a sudoku puzzle
        # https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
        # https://gamedev.stackexchange.com/questions/56149/how-can-i-generate-sudoku-puzzles
        # This code use fixed puzzle
        self.puzzle = np.array(
              [['4', '#', '7', '#', '#', '9', '#', '8', '3'],
               ['#', '#', '#', '3', '#', '#', '#', '#', '2'],
               ['3', '2', '#', '#', '8', '6', '7', '4', '1'],
               ['#', '#', '2', '#', '#', '3', '1', '#', '#'],
               ['#', '#', '1', '8', '6', '#', '#', '#', '5'],
               ['6', '4', '#', '9', '#', '1', '2', '7', '8'],
               ['#', '7', '#', '#', '2', '#', '#', '#', '#'],
               ['#', '#', '#', '6', '#', '4', '#', '2', '7'],
               ['2', '6', '4', '#', '3', '#', '5', '#', '#']])
        
        self.answer = self.puzzle.copy()
        self.solved = False
    
    # Display puzzle to user 
    # Learned how to display a puzzle board
    # https://stackoverflow.com/questions/28282717/display-2d-sudoku-board-in-python
    def display_puzzle(self):
        print("          Puzzle\n")

        # Display each column and row in order
        for i in range(9):
            print("  ".join(self.puzzle[i][:3]), end=" | ")
            print("  ".join(self.puzzle[i][3:6]), end=" | ")
            print("  ".join(self.puzzle[i][6:]))

            if i ==2 or i ==5:
                print("---------------------------")
    
    # Display answer to user
    # Learned how to display a puzzle board
    # https://stackoverflow.com/questions/28282717/display-2d-sudoku-board-in-python
    def display_answer(self, title = "      Your Answer\n"):
        print(title)

        # Display each column and row in order
        for i in range(9):
            print("  ".join(self.answer[i][:3]), end=" | ")
            print("  ".join(self.answer[i][3:6]), end=" | ")
            print("  ".join(self.answer[i][6:]))

            if i ==2 or i ==5:
                print("---------------------------")
    
    # Check answer with given puzzle
    def check_answer(self):
             
        # Check if the answer match the puzzle
        for i in range(9):
            for j in range(9):
                if self.puzzle[i,j] == "#":
                    continue
                else:
                    # Print error message if puzzle and answer do not match
                    if self.puzzle[i,j] != self.answer[i,j]:
                        print(f"Your answer does not match the puzzle at row: {i+1}, col: {j+1}")
                        return False
                    
        # Check if the answer contains "#"
        if np.sum(np.isin(self.answer,"#")):
            print("Your answer should not contain \"#\"")
            return False


        # Check Normal condition
        
        # Check row and col
        for i in range(9):
            if len(set(self.answer[i]))!=9:
                print(f"The row: {i} contains duplicate values")
                return False
            if len(set(self.answer[:,i]))!=9:
                print(f"The col: {i} contains duplicate values")
                return False


        # Check each squre for answer
        for i in range(0,9,3):
            for j in range(0,9,3):
                if len(set(self.answer[i:i+3,j:j+3].reshape(-1).tolist()))!=9:

                    return False   

        # Return true if it matchs
        self.solved = True
        return True
    
    
    # "check_place" and "generate_answer" are used to solve the puzzle
    # We use backtracking to solve the sudoku problem
    # Methods are learned from 
    # https://leetcode.com/problems/sudoku-solver/
    # https://leetcode-cn.com/problems/sudoku-solver/solution/zi-cong-wo-xue-hui-liao-hui-su-suan-fa-zhong-yu-hu/
    # https://www.geeksforgeeks.org/backtracking-introduction/

    # Check whether the number can be placed at the given location
    def check_place(self,row, col, num):
    
        # Check number in row and col
        if num in self.answer[row,:]:
            return False
        if num in self.answer[:,col]:
            return False
        
        # Check each block
        i = row//3
        j = col//3
        if num in self.answer[i*3:i*3+3,j*3:j*3+3].reshape(-1).tolist():
            return False
        
        return True
    
    # Using backtrack to solve the puzzle
    def generate_answer(self, row=0, col=0):

        # Base case, after searched all location 
        if row == 9:
            return True

        # Meet the end of the row, start search a new row
        if col == 9:
            return self.generate_answer(row+1)
        
        # If the place is "#", we can start find answer
        if self.answer[row, col] == "#":
            for i in range(1,10):

                # Check all possible number at the location
                if self.check_place(row,col,str(i)):
                    
                    # Start backtracking
                    # Set a possible number in place
                    self.answer[row, col] = str(i)
                    
                    # Check if we place a possible number, can we also
                    # find answer for the following location. If yes, return
                    # True
                    if self.generate_answer(row, col+1):
                        return True
                    else:
                        # If not, backtrack to the original value
                        self.answer[row,col] = "#"
        else:
            # If the place already has a value, searh the next location
            return self.generate_answer(row,col+1)
        
        # If we cannot find a solution, return False
        return False
    
    # Display the answer to user
    def find_answer(self):
        # Reset the answer board for solver
        self.answer = self.puzzle.copy()
        self.generate_answer()
        
        # Check if the there is a solution for the puzzle
        if self.check_answer():
            print("Solution find!\n")

            self.display_answer("           Answer")
            solved = True
        # Print error message if not
        else:
            print("There is no valid solution")
    # Allow user to modify the answer
    def modify_answer(self,row, col, num):
        self.answer[row-1,col-1] = str(num)
        self.display_answer()

    # Reset answer
    def reset(self):
        self.answer = self.puzzle.copy()