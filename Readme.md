# INF 1340 Midterm project - Sudoku

## Overview

This project performs a simple Sudoku game that contains three features.

1. Check whether the user's solution is a valid sudoku answer 
2.  Allow user to modify their answer 
3. Find a possible sudoku solution to user



## Basic rules

The sudoku is a 9*9 board that contains numbers {1, 2, 3, 4, 5, 6, 7, 8, 9}.

For example, here is a typical sudoku board in the program.

``` 
4  #  7 | #  #  9 | #  #  3
#  #  # | #  #  # | #  #  2
#  2  # | #  #  # | 7  #  1
---------------------------
#  #  2 | #  #  3 | 1  #  #
#  #  1 | 8  #  # | #  #  5
#  #  # | #  #  # | 2 #  #
---------------------------
#  7  # | #  2  # | #  #  #
#  3  # | #  #  # | #  #  7
#  #  4 | #  #  # | #  #  #
```

The 9*9 board are divided into 9  3 * 3 blocks, and# indicates that you need to place a number where need to satisfices the following rules:

1. Each row contains numbers 1-9 without duplication
2. Each column contains numbers 1-9 without duplication
3. Each block contains numbers 1-9 without duplication

## How to Run the Sudoku Game

### Required packages

- Numpy

If you do not have numpy install on your workspace 

Using

``` shell
pip install numpy
```

to download required package



### Getting Start 

There are two files in the project

- Sudoku.py
- main.py

Download these two files in your local workspace, and make sure these two files are on the same directory.

Use the following code on your terminal to start the game

```shell
python main.py
```



### Play the Game

#### Description 

The game contains two boards, puzzle board and answer board. The puzzle board is the sudoku question, and the answer board is where you solve the sudoku. After you place numbers on the answer board, your answer will be checked with the puzzle board. You can only place the number at the location where it is # in the puzzle board. If you change the existed value in answer board, the answer board will not match the puzzle board. 

You can always check your input answer and the puzzle in the game, and if you forget which location is #, you can always reset your answer, but your input history will also be reset. Once you find a possible answer, you can check whether your answer is valid, if your answer is valid. You can always return the game to try different answers or you can quit directly. Also, the game can find a possible solution, and the solution is stored on the answer board and displayed to the user. At that time, you can always return the game to try different answers or you can quit directly.

#### Play it step by step

At the beginning, it will print 

``` 
Press 1 to start play a sudoku game or -1 to quit:
```

You can input **1** to start or **-1** to quit the game

After you start a sudoku game, the games shows like that

``` 
Game start!

(Puzzle board here)

-Input 1 to display the puzzle
-Input 2 to display the answer
-Input 3 to fill the puzzle
-Input 4 to check your answer
-Input 5 to generate an answer
-Input 6 to reset the answer
-Input -1 to quit

Please input your choice: 
```

There are seven available options

- **Input 1 to show the puzzle**

Check the puzzle that you need to solve.

```
(puzzle board here)
```

- **Input 2 to show the answer**

Check your input answer.

```
(answer board here)
```

- **Input 3 to fill the puzzle**

Input the number at the given row and column index on the puzzle.

For example, if you want to input number 8 at 3rd row and 1st col.

```
Start fill your answer

Row index (1-9) or -1 to stop fill puzzle: 3
Column index (1-9): 1
Input number: 8

      Your Answer

4  #  7 | #  #  9 | #  #  3
#  #  # | #  #  # | #  #  2
8  2  # | #  #  # | 7  4  1
---------------------------
#  #  2 | #  #  3 | 1  #  #
#  #  1 | 8  #  # | #  #  5
#  #  # | #  #  1 | 2  7  8
---------------------------
#  7  # | #  2  # | #  #  #
#  3  # | #  #  # | #  #  7
#  6  4 | #  #  # | 5  #  #
```

Once you finished the placement, input -1 to the row index to quit.

```
Row index (1-9) or -1 to stop fill puzzle: -1
```

***Important***: *You need to fill the number one by one, and there is no function that allows you to fill multiple numbers at once*

- **Input 4 to check your answer**

It will check if your answer is valid and matches the puzzle.

If yes, it prints

``` 
Solved, you got it.
Press 1 to continue play or -1 to quit:
```

you can enter **1** to continue to play or **-1** to quit the game

If not, it shows where you have the error. And then you can modify your answer later.

- **Input 5 to display the answer**

Entering 5 to find a possible answer to the puzzle, and it will store the result in the answer board. You can either enter **1** to continue to try different answer or **-1** to quit the game after solution has been found. 

```
(Generated answer here)
Press 1 to continue play or -1 to quit: -1

See you in another game!
```

***Important***: *After you find an answer, the result will be stored on the answer board. And if you chose continue to play, it will show the answer when you trying to display the current answer board*

- **Input 6 to reset your answer board**

If you are stuck, you can reset the answer to re-think the solution

```
(Reseted answer board here)

Answer board has been reset!
```

- **Input -1 to quit**

Once you solved the puzzle or you want to quit the game, you can input -1 to quit the current game.

``` 
Please input your choice: -1

See you in another game!
```

#### Quit Program

Once you quit the sudoku game, it will ask you want to play the sudoku game again, and press -1 to quit

```
Press 1 to start play a sudoku game or -1 to quit: -1

Have a good day!
```



## Testing Hints

If you want to test the algorithm of the solution verification. You can simply input 5 to generate a solution first. And then test different results by placing numbers at different locations (Use Input 3 option). After that, input 4  to test the solution verification algorithm.

## Reference

1. https://www.makeareadme.com/
2. https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
3. https://gamedev.stackexchange.com/questions/56149/how-can-i-generate-sudoku-puzzles
4. https://leetcode.com/problems/sudoku-solver/
5. https://leetcode-cn.com/problems/sudoku-solver/solution/zi-cong-wo-xue-hui-liao-hui-su-suan-fa-zhong-yu-hu/
6. https://www.geeksforgeeks.org/backtracking-introduction/
7. https://stackoverflow.com/questions/28282717/display-2d-sudoku-board-in-python

&copy;  HL 2021/11/17
