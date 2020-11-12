def ft_len(s):
    num = 0
    for i in s:
        num += 1
    return num


def ft_join(lst, se=" "):
    strr = ''
    dlin = ft_len(lst)
    for i in range(dlin):
        if i == dlin - 1:
            strr += lst[i]
        else:
            strr += lst[i] + se
    return strr
