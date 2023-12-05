import random


def roll_dice():
    return random.randint(0, 1)


max_heads = 0
max_tails = 0
current_order = 0
previous_result = None

balance = 100000
default_bet = 100
max_bet = 1
bet = default_bet
bet_multiplier = 4
drawdown = 9999999999999
max_balance = 0

for i in range(100):
    if balance < drawdown:
        drawdown = balance

    if balance > max_balance:
        max_balance = balance

    if bet > max_bet:
        max_bet = bet

    if balance < bet:
        print('your money gone')
        break


    balance = balance - bet

    result = roll_dice()

    if result == previous_result:
        current_order += 1
    else:
        current_order = 1

    if result == 1:
        # print('H',end='')
        balance = balance + (bet * 2)
        bet = default_bet
        max_heads = max(current_order, max_heads)
    else:
        bet = bet * bet_multiplier
        # print('',end='')
        max_tails = max(current_order, max_tails)

    previous_result = result

    if (i % 100 == 0):
        max_heads = 0
        max_tails = 0

print()
print(f'Heads: {max_heads}')
print(f'Tails: {max_tails}')
print()
print(f'balance: {balance}')
print(f'max balance: {max_balance}')
print(f'drawdown: {drawdown}')
print(f'max_bet: {max_bet}')
