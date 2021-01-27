with open('test6.txt', encoding='utf-8') as file:
    my_dict = {}
    for line in file:
        line = line.replace('(л)','').replace('(пр)','').replace('(лаб)','').replace('\n','').replace('—','')
        my_str = line.split(':')
        my_str[1] = sum(map(int,my_str[1].split()))
        my_dict.update({my_str[0]:my_str[1]})
    print(my_dict)



