# ПОДБРАСЫВАНИЕ МОНЕТКИ
import random
import matplotlib.pyplot as plt


def coin_flip():
    return random.randint(0, 1)


def monte_carlo(n):
    results = 0
    data = []
    for i in range(n):
        flip_result = coin_flip()
        results += flip_result
        prob_value = results / (i + 1)
        data.append(prob_value)
    plt.axhline(y=0.5, color='r')
    plt.xlabel("Итерации")
    plt.ylabel("Вероятность")
    plt.plot(data)
    plt.show()
    return results/n


print("Final value: ", monte_carlo(5000))

