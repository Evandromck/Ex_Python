j = float(input("Digite j:"))
i = float(input("Digite i:"))
n = float(input("Digite n:"))
limite = n - 1
nj2 = 0
nj3 = 0
nj5 = 0
nj7 = 0
nj11 = 0
nj13 = 0
ni2 = 0
ni3 = 0
ni5 = 0
ni7 = 0
ni11 = 0
ni13 = 0

d = [0]
c = [0]
cb = [0]
ca = [2, 3, 5, 7, 9, 11, 13]
c.append(j)
c.append(i)
loc = len(ca) - 1

for jj in range(0, loc):
    for jj in range(0, loc):
        if (j % ca[jj]) == 0:
            d.append(ca[jj])
            jj += 1
        else:
            d.sort()

            for jj in range(0, loc):
                if (i% ca[jj]) == 0:
                    d.append(ca[jj])
                    jj += 1
                else:
                    d.sort()

            da = []
            for verd in d:
                if verd not in da:
                    da.append(verd)

                da.sort()

                if (0 in da):
                    da.remove(0)

                certo = 0
                certo1 = 0
                if (j > i):
                    while (len(cb) + 1) < n:
                        for ab in range(0, len(da)):
                            certo = da[ab] * i
                            certo1 = da[ab] * j
                            ab += 1
                            c.append(certo)
                            c.append(certo1)
                        for de in c:
                            if de not in cb:
                                cb.append(de)
                        c.sort()
                        cb.sort()
                else:
                    while (len(cb) + 1) < n:
                        for ab in range(0, len(da)):
                            certo = da[ab] * j
                            certo1 = da[ab] * i
                            ab += 1
                            c.append(certo)
                            c.append(certo1)
                        for de in c:
                            if de not in cb:
                                cb.append(de)
                        c.sort()
                        cb.sort()

                c.sort()
                cb.sort()

print(cb)
