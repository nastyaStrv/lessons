import io


def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'test.txt'
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        bbt = file.tell()
        file.write(i + '\n')
        strings_positions[(len(strings_positions) + 1, bbt)] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
