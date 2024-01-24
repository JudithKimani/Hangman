secret_number = 7
count = 0
limit = 3
while count < limit:
    guess = int(input("Guess: "))
    count += 1
    if guess == secret_number:
        print("Win win!!!!")
        break
    else:
        print("you lose!!")
        
