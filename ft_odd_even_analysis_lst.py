def minn_chet(x):
    ret = 0
    while x:
        ret = min(x)
        if ret % 2 == 0:
            break
        x.remove(ret)
    return ret


def maxx_chet(o):
    ret = 0
    while o:
        ret = max(o)
        if ret % 2 == 0:
            break
        o.remove(ret)
    return ret


def maxx_nechet(q):
    ret = 0
    while q:
        ret = max(q)
        if ret % 2 != 0:
            break
        q.remove(ret)
    return ret


def minn_nechet(y):
    ret = 0
    otv = 0
    while y:
        ret = min(y)
        if ret % 2 != 0:
            break
        y.remove(ret)
    return ret


def col_chet(z):
    col = 0
    for i in z:
        if i % 2 == 0:
            col += 1
    return col


def col_nechet(a):
    col = 0
    for i in a:
        if i % 2 != 0:
            col += 1
    return col


def summ_chet(lst):
    summ = 0
    for i in lst:
        if i % 2 == 0:
            summ += i
    return summ


def summ_nechet(lst):
    summ = 0
    for i in lst:
        if i % 2 != 0:
            summ += i
    return summ




def ft_odd_even_analysis_lst(lst):
    print("Анализ списка:")
    print(f"Количество четных чисел: {col_chet(lst)},\t\tКоличество нечетных чисел: {col_nechet(lst)},\n"
          f"Максимальная четная цифра: {maxx_chet(lst)},\t\tМаксимальная нечетная цифра: {maxx_nechet(lst)},\n"
          f"Минимальная четная цифра: {minn_chet(lst)},\t\tМинимальная нечетная цифра: {minn_nechet(lst)},\n"
          f"Сумма четных чисел: {summ_chet(lst)},\t\t\tСумма нечетных чисел: {summ_nechet(lst)},\n")
          
