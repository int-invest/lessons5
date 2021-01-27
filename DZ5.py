with open('test5.txt', 'w') as file:
    str_num = input('Введите числа через пробел: ')
    file.write(str_num + '\n')
    num = str_num.split()
    sum_num = sum(map(int, num))
    str_sum = str(sum_num)
    file.write(f'Сумма: {str_sum}')

    print(sum_num)
