#def getFizzBuzz(multiples, *args):
#	for i in range(*args):
#		output = ''
#	for multiple in multiples:
#		if i%multiple==0:
#			output+=multiples[multiple]
#		if output=='':
#			output = i
#	print(output)
#multiples = {3: 'Fizz', 5:'Buzz'}
#getFizzBuzz(multiples, 1,101)

#Write a program that prints the numbers from 1 to 20.
#But for multiples of three print “Fizz” instead of the number
#and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz"
   
FizzBuzz = {'fizz': 1, 'buzz': 2, 'unknown': 3}

for key in FizzBuzz:
    if key == 'buzz':
        continue
    print(key, FizzBuzz[key])

for outer in range(2,6):
    for inner in range(1, outer):
        if not outer % inner:
            print(outer, '=', inner, '*', int(outer / inner))
            break
        else:
                print(outer, 'is fizz')
              


