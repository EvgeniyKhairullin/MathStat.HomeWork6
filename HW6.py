left=80-1.96*16/256**(1/2)
right=80+1.96*16/256**(1/2)
print(f'95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [{left};{right}].')

import numpy as np
arr=np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
print(f'Среднее выборочное: {np.mean(arr): .2f},\n'
      f'Размер выборки n={len(arr)},\n'
      f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(arr, ddof=1): .2f}.'
     )
import scipy.stats as stats
def t_from_table(confidens, len_array):
    alpha=(1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)
print(f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t_from_table(0.95, len(arr)): .3f}')
def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3), \
           round(np.mean(arr)+t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3)

print(f'95%-й доверительный интервал для истинного значения Х: {confidens_int(arr, 0.95)}.')

a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x_1 = np.mean(a)
x_2 = np.mean(b)
delta = x_1 - x_2
n = len(a)
D1 = np.var(a, ddof = 1)
D2 = np.var(b, ddof = 1)

D = (D1 + D2) / 2
SE = np.sqrt(D/n + D/n)

t = stats.t.ppf(0.975, 2 * (n - 1))

result = (delta - t*SE, delta + t*SE)
print(f"Доверительный интервал: {result}")