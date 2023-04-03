num1 = 42 # variable declaration of a number

num2 = 2.3 # variable declaration of a number
boolean = True # a boolean value being true
string = 'Hello World'#  a string which is literal text
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#  a list of ingredients fot pizza toppings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#  a dictionary
fruit = ('blueberry', 'strawberry', 'banana')#  a list
print(type(fruit))#  print the type of data type of variable fruits
print(pizza_toppings[1])#  a dictionary
pizza_toppings.append('Mushrooms')#adds value
print(person['name'])#prints only the name inside the dictionary of our variable person
person['name'] = 'George'#change value
person['eye_color'] = 'blue'#change value
print(fruit[2])#prints index 2 inside of our variables fruits

if num1 > 45:#check if our number is greater than 45
    print("It's greater")#  if num1 is greater than 45 print this
else:
    print("It's lower")#  if num1 is less than 45 print this

if len(string) < 5: # gets the lenght of our string and checks to see if its lenght is less than 5
    print("It's a short word!")# if its less than 5 print this
elif len(string) > 15:# gets the lenght of our string and checks to see if its lenght is greater than 15
    print("It's a long word!")# if its greater than 15 print this
else:
    print("Just right!")#  if our string length isnt less than 5 or greater than 15 print this

for x in range(5):#will go from 0-5
    print(x)        #print will print 5 times staring from 0
for x in range(2,5):#will go from 2-5
    print(x)        #will print 3 times starting from 2
for x in range(2,10,3):#start at 2 stop at 10 count by 3
    print(x)#@will print from 2 to 10 counting by 3
x = 0 #variable declaration
while(x < 5): #while loop,while x is less than 5
    print(x) #print x until its less than 5
    x += 1  #add 1 to x

pizza_toppings.pop()#delete value
pizza_toppings.pop(1)#delete value at index 1

print(person) #prints our dictionary inside variable person
person.pop('eye_color')#AttributeError: 'tuple' object has no attribute 'pop'
print(person)   #prints our dictionary inside variable person

for topping in pizza_toppings:#for loop start
    if topping == 'Pepperoni':#conditional if toppings are pepperonis
        continue        #keep going inside the code block
    print('After 1st if statement')#if the first condition is true print this
    if topping == 'Olives':#conditional if toppings are olives
        break       #break the loop

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):#declaring our function and its parameters
    for num in range(x):#from var num given our parameter range meanign any number go from 0 to any given value to x
        print('Hello')#prints this string

print_hello_x_times(4)#prints hello 4 times

def print_hello_x_or_ten_times(x = 10):#function with a parameter as a variable with a value of 10
    for num in range(x): #loop for a number with the giiven value of x which is 10
        print('Hello')#princt hello

print_hello_x_or_ten_times()#calls the function so it will print hello 10 times
print_hello_x_or_ten_times(4)#reassing the value of x to 4 so it will print hello four times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)