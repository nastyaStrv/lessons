#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(a = 33, b = 'yjkm', c = 'ffff')
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:

values_list = [99, False, 'ooo']
values_dict = {'a': 80, 'b': False, 'c': 'kkk'}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [77, '99']
print_params(*values_list_2, 42)