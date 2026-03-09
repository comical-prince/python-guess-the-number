import random as r 


point = 0 
round = 1
print("Score Rules:")
print("Correct guess: 5 to 1 points depending on attempts")
print("Fail to guess: -5 points")
print()
while True :
    print(f"=============Round {round}===============")
    num_to_guess = r.randint(1,100)
    attempt = 1
    guessed_correctly = False

    if num_to_guess <= 50:
        print("Number is between 1 and 50")
    else:
            print("Number is between 51 and 100")

    while attempt <= 5:
        try:
            guessed_num = int(input("Enter ur guess : "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if guessed_num < 1 or guessed_num > 100 :
            print("Invalid guess!!Enter a valid guess.")
            continue

        if guessed_num == num_to_guess:
            point += 6 - attempt
            print("Guessed correctly !!")
            #print(f"Total Score : {point}")
            guessed_correctly = True
            break 

        if guessed_num != num_to_guess:
            if guessed_num > num_to_guess:
                print("Too High")
            else:
                print("Too Low")

            print("HINT:")

            if attempt <= 2:
                lower = (num_to_guess // 10) * 10
                upper = min(lower + 9, 100)
            else:
                if guessed_num < num_to_guess:
                    lower = max(lower ,guessed_num)
                else:
                    upper = min(upper , guessed_num)

            print("LOWER:", lower, "UPPER:", upper)

            attempt += 1

    if not guessed_correctly:
        point -= 5
        print("❌ You failed to guess the number.")
        print(f"The correct number was: {num_to_guess}")
        print("Penalty: -5 points")

    print(f"Total Score: {point}")
    round += 1 
    play = input("Do u want to play again?(Y/N) : ").lower()
    if play != "y":
        print("Thanks for playing!!")
        break

    print("\n---------------------------\n")
        