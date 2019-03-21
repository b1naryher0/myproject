# Writing a collatz function
def collatz(number):
    if number % 2 == 0:          # Even
        print ( number // 2)
        return number // 2
    elif number % 2 == 1:        # Odd
        result =  3 * number + 1
        print (result)
        return result

try:
    n = int(input("Give me any integer: ")) # User Input
    while collatz() != 1:  # performs while loop until 'n' becomes 1
        n = collatz(int(n))        

except ValueError:
    print ("Value Error. Please enter an integer.")
