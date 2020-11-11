def ft_odd_even_separator_lst(lst):
    chet = []
    nechet = []
    it = []
    for i in lst:
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    it.append(chet)
    it.append(nechet)
    return it
