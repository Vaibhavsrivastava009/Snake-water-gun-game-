import random

'''
# 1 for Snake 
# -1 for Water
# 0 for Gun
'''
def Snake_gun_water_game():
    print("Welcome to Snake, Gun, and Water Game!")
    youDict = {"s":1, "w":-1, "g":0}
    reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
    while True:
        computer = random.choice([1,0,-1])
        youstr = input("Enter your choice : from 's' for Snake, 'w' for Water, 'g' for Gun, 'q' for Quit: ").lower()
        if youstr in 'q':
            print("Thanks for playing!...")
            break
        if youstr not in youDict:
            print("Invalid choice. Please enter 's' for Snake, 'w' for Water, 'g' for Gun....")
            continue

        you = youDict[youstr]
        print(f"You entered {reverseDict[you]}\nComputer entered {reverseDict[computer]}...")

        if you == computer:
            print("It's a Tie.....Play again")
        else:
            if computer == -1 and you == 1:
                print("You Win!...Snake drinks water")
            elif computer == -1 and you == 0:
                print("Computer Wins!...Gun shoots water")
            elif computer == 1 and you == -1:
                print("Computer Wins!...Snake drinks water")
            elif computer == 1 and you == 0:
                print("You Wins!...Gun shoots snake")
            elif computer == 0 and you == -1:
                print("You Wins!...Water extinguishes gun")
            elif computer == 0 and you == 1:
                print("Computer Wins!...Gun shoots snake")
            else:
                print("Something Went Wrong......please try again...")

Snake_gun_water_game()
                

