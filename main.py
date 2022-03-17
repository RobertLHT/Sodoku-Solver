from Sudoku import sudoku

# This is the main function for running the program
def main():

    # Start asking user to start a game
    while True:

        # Check if user wants to play
        play = int(input("Press 1 to start play a sudoku game or -1 to quit: "))


        # Break if user wants to quit
        if play == -1: 
            print("\nHave a good day!")
            break

        if play != 1:
            print("Please input 1 or -1 to play or quit")
            continue

        # Initialize a game 
        game = sudoku()
        print("\nGame start!\n\n")

        game.display_puzzle()
        while True:

            # Print options to user
            print("\n-Input 1 to display the puzzle")
            print("-Input 2 to display the answer")
            print("-Input 3 to fill the puzzle")
            print("-Input 4 to check your answer")
            print("-Input 5 to generate an answer")
            print("-Input 6 to reset the answer")
            print("-Input -1 to quit\n")

            # Get user input
            choice = int(input("Please input your choice: "))
            print()

            # Display puzzle
            if choice == 1:
                game.display_puzzle()
            # Display answer
            elif choice == 2:
                game.display_answer()

            # Let user fill  the answer
            elif choice == 3:
                print("Start fill your answer")
                while True:

                    # Check row index, and whether user wants to stop fill the answer
                    row = int(input("\nRow index (1-9) or -1 to stop fill puzzle: "))
                    if row == -1:
                        break
                    col = int(input("Column index (1-9): "))
                    num = int(input("Input number: "))
                    print()

                    # Check the range of the row, column index and number
                    if row <1 or row>9:
                        print("Row index should be 1-9")
                    elif col<1 or col>9:
                        print("Column index should be 1-9")
                    elif num<1 or num >9:
                        print("Input num should be 1-9")
                    else:
                        game.modify_answer(row, col, num)
            # Check answer with the puzzle board
            elif choice == 4:

                # It the answer is valid, then print it to user
                if game.check_answer():
                    print("Solved, you got it.")

                    # Ask user if they want to quit or continue
                    quit = int(input("Press 1 to continue play or -1 to quit: "))
                    if quit == -1:
                        print("See you in another game!")
                        break
                else:
                    print("This is not a valid answer, please try again")
            # If user want to get the solution
            elif choice == 5:
                game.find_answer()

                # Check whether user want to continue to play or quit
                quit = int(input("\nPress 1 to continue play or -1 to quit: "))
                if quit == -1:
                    print("\nSee you in another game!\n")
                    break

            # If user wants to reset the answer board
            elif choice == 6:
                game.reset()
                game.display_answer()
                print("\nAnswer board has been reset!")
            # User wants to quit
            elif choice == -1:
                print("See you in another game!\n")
                break

            # Ask user to input an valid option
            else:
                print("Please input a valid choice\n")

# If this file is the main file, then run it 
if __name__ == "__main__":
    main()