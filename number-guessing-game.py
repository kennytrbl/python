import random
def main():
    guess = 0
    number = random.randint(1,100)
    while guess != number:
        try:
            guess = int(input("Guess the number from 1 to 100: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Correct!")
            break

if __name__ == "__main__":   
    main()