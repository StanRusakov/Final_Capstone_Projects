import sys
import math

print(sys.version)
print(sys.executable)

# number validation
def inp_num():
    num = ''
    while isinstance(num, int) == False or num < 2:
        try:
            num = int(input('\nEnter number:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER (number >= 2)!\n')
            continue
    else:
        return num

# define is number prime or not
def def_pr(user_input):
    for i in range(2, int(math.sqrt(user_input)) + 1):
        if user_input % i == 0:
            # return not prime number
            return False
    
    # return prime number
    return True

# prime factor function
def factor_func(user_input):
    factor_list = []
    res = False
    t_num = 2
    while res == False:
        if user_input % 2 == 0:
            user_input = user_input / t_num
            res = def_pr(user_input)
            factor_list.append(t_num)
            
        else:
            t_num = 2
            while user_input % t_num != 0:
                t_num += 1
                continue
            else:
                user_input = user_input / t_num
                res = def_pr(user_input)
                factor_list.append(t_num)
                
    factor_list.append(int(user_input))
    return factor_list

# main function
def main():
    user_input = inp_num()

    pr_nums = def_pr(user_input)

    if pr_nums == False:
        f_l = factor_func(user_input)
        f_l_conv = [str(x) for x in f_l]
        print('\nThe Prime Factorization is:')
        return ' * '.join(f_l_conv)

    elif pr_nums == True:
        print(f"\n{user_input} is prime.")

print(main())
