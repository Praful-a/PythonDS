def strcpy(s1, s2):
    if len(s2) == 0:
        return s1
    else:
        c = strcpy(s1, (s2)[1:-1])
        return c


s1 = input()
s2 = input()
res = strcpy(s1, s2)
print(res)
