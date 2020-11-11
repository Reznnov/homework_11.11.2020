def ft_rmstrchar(strr, less):
    spis = []
    now = ""
    risk = []
    for i in strr:
        spis.append(i)
    for j in spis:
        if j not in less:
            risk.append(j)
    for o in risk:
        now += o
    return now
