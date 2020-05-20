def task():
    a = int(input('a'))
    m = int(input('m'))
    b = int(input('b'))
    result = [a,m,b]
    return result


def flow():
    while True:
        print(estimate(*task()))
        answer = input('Do you want ot analyze another file? y/n: ').lower()
        if answer != 'y':
            break


        # standard_deviation(a,b)


def estimate(a, m, b):
    return (a+4*m + b)/6


def standard_deviation(a, b):
    (b-a)/6


if __name__ == '__main__':
    flow()
