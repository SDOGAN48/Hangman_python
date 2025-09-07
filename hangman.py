import random
word_list=["abuse","eroli","promt","funkv"]
images=['''OOOO''','''OOOX''','''OOXX''','''OXXX''','''XXXX''']
lifes=4
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder +="_"
print("Word to guess:" + placeholder)
game_over=False
correct_letter=[]
while not game_over:
    print(f"You have {lifes}/4 life left")
    guess=input("Guess a letter=").lower()
    if guess in correct_letter:
        print(f"You ve already guessed {guess}")
    display=""
    for letter in chosen_word:
        if letter==guess:
            display +=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display +=letter
        else:
            display +="_"
    print("Word to guess:" + display)
    if guess not in chosen_word:
        lifes -=1
        print(f"You guessed {guess},that's not in the word.You lose a life.")
        if lifes ==0:
            game_over=True
            print("You lose!!")
    if "_" not in display:
        game_over=True
        print("You win!!")
    print(images[lifes])

  