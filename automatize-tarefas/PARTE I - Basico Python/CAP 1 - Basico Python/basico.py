# http://inventwithpython.com/blog/

print('Hello world!')
print('What´s your name?')
myName = input() # input() - espera o usuário digitar um texto no teclao e pressionar ENTER
print('Its good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

str(29) # '29'
print('I am ' + str(29) + ' years old.')

int('42') # 42 '	
int(1.25) # 1 
int(1.99) # 1 

float('3.14') # 3.14 
float(10) # 10