number = 19
attempted = int(input("Guess a number: "))
while number!= attempted:
     if attempted > number:
        print("Too HIgh, guess lower")
        attempted = int(input("Guess a number: "))

     elif attempted < number:
        print("Too Low,Try higher")
        attempted = int(input("Guess a number: "))
         
print("Correct guess")
  