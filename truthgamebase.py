name = input('what is ur name? Lets play two truths and a lie!')
print('Hello', name + ', welcome to two truths and a lie!')

print('Just for FUN lets put your name in reverse!')
name = input ('First and last name to reverse -> ! ')
first, last  = name.split()
print(first[::-1], last[::-1]) 

counter = 3
while counter > 0:
    print("Counting down:", counter)
    counter -= 1

while counter > 0:
    print('Never executes suite')
    print('when condition is False')

while 1:
    print('Executes at least once')
    if not counter:
        break

names = ['Tom', 'Ellen']
while names:
    print(names.pop(), 'is going')

    results = [1, 0, 1]
processed = 0
passed = 0
while results:
    processed += 1
    result = results.pop()
    if not result:
                continue
    passed += 1


else:
    print('Processed:', processed, 'Passed:', passed)

for elem in range(5):
    print(elem, end=' ')
print()

for elem in range(1, 6):
    print(elem, end=' ')
print()

for elem in range(5, -1, -1):
    print('Countdown:', elem)

for char in 'string':
    print(char, end=' ')
print()

for tup in (1, 3, 5):
    print(tup)

for val in ['truth', 'lie', 'idk']:
    print(val)

age = 0
if age:
    print('False conditions do not execute')
    print('So, these statements won\'t print')

age = 1
if age:
    print('True conditions execute the')
    print('indented suite of code')

age = 19
if age >= 18:
    print('You are old enough to vote')
else:
    print('You are too young to vote')

score = 66
print('The grade was:', end=' ')
if score < 60:
    print('F')
elif 60 <= score < 70:
    print('D')
elif 70 <= score < 79:
        print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score <= 100:
    print('A')
else:    
    print('Impossible!')

debug = True
if debug: print('Score was:', score)

if score > 59:
    result = 'pass'
else:
     result = 'fail'
if debug: print('Result was:', result)

score = 40
if debug: print('Score was:', score)
result = 'pass' if score > 59 else 'fail'
if debug: print('Result was:', result) 
 
