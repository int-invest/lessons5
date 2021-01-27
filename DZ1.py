file = open('test1.txt', 'w+')
while True:
    content = input('Введите текст или нажмите "Enter" для завершения: ')
    if content == "":
        break
    file.writelines(content + '\n')
file.close()



