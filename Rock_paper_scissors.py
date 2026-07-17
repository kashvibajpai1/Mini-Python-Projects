import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!\n")
user_input=input(print("Rock, paper, or scissors?\n"))

if user_input=="rock":
    print(rock)
elif user_input=="paper":
    print(paper)
elif user_input=="scissors":
    print(scissors)

print("Computer's Choice:\n")

choices=[rock, paper, scissors]
final_choice=random.choice(choices)
print(final_choice)

if user_input=="rock" and final_choice==paper:
    print("Computer Wins!")
elif user_input=="scissors" and final_choice==rock:
    print("Computer Wins!")
elif user_input=="paper" and final_choice==scissors:
    print("Computer Wins!")
elif user_input==str(final_choice):
    print("Its a draw!")
else:
    print("You win!")
