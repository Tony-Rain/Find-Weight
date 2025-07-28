import random

from classes import Matrix, Vector


def weight(seed, n):
    random.seed(seed)
    return Vector([[random.random() for _ in range(n)]])


def gen_vectors_and_y(seed, vectors_len, count):
    w = weight(seed, vectors_len + 1)
    x = []
    for i in range(count):
        vector = []
        vector.append(1)
        for j in range(vectors_len):
            vector.append(random.random())
        x.append(vector)
    x = Matrix(x)
    y = []
    for elem in x.matrix:
        y.append((Vector([elem]) * w).matrix)
    print(f"answer: {y}\n"
          f"date: {x}\n"
          f"weight: {w}")
    return y, x, w


def find_w(vectors_len, count):
    # создание альфы - длинны вектора-производной, деление на count - для усреднения функции ошибки бля разного кол ва точек
    al = Vector([[00.1 / count]])  # менять 0.1 и/или убрать добавить деление на count
    ans = gen_vectors_and_y(1, vectors_len, count)
    w_true = ans[2]
    x_tran = Matrix(ans[1].matrix).tranponate()
    w_find = weight(2, vectors_len + 1).tranponate()
    y = []
    for i in range(len(ans[0])):
        elem = (1 + random.random()) / 5 * ans[0][i][0][0]  # random.random() -добавление шума, /5 - уменьшение шума
        y.append([elem])
    y = Matrix(y)
    for i in range(100000):  # увеличивать кол во циклов для более точной настройки
        l = x_tran * (ans[1] * w_find - y)
        del_l = l * al
        w_find -= del_l
    w_find.tranponate()
    return (f'weight_TRUE: {w_true}\n'
            f'weight_FALSE: {w_find}\n')


print(find_w(5, 1000))
