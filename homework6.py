my_dict = {'Anastasiia':1995, 'Anna':1989, 'Sasha':2000, 'Olga':1985}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Oleg', 'Такого значения нет'))
my_dict.update({'Vlad':1900,'Elena':2001})
print(my_dict)
a=my_dict.pop('Olga')
print(my_dict)
print(a)
print(my_dict)

my_set={1,4,5,5,5,3,2,'Star','Star', (9,8,8,7)}
print(my_set)
my_set.add(6)
print(my_set)
my_set.add('Home')
print(my_set)
my_set.remove((9,8,8,7))
print(my_set)







