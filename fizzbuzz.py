# Write a Python program that prints the numbers from 1 to 100.
# For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz" instead of the number.
# For multiples of both three and five, print "FizzBuzz" instead of the number.


list = ""

# Loop from 1 to 100
for number in range (1,101):
    # number is divided by 3 and 5
    if (number % 3 == 0) and (number % 5 == 0):
        print("\tFizzBuzz\n")
        list = list + "FizzBuzz "
    # number is divided by 3
    elif (number % 3 == 0):
        print("\tFizz\n")
        list = list + "Fizz "
    # number is divided by 3
    elif (number % 5 == 0):
        print("\tBuzz\n")
        list = list + "Buzz "
    else: 
        print("\t"+str(number)+"\n")
        list = list + str(number)+" "

print (list)
