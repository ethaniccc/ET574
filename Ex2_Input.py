# Intro Examples
# using input() & print() function to display

def askThisGuyForHisFavoriteClass(times = 1):
    course  = input("What is your favorite class?\n")
    match course:
        case "Math":
            print("Math classes are OK....")
        case "English":
            print("I think I hate this class even more than I do Social Studies...")
        case "Social Studies":
            print("¡™£¢∞§¶ª•ºª•¡•™ª£¡¶£••¡º¡™£•¶ª•£§¶¡§ no.")
        case "i dunno":
            print("Just say something man I need rent from this survey :/")
        case "":
            if times == 3:
                print("Dude, you suck.")
                return

            print("Hello? I'd like a response..... please :(")
            askThisGuyForHisFavoriteClass(times + 1)
        case _:
            print("What type of class is " + course + "?")

askThisGuyForHisFavoriteClass()