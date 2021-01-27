import json
with open('test7.txt', encoding='utf-8') as file:
    sum_profit = 0
    i = 0
    dict_p = {}
    for line in file:
        line = line.split()
        #print(line)
        profit = int(line[2]) - int(line[3])
        #print(f'Прибыль {profit}')

        if (profit > 0):
            sum_profit += profit
            i +=1
        dict_p.update({line[0]: profit})

    val_profit = sum_profit / i
    #print(f'Средняя прибыль: {round(val_profit, 2)}')
    dict_a = {'average_profit': round(val_profit, 2)}
    #print(dict_p)
    #print(dict_a)
    my_list = [dict_p, dict_a]
    print(my_list)

    with open("my_file.json", "w", encoding='utf-8') as write_f:
        json.dump(my_list, write_f)

        to_json = json.dumps(my_list)
        print(f'Файл json со следующим содержимым: \n '
              f' {to_json }')
