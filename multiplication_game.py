import random

def check_answer(num1, num2, user_answer):
    correct_answer = num1 * num2
    return user_answer == correct_answer

def play_game():
    score = 0
    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        print(f"What is the product of {num1} and {num2} ? ")
        user_answer = int(input(f"What is {num1} x {num2}? "))
        
        if check_answer(num1, num2, user_answer):
            print("Correct! Well done.")
            score += 1
            print(f"Correct! Your score is {score}")
            play_again = input("Do you want to continue playing? (y/n): ")
            if play_again.lower() != "y":
                print("Thanks for playing!")
                break
        else:
            print(f"Sorry, the correct answer is {num1 * num2}.")
            print("Game over!")
            break

if __name__ == "__main__":
    print("Let's play a multiplication game!")
    print()
    play_game()
