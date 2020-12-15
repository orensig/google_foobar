from math import factorial
from collections import Counter
from fractions import gcd


def generate_gcd_array(max_arr_size):
    temp_max_arr_size = max_arr_size + 1
    _gcd_array = [[0 for c in range(temp_max_arr_size)] for r in range(temp_max_arr_size)]
    for i in range(temp_max_arr_size):
        for j in range(i, temp_max_arr_size):
            _gcd_array[i][j] = gcd(i,j)
            if i != j:
                _gcd_array[j][i] = _gcd_array[i][j]
    return _gcd_array


def generate_factorial_array(max_fact):
    temp_max_fact = max_fact+1
    _fact_array = []
    for i in range(temp_max_fact):
        _fact_array.append(factorial(i))
    return _fact_array


def count_cycles(_fact_array, _partition, _max_size):
    numer = _fact_array[_max_size]
    denom = 1
    for grp, fix in Counter(_partition).items():
        denom *= (grp**fix)*_fact_array[fix]
    cycles_cntr = numer // denom
    return cycles_cntr


def generate_partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def is_valid_input(_w, _h, _s):
    if any([_w < 1, _h < 1, _s < 2, _w > 12, _h > 12, _s > 20]):
        return False
    return True


def solution(w, h, s):
    err_msg = "One of the parameters: w, h, s is malformed"
    _is_valid_input = is_valid_input(_w=w, _h=h, _s=s)
    try:
        if not _is_valid_input:
            raise Exception
        sum_cycles_n_partition = 0
        max_w_h = max(w, h)
        gcd_array = generate_gcd_array(max_w_h)
        fact_array = generate_factorial_array(max_w_h)
        w_partitions = sorted(generate_partitions(w))
        h_paritions = sorted(generate_partitions(h))
        for _w_part in w_partitions:
            for _h_part in h_paritions:
                sect_2 = count_cycles(fact_array, _w_part, w) * count_cycles(fact_array, _h_part, h)
                sect_3 = s**sum([sum([gcd_array[a][b] for a in _w_part]) for b in _h_part])
                sect_2_3_prod = sect_2*sect_3
                sum_cycles_n_partition += sect_2_3_prod
        denom = fact_array[w]*fact_array[h]
        ans = str(sum_cycles_n_partition//denom)
        return ans
    except Exception as e:
        raise Exception("{}. {}".format(err_msg, e).strip(". "))



if __name__ == '__main__':
    w = 20
    h = 12
    s = 20
    sol1 = solution(w,h,s)
    # sol2 = answer(w,h,s)
    # print(sol1==sol2)