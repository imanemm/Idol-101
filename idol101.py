#Projet : Text-Based game
# Nom du projet: IDOL 101

def appuie_pour_continuer():
    '''
    Cette fonction améliore la visibilité et la compréhension du jeu. Elle permet au joueur de finir sa lecture avant de continuer.
    '''
    try:
         input("\nAppuyez Enter pour continuer. ")
    except SyntaxError:
         pass

# Introduction du jeu et du concept
def intro():
    print("Welcome to Idol 101!")
    print("In this game, you’ll go through the hardships of becoming a kpop idol.")
    print("You are a high school student in South Korea at Hamlin Art School.")
    print("You’ve always dreamed about becoming a kpop Idol.")
    print("Let's start choosing with your stage name!")
    name = input("What's your stage name :")
    appuie_pour_continuer()
    print("You will have to choose between dancer, singer and rapper. Better choose wisely...")
    print(f"{name}, will you succeed debuting? We wish you the best luck in your quest of becoming the next global star!")
    choice = input("Which position do you want to choose: ").lower
    return choice


#Définition de la storyline en tant que dancer
def dancerpath():
    print("You have chosen the dancer path!")
    print("You auditioned for your school dance team.")
    print("You were picked!")
    appuie_pour_continuer()
    print("Now you have to choose your entertainment label.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ?").lower()

    if company_choice == "a":
        print("You were chosen by Hybe.")
        print("Hybe Entertainment is known for innovation, artist-driven content, and global reach.")
        print("They were impressed by your language skills and your drive.")
        print("You've started training under the company, known for intense, structured training programs.")
        appuie_pour_continuer()
        training_choice = input("Do you want to focus on (1) becoming popular or (2) improving your dance skills?")

        if training_choice == "1":
            print("\nYou've gained a lot of fans, but your dancing skills are not up to par with your popularity :/")
            return "Successful Debut" #Amène à une fin spécifique!
        elif training_choice == "2":
            print("\nYou were praised for your dancing skills, and everyone looks up to you!")
            return "Global Sensation" #Amène à une fin plus impressionante
    
    elif company_choice == "b":
        print("You were recruited by JYP!")
        print("JYP is known for its emphasis on personality, teamwork, and “JYP Style” of training.")
        print("They loved how you thrive among others!")
        appuie_pour_continuer()
        setback_choice = input("Oh no! You've been involved in a huge scandal that threatens your reputation. Do you wish to (1) ignore the scandal and lay low or (2) face it head-on?: ")

        if setback_choice == "1":
            print("\nYou've stayed out of the spotlight and managed to make it, gaining a small but loyal fandom.")
            return "Underground Star"
        elif setback_choice == "2":
            print("\nYou addressed the rumor. It turns out it was a false accusation...")
            print("You've made headline and everyone sympathizes with you.")
            print("You've gained a lot of attention and everyone loves you now!")
            return "Successful Debut"

    elif company_choice == "c":
        print("You've joined SM, where visuals and talent are prized above all.")
        print("They were impressed by your amazing visuals!")
        appuie_pour_continuer()
        perseverance_choice = input("Do you wish to (1) stick with your members or (2) try to break it solo? ")

        if perseverance_choice == "1":
            print("\nYour teamwork paid off. You've debuted in a popular and solid K-pop group!")
            return "Successful Debut"
        elif perseverance_choice == "2":
            print("\nYou decided to go solo. You've barely made it, but you have a small community supporting you.")
            return "Underground Star"
    
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        dancerpath()

#Défintion de la storyline de singer
def singerpath():
    print("You have chosen the singer path!")
    print("You performed at your school festival!")
    print("Your classmates brag about your amazing vocal skills.")
    print("Due to your popular reputation, many companies recruited you.")
    appuie_pour_continuer()
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ?").lower()

    if company_choice == "a":
        print("\nYou were recruited by Hybe.")
        print("They liked your drive and your leadership!")
        print("They decided to make you a part of their new debut team.")
        appuie_pour_continuer()
        print("While promoting the new group, someone discovered something dark from your past.")
        print("Your history as a high school bully is threatens your position as a debut member.")
        scandalous_choice = input("\nDo you want to (1) cover it up or (2) admit to your mistakes and apologize?")

        if scandalous_choice == "1":
            print("\nIt all blew up in your face, and all of your fans are furious!")
            print("Hybe decided to kick you out of the company!")
            return "Quiet Retirement"
        
        elif scandalous_choice == "2":
            print("\nEven if you admitted your mistakes, not everyone forgave you.")
            print("After some time, people moved on, and you succeded in debuting.")
            return "Underground Star"

    
    elif company_choice == "b":
        print("\nYou were recruited by JYP!")
        print("You trained a year and half with them before they realized you were an ace.")
        print("The entertainment compagny made you a part of an already made debut group! ")
        appuie_pour_continuer()
        second_skill_choice = input("\nIn order to become the K-pop \"It\ Idol, you need to take on another skill, do you want to work on (1) your dancing skill or (2) your rapping skill?: ")
        
        if second_skill_choice == "1":
            print("\nEveryone is impressed, not even can excel in both singing and dancing!")
            print("You've experienced some tensions from your group members, they're jalous of your sucess.")
            print("However, you managed to resolve every conflits.")
            print("You dit it!")
            return "Global Sensation"
        
        elif second_skill_choice == "2":
            print("\nYou received tons of hate. They claim you are appropriating black culture.")
            print("You tried to explain yourself, but it was unconclusive...")
            appuie_pour_continuer()
            redemption_choice = input("Do you wish to (1) host a media statement or (2) collab with a western artist to show your intentions?: ")

            if redemption_choice == "1":
                print("\nThey made fun of you!")
                print("Memes of you are all over the Internet.")
                return "Underground Star"
            
            elif redemption_choice == "2":
                print("\nIt worked!")
                print("They feel bad for you. Now, they understand your love for it.")
                return "Global Sensation"
    
    elif company_choice == "c":
        print("\nYou were recruited by SM!")
        print("You have trained with SM for 6 long years.")
        print("They created with an amazing debut group and you are on it!")
        print("After all of your blood, sweat and tears, you finally get to debut.")
        appuie_pour_continuer()
        print("\nPeople praise your amazing visuals, and many wonder how someone can look so perfect.")
        print("They dove into your past,found old pictures of you and noticied you went under the knife!")
        print("Your reputation took a hit.")
        appuie_pour_continuer()
        visual_choice = input("Do you want to (1) start on campain on how to love yourself or (2) share a crying video of you on the web?: ")
        
        if visual_choice == "1":
            print("")
            return "Global Sensation"
        elif visual_choice == "2":
            print("")
            return "Side Role"
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        singerpath()

#Définition de la storyline en tant que rapper
def rapperpath():
    print("You have chosen the rapper path!")
    print("You are a popular underground rapper in Seoul.")
    print("Many people stream your songs on SoundCloud.")
    print("A popular celebrity posted one of your songs in his Instagram story.")
    print("Entertainment compagnies go through hell and back to recruite you.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ?").lower()


    if company_choice == "a":
        print("You were recruited by Hybe and you trained for 2 months.")
        print("During one of the montly evaluations, you had to make your own song.")
        print("You made it before so it is no problem for you.")
        print("Except... Other trainees mocked you for making up fake opps.")
        print("You couldn't take the humiliation and quit!")
        print("Game Over...")
    
    elif company_choice == "b":
        print("You were recruited by JYP!")
        print("They fell in love with your creativity")
        print("The compagny wants you to help produce the songs of your new debut team.")
        print("You've met another trainee just like you.")
        print("That trainee became your best friend!")
        print("You finally debuted as the leader of a new group!")
        print("Fans love you and your group!")
        print("You win the game!")

    elif company_choice == "c":
        print("You were recruited by SM!")
        print("You have trained with SM for 2 long years.")
        print("You were making beats in the studio when one of your songs leaked.")
        print("They realised that you plageried the popular artist who help you get recruited...")
        print("Unfortunatly, people were mad and the artist sued you.")
        print("Game over...")
    else:
        print("This is not an option. Please choose betwee a, b or c.")
        rapperpath()

def display_ending(ending):
    if ending == "Successful Debut":
        print("\nCongratulations! You've successfully debuted as a part of a popular group. Fame and fortune are within your reach!")
    elif ending == "Global Sensation":
        print("\nYou've become an international superstar, leading the wave of K-pop around the world!")
    elif ending == "Underground Star":
        print("\nThough you didn’t debut in a major group, you've become a beloved solo artist in the underground scene.")
    elif ending == "Quiet Retirement":
        print("\nThe idol life was tough, and you decided to pursue a simpler life outside of the industry.")
    elif ending == "Side Role":
        print("\nAlthough you didn’t debut as an idol, you found success as a choreographer and a coach.")
    else:
        print("\nYour journey has ended in an unexpected way. Keep pushing forward!")

#Définition du jeu principal
def main():
    while True:
        def start_game():
            choice = intro()

            if choice == "dancer":
                dancerpath()

            elif choice == "singer":
                singerpath()

            elif  choice == "rapper":
                rapperpath()

            else :
                print("This is not an option. Please choose betwee a, b or c.")
                start_game()
        #Début de la partie
        start_game()
        display_ending(ending)
        #Propose une autre partie
        play_again = input("Do you want to play again? (yes/no): " ).lower()

        #Arrête la boucle si le joeur opte pour "no"
        if play_again != "yes":
            print("Thanks for playing! See you again!")
            break

if __name__ == "__main__":
    main()