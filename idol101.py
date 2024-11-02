#Projet : Text-Based game
# Nom du projet: IDOL 101

def appuie_pour_continuer():
    '''
    Cette fonction améliore la visibilité et la compréhension du jeu. Elle permet au joueur de finir sa lecture avant de continuer.
    '''
    try:
         input("\nPress enter to continue. ")
    except SyntaxError:
         pass

# Introduction du jeu et du concept
def intro():
    print("\nWelcome to Idol 101!")
    print("In this game, you’ll go through the hardships of becoming a kpop idol.")
    print("You are a high school student in South Korea at Hamlin Art School.")
    print("You’ve always dreamed about becoming a kpop Idol.")
    print("Let's start choosing with your stage name!")
    name = input("What's your stage name : ")
    appuie_pour_continuer()
    print("\nYou will have to choose between dancer, singer and rapper. Better choose wisely...")
    print(f"{name}, will you succeed debuting? We wish you the best luck in your quest of becoming the next global star!")
    choice = input("Which position do you want to choose: ")
    return (choice, name)


#Définition de la storyline en tant que dancer
def dancerpath(name):
    print(f"\n{name}, you have chosen the dancer path!")
    print("You auditioned for your school dance team.")
    print("You were picked!")
    appuie_pour_continuer()
    print("\nNow you have to choose your entertainment label.")
    print("You have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ? ").lower()

    if company_choice == "a":
        print(f"\n{name}, you were chosen by Hybe.")
        print("Hybe Entertainment is known for innovation, artist-driven content, and global reach.")
        print("They were impressed by your language skills and your drive.")
        print("You've started training under the company, known for intense, structured training programs.")
        appuie_pour_continuer()
        training_choice = input("\nDo you want to focus on (1) becoming popular or (2) improving your dance skills?")

        if training_choice == "1":
            print("\nYou've gained a lot of fans, but your dancing skills are not up to par with your popularity :/")
            return "Successful Debut" #Amène à une fin spécifique!
        elif training_choice == "2":
            print("\nYou were praised for your dancing skills, and everyone looks up to you!")
            return "Global Sensation" #Amène à une fin plus impressionante
    
    elif company_choice == "b":
        print(f"\n{name}, you were recruited by JYP!")
        print("JYP is known for its emphasis on personality, teamwork, and “JYP Style” of training.")
        print("They loved how you thrive among others!")
        appuie_pour_continuer()
        setback_choice = input("\nOh no! You've been involved in a huge scandal that threatens your reputation. Do you wish to (1) ignore the scandal and lay low or (2) face it head-on?: ")

        if setback_choice == "1":
            print("\nYou've stayed out of the spotlight and managed to make it, gaining a small but loyal fandom.")
            return "Underground Star"
        elif setback_choice == "2":
            print("\nYou addressed the rumor. It turns out it was a false accusation...")
            print("You've made headline and everyone sympathizes with you.")
            print("You've gained a lot of attention and everyone loves you now!")
            return "Successful Debut"

    elif company_choice == "c":
        print(f"\n{name}, you've joined SM, where visuals and talent are prized above all.")
        print("They were impressed by your amazing visuals!")
        appuie_pour_continuer()
        perseverance_choice = input("\nDo you wish to (1) stick with your members or (2) try to break it solo? ")

        if perseverance_choice == "1":
            print("\nYour teamwork paid off. You've debuted in a popular and solid K-pop group!")
            return "Successful Debut"
        elif perseverance_choice == "2":
            print("\nYou decided to go solo. You've barely made it, but you have a small community supporting you.")
            return "Underground Star"
    
    else:
        print("\nThis is not an option. Please choose betwee a, b or c.")
        dancerpath()

#Défintion de la storyline de singer
def singerpath(name):
    print(f"\n{name}, you have chosen the singer path!")
    print("You performed at your school festival!")
    print("Your classmates brag about your amazing vocal skills.")
    print("Due to your popular reputation, many companies recruited you.")
    appuie_pour_continuer()
    print("\nYou have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ?").lower()

    if company_choice == "a":
        print(f"\n{name}, you were recruited by Hybe.")
        print("They liked your drive and your leadership!")
        print("They decided to make you a part of their new debut team.")
        appuie_pour_continuer()
        print("\nWhile promoting the new group, someone discovered something dark from your past.")
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
        print(f"\n{name}, you were recruited by JYP!")
        print("You trained a year and half with them before they realized you were an ace.")
        print("The entertainment compagny made you a part of an already made debut group! ")
        appuie_pour_continuer()
        second_skill_choice = input("\nIn order to become the K-pop \"It\" Idol, you need to take on another skill, do you want to work on (1) your dancing skill or (2) your rapping skill?: ")
        
        if second_skill_choice == "1":
            print("\nEveryone is impressed, not everyone can excel in both singing and dancing!")
            print("You've experienced some tensions from your group members, they're jealous of your sucess.")
            print("However, you managed to resolve every conflits.")
            print("You dit it!")

            return "Global Sensation"
        
        elif second_skill_choice == "2":
            print("\nYou received tons of hate. They claim you are appropriating black culture.")
            print("You tried to explain yourself, but it was unconclusive...")
            appuie_pour_continuer()
            redemption_choice = input("\nDo you wish to (1) host a media statement or (2) collab with a western artist to show your intentions?: ")

            if redemption_choice == "1":
                print("\nThey made fun of you!")
                print("Memes of you are all over the Internet.")
                return "Underground Star"
            
            elif redemption_choice == "2":
                print("\nIt worked!")
                print("They feel bad for you. Now, they understand your love for it.")
                return "Global Sensation"
    
    elif company_choice == "c":
        print(f"\n{name}, you were recruited by SM!")
        print("You have trained with SM for 6 long years.")
        print("They created with an amazing debut group and you are on it!")
        print("After all of your blood, sweat and tears, you finally get to debut.")
        appuie_pour_continuer()
        print("\nPeople praise your amazing visuals, and many wonder how someone can look so perfect.")
        print("They dove into your past,found old pictures of you and noticied you went under the knife!")
        print("Your reputation took a hit.")
        appuie_pour_continuer()
        visual_choice = input("\nDo you want to (1) start on campain on how to love yourself or (2) share a crying video of you on the web?: ")
        
        if visual_choice == "1":
            print("\nYou did it. You addressed the toxic and complicated relationship the industry has with visuals. You changed the idol industry.")
            return "Global Sensation"
        elif visual_choice == "2":
            print("\nYou realized that you don't want to keep working in this toxic environment and decided to quit.")
            return "Side Role"
    else:
        print("\nThis is not an option. Please choose betwee a, b or c.")
        singerpath(name)

#Définition de la storyline en tant que rapper
def rapperpath(name):
    print(f"\n{name}, you have chosen the rapper path!")
    print("You are a popular underground rapper in Seoul.")
    print("Many people stream your songs on SoundCloud.")
    print("A popular celebrity posted one of your songs in his Instagram story.")
    print("Entertainment compagnies go through hell and back to recruite you.")
    appuie_pour_continuer()
    print("\nYou have the choice between : a = Hybe, b = JYP and c = SM ")
    company_choice = input("Will you choose between a, b or c ?: ").lower()


    if company_choice == "a":
        print(f"\n{name}, you were recruited by Hybe!")
        print("During one of the montly evaluations, you had to make your own song.")
        print("You made it before, so it's no problem for you.")
        print("Except... other trainees mocked you for making up fake opps (slang for rivals).")
        appuie_pour_continuer()
        opps_choice = input("Do you want to (1) create a diss track about them or (2) ignore them? : ")

        if opps_choice == "1":
            print("\nYou released the track and went viral!")
            print("You become part of a hip-hop-oriented group and become famous.")
            return "Global sensation"
        
        elif opps_choice == "2":
            print("\nYou couldn't take the humiliation and quit!")
            print("You still have nightmares about that day.")
            return "Side Role"
    
    elif company_choice == "b":
        print(f"\n{name}, you were recruited by JYP!")
        print("They fell in love with your creativity.")
        print("The company wants you to help produce songs of your new debut team.")
        print("You debuted as the leader of the new group.")
        print("Someone noticied an uncanny similarity with a famous rap song.")
        appuie_pour_continuer()
        plagiat_choice = input("\nDo you wish to (1) admit that you sampled the song or (2) claim that it all came from you?: ")

        if plagiat_choice == "1":
            print("\nMany came to your defense, as sampling is a common practice in the industry.")
            print("Fans love you and your group!")
            appuie_pour_continuer()
            print("\nHowever, you prefer producing song over performing them.")
            print("You become a famous producer, making songs for BTS, Blackpink, Seventeen, and many more!")
            return "Side Role"
        
        elif plagiat_choice == "2":
            print("\nYou were exposed!")
            print("People criticize you for lying when you could've come clean.")
            return "Quiet Retirement"


    elif company_choice == "c":
        print(f"\n{name}, you were recruited by SM!")
        print("You have trained with SM for 7 long years.")
        print("You finally debuted in a team when something happened.")
        print("You were making beats in your studio when an artist released a diss track about you.")
        print("He wants to start a beef (slang for feud).")
        print("You need to make your move now!")
        appuie_pour_continuer()
        retaliation_choice = input("\nDo you want to (1) respond to the attack with peace and love or (2) drop your own diss track? : ")

        if retaliation_choice == "1":
            print("\nPeople are calling you soft and weak.")
            print("They say you're not what the hip-hop industry stands for.")
            return "Underground Star"
        
        elif retaliation_choice == "2":
            print("\nAll eyes are on you and the other artist.")
            print("They find your beef super entertaining.")
            print("Your rivalry went down in history, and you became even more famous than before.")
            return "Global Sensation"
    else:
        print("\nThis is not an option. Please choose betwee a, b or c.")
        rapperpath(name)

def display_ending(ending):
    if ending == "Successful Debut":
        appuie_pour_continuer()
        print("\nCongratulations! You've successfully debuted as a part of a popular group. Fame and fortune are within your reach!")
    elif ending == "Global Sensation":
        appuie_pour_continuer()
        print("\nYou've become an international superstar, leading the wave of K-pop around the world!")
    elif ending == "Underground Star":
        appuie_pour_continuer()
        print("\nThough you didn’t debut in a major group, you've become a beloved solo artist in the underground scene.")
    elif ending == "Quiet Retirement":
        appuie_pour_continuer()
        print("\nThe idol life was tough, and you decided to pursue a simpler life outside of the industry.")
    elif ending == "Side Role":
        appuie_pour_continuer()
        print("\nAlthough you didn’t debut as an idol, you found success as a choreographer and a coach.")
    else:
        appuie_pour_continuer()
        print("\nYour journey has ended in an unexpected way. Keep pushing forward!")

#Définition du jeu principal
def main():
    while True:
        def start_game():
            choice, name = intro()

            if choice == "dancer":
                ending = dancerpath(name)
                display_ending(ending)

            elif choice == "singer":
                ending = singerpath(name)
                display_ending(ending)

            elif  choice == "rapper":
                ending = rapperpath(name)
                display_ending(ending)

            else :
                print("This is not an option. Please choose betwee dancer, rapper or singer.")
                start_game() #Voir si on peut commencer au choix du skill au lieu du début!
        #Début de la partie
        start_game()
        #Propose une autre partie
        play_again = input("\nDo you want to play again? (yes/no): " ).lower()

        #Arrête la boucle si le joeur opte pour "no"
        if play_again != "yes":
            print("Thanks for playing! See you again!")
            break

if __name__ == "__main__":
    main()
