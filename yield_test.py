
def test_yield(x, j=0):
    print(str(x))
    yield x
    j += 1
    if j > 10:
        yield


if __name__ == '__main__':
    i = [10]
    while i:
        print([x for x in i])
        i = test_yield(i)
