def ft_sum_even_lst(lst):
    dlin = len(lst)
    summ = 0
    for i in range(dlin - 1):
        if i % 2 == 0:
            summ += lst[i]
    return summ
