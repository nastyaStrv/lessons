import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []

    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]


start_time_line = datetime.datetime.now()

for filename in filenames:
    read_info(filename)

end_time_line = datetime.datetime.now()

print(f'{end_time_line - start_time_line} (линейный)')


if __name__ == '__main__':

    start_time_multi = datetime.datetime.now()

    with Pool(processes=4) as pool:


        pool.map(read_info, filenames)

    end_time_multi = datetime.datetime.now()

    print(f"{end_time_multi - start_time_multi} (многопроцессный)")



