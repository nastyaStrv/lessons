immutable_var=('ok', 6, True)
print(immutable_var)
print(type(immutable_var))

#immutable_var[1]=9 #TypeError: 'tuple' object does not support item assignment
#print(immutable_var)

mutable_list=[7,'go',False]
mutable_list[-1]=True
print(mutable_list)

IM_t=('Immutable tuple: ', immutable_var)
ML=('Mutable list: ', mutable_list)
print(IM_t,ML)