def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res > 1:
            for i in range(2, res + 1):
                if res % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
