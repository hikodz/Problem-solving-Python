def less_cash(n, m, b):
    b.sort(reverse=True)
    Goal = 0
    Simple_Output = 0
    for type in b:
        if Goal and Goal < n:
            Goal += type
            Simple_Output += 1
        elif type <= n and Goal < n:
            Goal += type
            Simple_Output += 1
    return Simple_Output if Goal == n else -1
n, m =  map(int, (input("=> ").split()))
b =  list(map(int, (input("=> ").split())))
print(less_cash(n, m, b))