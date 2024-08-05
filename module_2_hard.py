import random
def selection():
    first_field = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    total_first_field = random.choice(first_field)
    return total_first_field
total_first_field = selection()

def password_options(n):
    password = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
                14: 1611325212343114105968, 15: 1214114232133124115106978, 16: 1317115262143531341251161079,
                17: 11621531441351261171089, 18: 12151811724272163631545414513612711810,
                19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911}
    passcode = password.get(n)
    return passcode

n = selection()
print('Key: ', n)

para1 = list(range(1, n))
para2 = list(range(1, n))
parii = []
result = ''

for i in para1:
    for j in para2:
        pr1 = i
        pr2 = j
        if pr1 >= pr2:
            continue
        else:
            krat = n % (pr1 + pr2)
            if krat == 0:
                parii.append([pr1, pr2])
                result = result + str(pr1) + str(pr2)
print(parii)
print(result)





