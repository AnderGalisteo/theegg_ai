"""
Está claro que uno es O(n) y el otro O(1). Con esta lección he aprendido que cuando intentas medirlo, no sale lo que esperas por implementaciones del hardware! Si fuera otra operación, se vería mejor, pero la suma está ultra optimizada en todos los procesadores.

La suma lineal recorre todos los elementos una vez, su big O es O(n)!

La suma constante de Newton es O(1) ya que no importa le número, la cantidad de operaciones es la misma!

"""
import time
import numpy as np
from sklearn.linear_model import LinearRegression



def sum_line(number_elements):    
    sum_num = 0
    for i in range(number_elements + 1):
        sum_num = sum_num + i
    return sum_num


def sum_const(number_elements):
    sum_num = (number_elements/2)*(number_elements+1)
    return sum_num


if __name__ == "__main__":
    num_iter = 60000
    print("Vamos a calcular O() de los dos algoritmos")
    sum_line_time = []
    sum_const_time = []
    sum_line_array = []
    sum_const_array = []
    x = list(range(50000,num_iter+1))
    for i in x:
        tpre = time.time()
        sum_line_array.append(sum_line(i))
        tpost = time.time()
        sum_line_time.append(tpost-tpre)
        tpre = time.time()
        sum_const_array.append(sum_const(i))
        tpost = time.time()
        sum_const_time.append(tpost-tpre)
    model = LinearRegression()
    npArray = np.array(x).reshape((-1, 1))
    model.fit(npArray,sum_line_time)
    r_sq = model.score(npArray, sum_line_time)
    print('coefficient of determination linear:', r_sq)
    print('intercept linear:', model.intercept_)
    print('slope linear:', model.coef_)

    model = LinearRegression()
    model.fit(npArray,sum_const_time)
    r_sq = model.score(npArray, sum_const_time)
    print('coefficient of determination constant:', r_sq)
    print('intercept constant:', model.intercept_)
    print('slope constant:', model.coef_)
    