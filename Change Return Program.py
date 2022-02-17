import sys
from math import floor

print(sys.version)
print(sys.executable)

# user input cost
def cost_func():
    c_num = float(input('\nPrice:\n'))
    while c_num < 0.01:
        try:
            print("\nToo low price. Couldn`t be lower then 0.01$:\n")
            c_num = float(input('\nPrice:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return c_num

# user input amount of money
def input_amount_func(cost):
    a_num = float(input('\nAmount of money:\n'))
    while a_num < cost:
        try:
            print(f"\nNot enough money. Couldn`t be less then {cost}$:\n")
            a_num = float(input('\nAmount of money:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return a_num

# defiine the change
def change_func(paper_money, coins, diff):
    if diff >= paper_money['100$']:
        p_m_hundr = floor(diff / paper_money['100$'])
        print(f"\t100$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['100$'])

    elif diff >= paper_money['50$']:
        p_m_hundr = floor(diff / paper_money['50$'])
        print(f"\t50$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['50$'])

    elif diff >= paper_money['20$']:
        p_m_hundr = floor(diff / paper_money['20$'])
        print(f"\t20$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['20$'])
        
    elif diff >= paper_money['10$']:
        p_m_hundr = floor(diff / paper_money['10$'])
        print(f"\t10$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['10$'])

    elif diff >= paper_money['5$']:
        p_m_hundr = floor(diff / paper_money['5$'])
        print(f"\t5$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['5$'])

    elif diff >= paper_money['2$']:
        p_m_hundr = floor(diff / paper_money['2$'])
        print(f"\t2$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['2$'])

    elif diff >= paper_money['1$']:
        p_m_hundr = floor(diff / paper_money['1$'])
        print(f"\t1$ * {p_m_hundr}")
        return diff - (p_m_hundr * paper_money['1$'])

    elif diff >= coins['50c']:
        p_m_hundr = floor(diff / coins['50c'])
        print(f"\t50c * {p_m_hundr}")
        return diff - (p_m_hundr * coins['50c'])

    elif diff >= coins['25c']:
        p_m_hundr = floor(diff / coins['25c'])
        print(f"\t25c * {p_m_hundr}")
        return diff - (p_m_hundr * coins['25c'])

    elif diff >= coins['10c']:
        p_m_hundr = floor(diff / coins['10c'])
        print(f"\t10c * {p_m_hundr}")
        return diff - (p_m_hundr * coins['10c'])

    elif diff >= coins['5c']:
        p_m_hundr = floor(diff / coins['5c'])
        print(f"\t5c * {p_m_hundr}")
        return diff - (p_m_hundr * coins['5c'])

    elif diff >= coins['1c']:
        p_m_hundr = floor(diff / coins['1c'])
        print(f"\t1c * {p_m_hundr}")
        return diff - (p_m_hundr * coins['1c'])

    else:
        p_m_hundr = 0
        return p_m_hundr


# main function
def main():
    paper_money = {'1$': 100, '2$': 200, '5$': 500, '10$': 1000, '20$': 2000, '50$': 5000, '100$': 10000}
    coins = {'1c': 1, '5c': 5, '10c': 10, '25c': 25, '50c': 50}

    cost = cost_func()
    input_amount = input_amount_func(cost)

    diff = int(input_amount * 100) - int(cost * 100)

    print('\nYour change:')
    for i in range(1, len(paper_money) + len(coins) + 1):
        change = change_func(paper_money, coins, diff)
        diff = change

    return f"Total change: {input_amount - cost:.2f}$"

print(main())