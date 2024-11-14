from random import randint

def middle_of_list(original_list):
    if type(original_list) != list:
        print(f"Expected list argument, got {type(original_list)}")
        return

    # There cannot be any middle elements remaining in the list if the list has
    # two or less elements inside of it.
    if len(original_list) < 2:
        return original_list
    
    # We start at index 1 (the second element), and cut off the last element. Slicing list this
    # makes a copy of the original, and therefore, we would not modify the original list.
    return original_list[1 : len(original_list)-1]

def main():
    count_of_list = randint(1, 10)
    print(f"Your lucky number today is {count_of_list}!")

    num_list = list(range(1, count_of_list + 1))
    print("This is our original list:", num_list)
    new_num_list = middle_of_list(num_list)
    print("This is your new list of middle elements:", new_num_list)

# Call the main function...
main()