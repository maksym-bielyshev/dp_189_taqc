def my_gen():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s*10+7


g = my_gen()
print(next(g))
print(next(g))
print(next(g))
