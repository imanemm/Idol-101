#Project 2 : Text-Based game
#Début : 19 Septembre 2024
# Introduction du jeu et du concept
def intro():
    print("Welcome to Idol 101!")
    print("In this game, you’ll go through the hardships of becoming a kpop idol.")
    print("You are a high school student in South Korea at Hamlin Art School.")
    print("You’ve always dreamed about becoming a kpop Idol.")
    print("Let's start choosing with your stage name!")
    name = input("What's your stage name :")
    print("You will have to choose between dancer, singer and rapper. Better choose wisely...")
    print(f"{name}, will you succeed debuting? We wish you the best luck in your quest of becoming the next global star!")
    choice = input("Which position do you want to choose: ")
    return choice

#Définition de la storyline en tant que dancer
def dancerpath():
    print("\nYou have chosen the dancer path.")
    print("You auditioned for your school dance team.")
    print("You were picked!\n")
    print("Many people know you for your dance skills and you were recruited by many compagnies.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    choice = input("Will you choose between a, b or c ?")
    print()

    if choice == "a":
        print("You were recruited by Hybe and you trained for 6 months.")
        print("They were impressed by your passion!")
        print("They decided to make you a part of the new debut team.")
        print("You finally debuted after 3 years of training but you are not the most popular member...\n")
        print("Congrats! You win!")
    
    elif choice == "b":
        print("You were recruited by JYP!")
        print("You trained 7 months with them before they realized your lack vocal abilities...")
        print("You were kicked out of JYP :( \n")
        print("Game over...")

    elif choice == "c":
        print("You were recruited by SM!")
        print("You have trained with SM for 7 long years.")
        print("They kept you in the SM basement with many other trainees...")
        print("You decided to take the matter into your own hands and joined a survival show.")
        print("Unfortunatly, you were not popular enough to debut with the group.\n")
        print("Game over...")
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        dancerpath()

#Défintion de la storyline de singer
def singerpath():
    print('\n',"You have chosen the singer path.")
    print("You performed at your school festival!")
    print("Your classmates brag about your amazing vocal skills.\n")
    print("Due to your popular reputation, many compagnies recruited you.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    choice = input("Will you choose between a, b or c ?")
    print()

    if choice == "a":
        print("You were recruited by Hybe and you trained for 11 months.")
        print("They liked your drive and your leadership!")
        print("They decided to make you a part of the new debut team.")
        print("Unfortunatly, you get caught up in a huge scandal...")
        print("Hybe decided to kick you out of the compagny!")
        print("You are no longer wanted by any compagnies.\n")
        print("Game over...")
    
    elif choice == "b":
        print("You were recruited by JYP!")
        print("You trained a year and half with them before they realized you were an ace.")
        print("The entertainment compagny made you a part of an already made debut group! ")
        print("You do not get along with your members at all. They are jaleous of your sucess.")
        print("They made up dating rumors about you...")
        print("Fans are disapointed in you and made you quit!\n")
        print("Game over...")

    elif choice == "c":
        print("You were recruited by SM!")
        print("You have trained with SM for 2 long years.")
        print("They created with an amazing debut group and you are on it!")
        print("After all of your blood, sweat and tears, you finally get to debut.")
        print("People are amazed by your extraordinary visuals.")
        print("You are the most popular member of the group!\n")
        print("Wow, you won!")
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        singerpath()

#Définition de la storyline en tant que rapper
def rapperpath():
    print("\nYou have chosen the rapper path.")
    print("You are a popular underground rapper in Seoul.")
    print("Many people stream your songs on SoundCloud.")
    print("A popular celebrity posted one of your songs in his Instagram story.\n")
    print("Entertainment compagnies go through hell and back to recruite you.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    choice = input("Will you choose between a, b or c ?")
    print()

    if choice == "a":
        print("You were recruited by Hybe and you trained for 2 months.")
        print("During one of the montly evaluations, you had to make your own song.")
        print("You made it before so it is no problem for you.")
        print("Except... Other trainees mocked you for making up fake opps.")
        print("You couldn't take the humiliation and quit!\n")
        print("Game Over...")
    
    elif choice == "b":
        print("You were recruited by JYP!")
        print("They fell in love with your creativity")
        print("The compagny wants you to help produce the songs of your new debut team.")
        print("You've met another trainee just like you.")
        print("That trainee became your best friend!")
        print("You finally debuted as the leader of a new group!\n")
        print("Fans love you and your group!")
        print("You win the game!")

    elif choice == "c":
        print("You were recruited by SM!")
        print("You have trained with SM for 2 long years.")
        print("You were making beats in the studio when one of your songs leaked.")
        print("They realised that you plageried the popular artist who help you get recruited...")
        print("Unfortunatly, people were mad and the artist sued you.\n")
        print("Game over...")
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        rapperpath()

#Définition du jeu principal
def start_game():
    choix = intro()

    if choix == "dancer":
        dancerpath()

    elif choix == "singer":
        singerpath()

    elif  choix == "rapper":
        rapperpath()

    else :
        print("This is not an option. Please choose betwee dancer, singer or rapper.")
        start_game()

start_game()
