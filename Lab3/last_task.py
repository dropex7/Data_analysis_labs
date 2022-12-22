import random
import matplotlib.pyplot as plt

choice = random.randint(0, 1)

if choice == 0:
    def pick_note():
        note = random.randint(1, 100)

        if note % 2 != 0 or note == 10:
            return False
        elif note % 2 == 0:
            return True


if choice == 1:
    def pick_note():
        note = random.randint(1, 100)

        if note % 2 == 0 or note == 11:
            return False
        elif note % 2 == 1:
            return True


def play(total_money, bet_money, total_plays):
    num_of_plays = []
    money = []

    play_number = 1

    for play_number in range(total_plays):
        if pick_note():
            total_money += bet_money
            num_of_plays.append(play_number)
            money.append(total_money)
        else:
            total_money -= bet_money
            num_of_plays.append(play_number)
            money.append(total_money)

    plt.ylabel('Деньги игрока в $')
    plt.xlabel('Количество ставок')
    plt.plot(num_of_plays, money)
    final_funds.append(money[-1])
    return final_funds


final_funds = []

for i in range(10):
    ending_fund = play(10000, 100, 50)

print("Количество ставок 50")
print("Игрок начал игру с $10,000")
print("Игрок закончил игру с ", str(sum(ending_fund) / len(ending_fund)))
print("-----------------------------------------------------")

plt.show()

for i in range(10):
    ending_fund = play(10000, 100, 500)

print("Количество ставок 500")
print("Игрок начал игру с $10,000")
print("Игрок закончил игру с ", str(sum(ending_fund) / len(ending_fund)))
print("-----------------------------------------------------")

plt.show()

for i in range(10):
    ending_fund = play(10000, 100, 5000)

print("Количество ставок 5000")
print("Игрок начал игру с $10,000")
print("Игрок закончил игру с ", str(sum(ending_fund) / len(ending_fund)))

plt.show()