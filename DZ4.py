with open('test4.txt', encoding='utf-8') as file:
    for line in file:
        c = line
        c = c.split()
        if (c[0] == 'One'):
            c[0] = 'Один'
        elif (c[0] == 'Two'):
            c[0] = 'Два'
        elif (c[0] == 'Three'):
            c[0] = 'Три'
        elif (c[0] == 'Four'):
            c[0] = 'Четыре'
        a = ' '.join(c)
        file2 = open('test41.txt', 'a')
        file2.write(a + "\n")
        file2.close()