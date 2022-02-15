import sys
import math

print(sys.version)
print(sys.executable)

# ask to enter a number
def num_valid():
    num = ''
    while isinstance(num, int) == False or num < 0 or num > 15:
        try:
            num = int(input('\nEnter number (0-15):\n'))
        except:
            print('\nWrong input. Please, enter NUMBER 0-15!\n')
            continue
    else:
        return num

# define how many digits should be return
def pi_func(valid_num, pi):
    conv_pi = str(pi)
    dig_list = []

    for nums in conv_pi[2:valid_num + 2]:
        dig_list.append(nums)

    dig_num = ''.join(dig_list)
    return int(dig_num)

# main function of project
def main():
    pi = math.pi
    m_num = math.floor(pi)

    valid_num = num_valid()
    if valid_num != 0:
        ch_num = pi_func(valid_num, pi)
    else:
        print('Your pi number is: ')
        return m_num
    
    print('Your pi number is: ')
    return f"{m_num}.{ch_num}"

print(main())