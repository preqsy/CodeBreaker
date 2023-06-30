import random

def get_guess():
    return list(input("What's your guess? \n"))


def get_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
    

def create_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED"
    
    clues = []
    
    for index, num in enumerate(user_guess):
        
        
        if num == code[index]:
            clues.append("Match")
        elif num in code:
            clues.append('Close')
            
            
    if clues == []:
        return ["Nope"]
    
    
    return clues
# print(get_guess())

print("Are you ready to crack the code 🤓😑🔒!!!!!!!!!")


secret_code = get_code()
clue_check = []


while clue_check != "CODE CRACKED":
    guess = get_guess()
    clue_check = create_clues(secret_code, guess)
    
    print("Here is your guess: ")
    for clue in clue_check:
        print(clue)