def fizzbuzz():
    """Prints out every integer between x and y between 1 and 100

    Asks user input twice for two integers

    Loops and prints every integer from the first to the second integer
    'fizz' if also divisible by 3; 
    'buzz' if also divisible by 5;
    """
    # Check input
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        # Retry condition not between 1 - 100
        if x > 100 or y > 100 or x < 1 or y < 1:
            print("Error: Enter valid integers from 1-100")
            #fizzbuzz()
            return
    except: # Retry condition not integer
        print("Error: Enter valid integers from 1-100")
        #fizzbuzz()
        return

    # For reverse count 
    if x > y:
        y -= 2
        step = -1
    else:
        step = 1

    # Main loop
    for i in range(x, y+1, step):
        print(i)
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
    return
    


if __name__ == "__main__":
    fizzbuzz()
