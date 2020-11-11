def ft_pos_neg_separator_lst(lst):
    otr = []
    nol = []
    pol = []
    it = []
    for i in lst:
        if i < 0:
            otr.append(i)
        elif i == 0:
            nol.append(i)
        else:
            pol.append(i)
    it.append(otr)
    it.append(nol)
    it.append(pol)
    return it
