def guess_number():
    """Guess a number game
    
    Input the upper and lower limit of a range of numbers
    and lets the user guess the random number until correct.
    """
    import random
    
    lower_limit = int(input("Enter the smaller number of the range: "))
    upper_limit = int(input("Enter the larger number of the range: "))
    secret_number = random.randint(lower_limit, upper_limit)
    tries = 0

    while True:
        tries += 1
        user_number = int(input("Enter a number to try to guess: "))

        if user_number < secret_number:
            print("Try with a higher number.")
        elif user_number > secret_number:
            print("Try with a lower number.")
        else:
            print(f"You won! It took you {tries} tries")
            break


if __name__ == "__main__":
    guess_number()
