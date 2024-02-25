c = str(input('Digite algo: '))
if c.isalnum():
    print('({}) é alfanumérico' .format(c))
else:
    print('({}) não é alfanumérico' .format(c))
if c.isalpha():
    print('({}) é alfabético' .format(c))
else:
    print('({}) não é alfabético' .format(c))
if c.isnumeric():
    print('({}) é númerico' .format(c))
else:
    print('({}) não é númerico' .format(c))
if c.isdecimal():
    print('({}) é decimal'.format(c))
else:
    print('({}) não é decimal'.format(c))
if c.isspace():
    print('({}) somente possuí espaços' .format(c))
else:
    print('({}) não possuí somente espaços' .format(c))
if c.islower():
    print('({}) é somente minúsculo' .format(c))
else:
    print('({}) não é somente minúsculo' .format(c))
if c.isupper():
    print('({}) é somente maíusculo'.format(c))
else:
    print('({}) não é somente maíusculo'.format(c))
