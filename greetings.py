print('----- PART 1 -----')
input_name = input('What is your name? ')
print(f'Your name is: {input_name}')

print('----- PART 2 -----')
input_name = input('What is your name? ')
if input_name == 'Joe':
    print("Hey that's my name too!")
else: print(f'Your name is: {input_name}')

print('----- PART 3 -----')
x = list()
for y in range(11):
    input_name = input('What is your name? ')
    x.append(input_name)
    if len(x) == 10:
        break
print(f"Names are: {x}")
print('It was nice to meet all of you')


print('----- PART 4 -----')
v = list()
for z in range(99):
    input_name = input('What is your name? ')
    if input_name in v:
        print('name is already given')
    else: v.append(input_name)
    if len(v) == 10:
        break
print(f"Names are: {v}")
print('It was nice to meet all of you')