import random


print("")
print("---------------------------------------------------------------------")
print("-------------------GUESS----THE----SECRET---CODE!--------------------")
print("---------------------------------------------------------------------")
print("")
print("---------------------------------------------------------------------")
print("---------------------------G---A---M---E-----------------------------")
print("-------------------------R---U---L---E---S---------------------------")
print("---------------------------------------------------------------------")
print("")
print("Welcome to Guess the Secret Code Game! " + "There are 3 levels of " +
      "difficulty: 1. easy(3 digits) 2. median(5 digits) 3. difficult" +
      "(7 digits). You can choose levels of difficulty by entering " +
      "1 or 2 or 3. During the game, you will see numbers of A and B. " +
      "A: # of right number in the right position, B: # of right number " +
      "but in wrong position. Numbers of AB are not overlapped. eg. when " +
      "guessing a 3 digit number, 3A0B that means you win the game. " +
      "Note: the first digit could be zero.")
print ("")
print ("--------------------------------------------------------------------")
print ("---------------------GAME---------------START!----------------------")
print ("--------------------------------------------------------------------")
print ("")
print ("Okay, Give yourself a name: ")


def level():
    level = input("choose a level: 1(easy), 2(median), 3(difficult): ")
    # Choose a level of difficulty.
    if level == '1':
        digit = 3
    elif level == '2':
        digit = 5
    elif level == '3':
        digit = 7
    else:
        print("Sorry, You did not enter 1, 2 or 3. The game level will set " +
              "to 1.")
        # If player entered any characters other than 1,2,3,
        # eg. abc, a space, float
        # numbers of digit would be automatically 3.
        digit = 3
    return digit


def main():
    chances = 10   # 10 total chances.
    while chances:
        print("this is a", digit, "digit code, you still have", chances,
              "chances.")
        print("Enter your number without space: ")

        choice = input()   # Enter the number you guessed.
        try:   # The "try" "except ValueError" code were from stackoverflow.
            i = int(choice)
            # The input must be an integer.
            if i in secret:
                return choice
        except ValueError:    # If it is not an integer, the game will end.
            print(":( Sorry, You have to type in a number")
            break

        if len(choice) != len(secret):
            # Need to enter 3/5/7 digit code
            print("Sorry, You have to enter a ", digit, "digit code. ")
            # If a longer or a shorter code is entered, the game will end.
            break

        chances -= 1
        A = 0
        B = 0
        for i in range(len(secret)):
            if str(choice[i]) == str(secret[i]):
                # if the number matches the secret number in same position.
                A += 1
            elif int(choice[i]) in secret:
                # if the number are in the secret number.
                B += 1

        common = "{}A{}B".format(A, B)
        print(common)
        if common == "{}A{}B".format(digit, 0):
            print("Congratulations! You win :) and You used",
                  10-chances, "chances.")  # 10 - chances left = chances used
            print("The secret code is: ", secret)
            break

        elif chances == 0:
            print("Sorry you ran out of chances and you lose the game:(")
            print("The secret code is: ", secret)


user_name = input()
digit = level()
secret = random.sample(range(10), digit)
# print(secret)
print('Hi, {}, You need to guess a {} digit code.'.format(user_name, digit))
main()

# The code here was from github gist.
print("Do you want to play again? y/n")
playagain = input()
while playagain == "y":
    digit = level()
    secret = random.sample(range(10), digit)
    main()
