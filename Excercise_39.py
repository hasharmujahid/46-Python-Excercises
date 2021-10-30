# Exercise 39 - Guess The Number
print("""

 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'
 aa,    ,88
  "Y8bbdP"  """

      )

print(
    """
 Developed by ::

  _   _   _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( H | a | s | h | a | r ) ( M | u | j | a | h | i | d )
 \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/
                                                                                                                                           
 """
)

low_point = 0
high_point = 1000
print("welcome to the guess the number game ... dev(Hashar Mujahid)")
print("PLZ thought of the number between 0 and 1000 but dont tell me! ")
guess_count = 0
while guess_count <= 10:
    guessed = low_point+(high_point-low_point)//2
    guessed_number = input(
        "my guess was {0}, should i guess higher (type h for that ),should i type lower (type l for that ), or am i right(type c for that ) ".format(guessed)).casefold()
    if guessed_number == 'h':
        low_point = guessed+1
    if guessed_number == 'l':
        high_point = guessed-1
    if guessed_number == 'c':
        print(' i got the answer in {0} guesses'.format(guess_count))
        break
    guess_count += 1
