from random import randint


def step_count(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n % 4 == 1:
            n = n - 1
        else:
            n = n + 1
        count += 1
    return count


def solution(n):
    err_msg = "The parameter n is malformed"
    try:
        n_cast = int(n)
        if (not isinstance(n,str)) or (len(n) > 309) or (n_cast < 1):
            raise Exception
        return step_count(n_cast)
    except Exception as e:
        raise Exception("{}. {}".format(err_msg,e).strip(". "))


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == '__main__':
    rand_n = random_with_N_digits(309)
    print(solution(str(rand_n)))