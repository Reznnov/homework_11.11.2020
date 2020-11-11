def ft_sum_even_part_lst(lst):
    summ = 0
    for i in lst:
        if i % 2 == 0:
            summ += i
    return summ
