


def is_prime(function):
    def wrapper(*args, **kwargs):
        sum_ch = function(*args, **kwargs)
        if sum_ch < 2:
            print("Состовное")
        for i in range(2, int(sum_ch / 2)):
            if sum_ch % i == 0:
                print('Составное')
                break
        else:
            print('Простое')

        return sum_ch
    return wrapper


@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    return summa


result = sum_three(2, 3, 6)
print(result)
