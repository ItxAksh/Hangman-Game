import random
hangman_graphics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
words = ["game", "track", "player", "goal", "dynamic", "grip", "visual", "net",
    "camp", "coach", "fit", "prong", "drive", "team", "run",
    "pitch", "field", "gym", "swim", "vault", "jump", "bronze", "tackle",
    "route", "squad", "base", "sled", "curve", "joint", "swipe"]
hangman=''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''
def level(listt):
    print(''.join(listt))

print("Welcome to Hangman Game\n",hangman,'\n')
word=random.choice(words)
choices=list("_"*len(word))
print(''.join(choices))

print(f"Your word is a {len(word)} letter word")
guessed=False
lives=6

while lives!=0 and guessed==False:
    print()
    l=input("Enter letter: ")
    if len(l)==1:
        if l in word:
            print(f"Letter {l} was found in the word.")
            choices[word.index(l)] = l
            level(choices)
            if choices==list(word):
                guessed=True
                print("\nYou guessed the word.")
                print(f"It is '{word}'")
                print("You Won!")
        else:
            print(f"Letter '{l}' is not a part of the word.")
            print("Try again")
            lives-=1
            print(hangman_graphics[lives])
            if lives==0:
                print("\nGame Over!")
                print("You couldn't help the man.")
    else:
        print("Invalid Input.More than 1 input noticed")