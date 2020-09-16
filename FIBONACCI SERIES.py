x=int(input());l=[0,1];any(map(lambda _ :l.append(sum(l[-2:])),range(2,10000)))
print(l[x])