def crazy(min_, filename):
    print("generator started")
    yield min_
    g=crazy(min_+1)
    while True:
        yield next(g)
        yield min_