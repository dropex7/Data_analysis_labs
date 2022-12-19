import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def show_charts(old_data, new_data, title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
    fig.suptitle(title)
    ax1.set(xticks=[])
    ax2.set(xticks=[])
    ax1.plot(old_data, 'g')
    ax2.plot(new_data, 'g')
    plt.show()


def average_of_array(lst):
    return sum(lst) / len(lst)


def smoothing_method(data, count_of_elements):
    length = data.shape[0]
    result = []
    for k in range(length):
        sum_of_x = []
        for j in range(count_of_elements):
            if k - j < 0:
                break
            else:
                sum_of_x.append(data[k - j])
        result.append(average_of_array(sum_of_x))
    return result


def weighted_smoothing_method(data, count_of_elements):
    length = data.shape[0]
    result = []
    for k in range(count_of_elements - 1, length):
        sum_of_x = sum([(data[k-j]) * (count_of_elements - j) for j in range(0, count_of_elements)])
        result.append(sum_of_x / sum([i for i in range(1, count_of_elements)]))
    return result


def make_solution(x_data, name):
    x = np.array(x_data)
    x_sm = smoothing_method(x_data, 10)
    x_wsm = weighted_smoothing_method(x_data, 10)
    show_charts(x, x_sm, f'{name} with smoothing')
    show_charts(x, x_wsm, f'{name} with weighted smoothing')


gold = pd.read_csv('stock_quotes/gold.csv', sep=';')
oil_brent = pd.read_csv('stock_quotes/oil_Brent.csv', sep=';', index_col='Дата')
oil_wti = pd.read_csv('stock_quotes/oil_WTI.csv', sep=';', index_col='Дата')
silver = pd.read_csv('stock_quotes/silver.csv', sep=';', index_col='Дата')
card = pd.read_csv('stock_quotes/card.csv', sep=';', index_col='Дата')


make_solution(gold["Цена"], 'Gold')
make_solution(oil_brent["Цена"], 'Oil brent')
make_solution(oil_wti["Цена"], 'Oil WTI')
make_solution(silver["Цена"], 'Silver')
make_solution(card["Цена"], 'Card')
