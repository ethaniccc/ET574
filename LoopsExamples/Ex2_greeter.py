# how to run the command line environment
# windows
# start -> run -> type cmd
# Mac
# applications -> utilities -> terminal


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
print()
#--------------------------------

number = input("Enter a number: ")
#int()	 returns an integer number
#print("number =", int(number))

#float() - returns a floating point number

#print("number =", float(number))

#eval() - evaluates and executes an expression
print("number =", eval(number))
