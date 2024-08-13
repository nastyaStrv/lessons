data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    summ_ = 0
    for i in args:
        if isinstance(i, list):
            for j in i:
                summ_ += calculate_structure_sum(j)
        elif isinstance(i, tuple):
            for j in i:
                summ_ += calculate_structure_sum(j)
        elif isinstance(i, set):
            for j in i:
                summ_ += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                summ_ += calculate_structure_sum(key, value)
        elif isinstance(i, str):
            summ_ += len(i)
        elif isinstance(i, int):
            summ_ += i
    return summ_


result = calculate_structure_sum(data_structure)
print(result)
