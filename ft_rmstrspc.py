def ft_rmstrspc(strr):
    spis = []
    now = ""
    for i in strr:
        spis.append(i)
    for j in spis:
        if j == " ":
            spis.remove(j)
    for o in spis:
        now += o
    return now
