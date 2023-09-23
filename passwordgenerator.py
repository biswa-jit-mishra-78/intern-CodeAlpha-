import random as rn
latters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '1234567890'
special_char = '@#$%^&*+_><?[({})]'
print('*******')
print(rn.choice(latters+latters),rn.choice(digits+special_char),rn.choice(special_char+digits),rn.choice(latters+latters),rn.choice(digits+special_char),rn.choice(special_char+digits),rn.choice(latters+latters),sep='')
print("*******")
