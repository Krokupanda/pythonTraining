color = int(input())
if 0 <= color <= 36:
    if ((0 < color <= 10) and (color % 2 == 0)) or ((11 <= color <= 18) and (color % 2 != 0) or ((19 <= color <= 28) and (color % 2 == 0)) or ((29 <= color <= 36) and (color % 2 != 0))):
        print('черный')
    elif ((0 < color <= 10) and (color % 2 != 0)) or ((11 <= color <= 18) and (color % 2 == 0) or ((19 <= color <= 28) and (color % 2 != 0)) or ((29 <= color <= 36) and (color % 2 == 0))):
        print('красный')
    else:
        print('зеленый')

else:
    print('ошибка ввода')
