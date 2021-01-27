with open('test2.txt', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        print(f'{i} {line.strip()}. В строке слов - {len(line.split())} шт')