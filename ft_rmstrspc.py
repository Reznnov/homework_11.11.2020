def ft_rmstrspc(strr):
    spis = []
    now = ""
    for i in strr:
        spis.append(i)
    print(spis)
    for j in spis:
        if j == " ":
            spis.remove(j)
    print(spis)
    for o in spis:
        now += o
    return now
