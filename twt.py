import pyperclip
while(1):
    ligma = input('enter twitter url: ')
    x = ligma[14:].split("/")
    # print(f'@{x[0]}_{x[2]}')
    b = '@' + x[0] + '_' + x[2]
    # print(b)
    pyperclip.copy(b)
