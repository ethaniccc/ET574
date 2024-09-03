# Intro Examples
# using input() & print() function to display

course  = input("What is your favorite class?\n")
match course:
    case "Math":
        print("Math classes are OK....")
    case "English":
        print("I think I hate this class even more than I do Social Studies...")
    case "Social Studies":
        print("¡™£¢∞§¶ª•ºª•¡•™ª£¡¶£••¡º¡™£•¶ª•£§¶¡§ no.")
    case _:
        print("What type of class  is " + course + "?")