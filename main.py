import re

print(f'Calculator')
print(f'Type "quit" to exit\n')

previous = 0
run = True

def performMath():
    global run
    global previous

    equation = ''
    if previous == 0:
        equation = input('Enter equation:')
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print('Goodbye.')
        run == False
    else:
        equation = re.sub('[a-zA-Z,.:()""]', '', equation) #avtomatsko izločimo vse simbole, ki lahko privedejo do crasha

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print(f'You typed: {previous}')

while run:
    performMath()
