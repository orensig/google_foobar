from collections import Counter
import random


def solution(data, n):
    if not isinstance(data, list) or len(data) >= 100 or not isinstance(n,int):
        raise Exception("""One of the parameters: data and n (or both) is not in a proper format.
        data should be a list shorter than 100 items and n should be an integer""")
    _data = data.copy()
    data_count = Counter(_data)
    result = [_id for _id in _data if data_count[_id] <= n]
    print(type(result))
    return result


def main():
    # result = solution([2, 2, 1, 3, 3, 3, 4, 5, 5], 2)
    # result = solution(data={"a":5, "b":6},n=5)
    # result = solution(data=list(range(90)), n=1.1)
    result = solution(data=random.sample(range(105), 101), n=5)
    print(f"result is {result}")
    return


if __name__ == '__main__':
    main()