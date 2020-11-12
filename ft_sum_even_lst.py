def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_sum_even_lst(lst):
    dlin = ft_len(lst)
    summ = 0
    for i in range(dlin - 1):
        if i % 2 == 0:
            summ += lst[i]
    return summ
