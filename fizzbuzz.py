import testcases

def fizzbuzz(x:int, y:int):
    '''
    Prints out every integer between x and y between 1 and 100;
    'fizz' if also divisible by 3; 
    'buzz' if also divisible by 5;
    '''

    #Requires number between 1-100
    try:
        x = max(1, int(x))
        y = min(100, int(y))
    except Exception as error:
        print('Error: ' + repr(error))
        return 1


    if x <= y:
        for i in range(x, y+1):
            #Within printline
            print(i, end = " ")
            if i % 3 == 0:
                print("fizz", end = "")
            if i % 5 == 0:
                print("buzz", end = "")
            print()
    else:
        fizzbuzz(y, x)
    return 0

if __name__ == "__main__":
    
    result = sum([
            fizzbuzz(1,100)
            fizzbuzz(10,1),
            fizzbuzz(0,1),
            fizzbuzz(-99,999),
            fizzbuzz(999,1000),
            fizzbuzz(-1000,-999),
            fizzbuzz("1","100"),
            fizzbuzz("a","b")]
        )
    print("Failed tests: ", result)
