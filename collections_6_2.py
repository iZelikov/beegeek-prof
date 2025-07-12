def make_trans():
    trans = {chr(k): v for k, v in zip(range(ord('a'), ord('z') + 1), input())}
    print(*(trans.get(c.lower(), c) for c in input()), sep="")

