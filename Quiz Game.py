def start_game():
    name = input("Enter you're name please")
    greet = print(f"Hello {name} welcome to the quiz game")
    points = 0
    playing = input("so you wanna play the game?")
    if playing.lower() != "yes":
        quit()
    else:
        print(
            "ok .Let's start the game. There are 5 Questions in this game for each correct  question you'll get 1 point")
    question_1 = input("Who created Python?")
    if question_1 == "gudio van rossum":
        points += 1
        print("Correct Answer Congratulations!" + f" You're current points are:{points} ")

    else:

        print("sorry incorrect answer ")
    #
    #         quit()
    question_2 = int(input('''How many bones are there in a human body
                           a) 205 , b) 209 c) 206 d) 321 '''))
    if question_2 == 206:
        points += 1
        print("Correct Answer Congratulations!" + f" You're current points are:{points} ")
    else:
        print("WRONG ANS ")
    #         print("Game Over!")
    question3 = input("CPU STANDS FOR?")
    if question3 == "central proccessing unit":
        points += 1
        print("Correct Answer Congratulations!" + f" You're current points are:{points} ")
    else:
        print("WRONG ANS ")
    #         print("Game Over!")
    question_4 = input(" Who invented Computer? ")
    if question_4 == "charles babbage":
        points += 1
        print("Correct Answer Congratulations!" + f" You're current points are:{points} ")
    else:
        print("WRONG ANS ")
    #         print("Game Over!")
    question_5 = input("  Fastest animal on earth is? ")
    if question_5 == "cheetah":
        points += 1
        print("Correct Answer Congratulations!" + f" You're current points are:{points} ")
    else:
        print("WRONG ANS ")
    #         quit()
    print(f"You're score is{points}  ")
start_game()










