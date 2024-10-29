import multiprocessing
import datetime


def read_info(name):
    all_data = []

    with open(name, encoding='utf-8') as n:
        line = n.readline()
        while line:
            all_data.append(line)
            line = n.readline()


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

start = datetime.datetime.now()
for file in files:
    read_info(file)
end = datetime.datetime.now() - start
print("Линейное выполнение заняло:", end)
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_1 = datetime.datetime.now()
        data_list = pool.map(read_info, files)
        end_1 = datetime.datetime.now() - start_1
        print("Многопроцессное выполнение заняло:", end_1)



