def fizz_buzz(x):
    for i in range(1,x):
        if i % 5 == 0:
            print ('Buzz')
        elif x % 3 == 0:
            print ('Fizz')
        elif x % 5 == 0 and x % 3 == 0:
            print ('FizzBuzz')
        else:
            print (x)
        x += 1