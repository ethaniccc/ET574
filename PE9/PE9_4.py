def hello():
    print("Hello world!")

def hello_no(n):
    # Check if n is not an integer. If it is not, then we don't want to execute further.
    type_of_n = type(n)
    if type_of_n != int:
        print(f"expected argument \"n\" to be integer, got {type_of_n} ({n})")
        return

    # Call hello() for the given amount of times. We could also use a 
    # WHILE loop for this.
    for _ in range(0, n):
        hello()

hello_no(3)
hello_no("some_random_string")
hello_no(3.0)
