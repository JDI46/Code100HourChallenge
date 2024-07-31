import random

#create random number generater


#use a loop to iterate through guesses/ make sure the loop has the proper checks to stay within parameters


random_num = random.randint(1, 100)
count = 0

guess = int(input("Guess the number: "))
while guess != random_num:
  guess = int(input("Guess the number: "))
  if guess < random_num:
    print("Guess Higher")
  elif guess > random_num:
    print("Guess Lower")
  elif guess == random_num:
    break

print(f"The number is {random_num}")
