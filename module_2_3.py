my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len(my_list):
    num_2 = my_list[num]
    num = num + 1
    if num_2 == 0:
        continue
    elif num_2 < 0:
        break
    else:
        print(num_2)



