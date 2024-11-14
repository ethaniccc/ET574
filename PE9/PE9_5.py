from random import randint

def echo_message(msg, times_to_repeat):
    if type(msg) != str:
        print(f"message should be a string, got {type(msg)}")
        return
    if type(times_to_repeat) != int:
        print(f"times_to_repeat should be an integer, got {type(times_to_repeat)}")
        return

    for _ in range(0, times_to_repeat):
        print(msg)

def main():
    motto = input("Enter the motto for your company: ").title()
    times = randint(1, 10)
    
    print(f"Awesome! Let's chant that {times} times!")
    echo_message(motto, times)

main()