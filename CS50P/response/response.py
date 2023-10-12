from validators import email

s = input('What is your email address? ')
s = s.strip()
if email(s) == True:
    print('Valid')
else:
    print('Invalid')
