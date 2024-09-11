def team_num(team1_num, team2_num):
    print('В команде "Мастера кода" участников: %s!' % (team1_num))
    print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))


def resolved_tasks(score_2, team1_time):
    print('Команда Волшебники данных решила задач: {}'.format(score_2))
    print("Волшебники данных решили задачи за {} с.!".format(team1_time))

def info(score_1, score_2):
    print(f'Команды решили {score_1} и {score_2} задач')

def challenge_result(score_1, score_2, team1_time, team2_time):
    tasks_total = (score_1 + score_2)
    time_avg = (team1_time + team2_time)/tasks_total
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print('Победа команды Волшебники Данных!')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print('Победа команды Мастера кода!')
    else:
        print('Ничья')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."')


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451


team_num(team1_num,team2_num)
resolved_tasks(score_2, team1_time)
info(score_1, score_2)
challenge_result(score_1, score_2, team1_time, team2_time)