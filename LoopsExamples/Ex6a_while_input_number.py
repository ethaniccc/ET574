## Using input() & while loop

n = int(input("Enter a number: "))  #1. get n
i = 1;                              #2. initialize i to 1
while i <= n :                      #3. check condition
  print(i)                          #4. repeat action
  i = i + 1;                        #5. update i
print(f"current_number = {i}")
