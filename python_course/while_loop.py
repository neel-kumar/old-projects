#this will check your password
name = input('Enter Name : ')
correct_password = 'python123'
password = input('Enter password : ')
while password != correct_password:
    password = input('Try Again ' + name + ' : ')
print('Hello ', name)
