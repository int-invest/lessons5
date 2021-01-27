with open('test3.txt', encoding='utf-8') as file:
    total_salary = 0
    z = 0
    my_list = []
    for line in file:
        c = line
        c = c.split()
        a = float(c[1])
        total_salary += a
        z += 1
        if(a < 20000):
            my_list.append(c[0])
    my_str = ', '.join(my_list)
    print(f'Зарплату меньше 20000 имеют: {my_str}')
    print(f'Общий зарплатный фонд: {total_salary}')
    print(f'Средняя ЗП: {round(total_salary / z, 2)}')