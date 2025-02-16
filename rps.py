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
print("Welcome to the RPS Game !!")
name = input("Enter your name :")
user = int(input("What do you choose ? Type 0 for Rock , 1 for paper or 2 for scissor :"))#input returns a string
print(f"{name} chose")
if user == 0:
    print(rock)
if user == 1:
    print(paper)
if user == 2:
    print(scissors)
comp_choose = random.randint(0,2)
print(f"Computer chose")
if comp_choose == 0:
    print(rock)
if comp_choose == 1:
    print(paper)
if comp_choose == 2:
    print(scissors)

if comp_choose > user:
    print("Computer Wins!")
elif comp_choose == user:
    print("It's a draw")
else:
    print(f"{name} Wins!")
