import random

#Calculate the n-th term of fibonacci sequence
def fibonacci(term):
    x_n1 = 0
    x_n2 = 1
    series = 0
    for i in range(term):
        x_n1 = x_n2
        x_n2 = series
        series = x_n1 + x_n2

    return series


#Variable b will determine if fib_series is prime (1) or not prime (0)
b=1

term = int(input("Please give a term from the Fibonacci sequence: "))

fib_serie=(fibonacci(term)) #Call fibonacci function and store the result

#Check 20 times if fib_series is prime
for i in range(20):
    rand_num=random.randint(1,fib_serie) #Choose a random number n where  1 < n < fib_series

    #Do calculations
    p1=(rand_num ** fib_serie) % fib_serie
    p2=rand_num % fib_serie

    if p1 == p2:
        b *=1 #Is prime
    else:
        b *=0 #Is not prime


if b==1:
    print("The term " + str(term) +" of fibonacci sequence is number " + str(fib_serie) + " and is prime!")
else:
    print("The term " + str(term) +" of fibonacci sequence is number " + str(fib_serie) + " and is not prime!")
    

