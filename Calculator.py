import sys
import operator

print(sys.version)
print(sys.executable)

# input numbers
def num_inp_func():
    d_num = float(input('\nNumber:\n'))
    while isinstance(d_num, float) == False:
        try:
            print("Nope. Wrong input.")
            d_num = float(input('\nNumber:'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return d_num

# ask input operator for calculation
def oper_sign_func(ops):
    o_s_s = input("\nChoose operator '+' Add, '-' Substract, '*' Multiply, '/' Divide.\n")
    while len(o_s_s) != 1 or o_s_s not in ops.keys():
        try:
            print("\nWrong choice!")
            o_s_s = input("Choose operator '+' Add, '-' Substract, '*' Multiply, '/' Divide.\n")
        except:
            print('\nWrong input. Please, try again!\n')
            continue
    else:
        return o_s_s

# exit or continue
def ex_qu_func():
    e_q = ' '
    while e_q != 'Q' and e_q != 'G' and e_q != 'C':
        print('Q(quit) or G(continue) or C(clear)')
        e_q = input('Your choice: ').upper()

    else:
        return e_q

# main function
def main():
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    print("*** Welcome to calculator! ***")

    calculate = True
    result = num_inp_func()

    while calculate:
        oper_sign = oper_sign_func(ops)
        num_inp = num_inp_func()
        print(f"\n{result} {oper_sign} {num_inp} = ")
        result = ops[oper_sign](result, num_inp)
        print(f"\t{result}\n")
        ex_qu = ex_qu_func()
        if ex_qu == 'Q':
            calculate = False
        elif ex_qu == 'C':
            result = num_inp_func()
            continue
        else:
            continue

    print('Good bye!')
print(main())