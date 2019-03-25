#Write a program that prints the numbers from 1 to 16.
#But for multiples of three print “Fizz” instead of the number, 3,6,9,12,15
#and for the multiples of five print “Buzz”, 5,10,15
#For numbers which are multiples of both three and five print “FizzBuzz"

for num in range(1,16):
    string = "" 
    string = string + str(num)
    if num % 3 == 0:
        string = string + "-->Fizz"
    if num % 5 == 0:
        string = string + "-->Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
