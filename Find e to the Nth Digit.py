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
def e_func(valid_num, e):
    conv_e = str(e)
    dig_list = []

    for nums in conv_e[2:valid_num + 2]:
        dig_list.append(nums)

    dig_num = ''.join(dig_list)
    return int(dig_num)

# main function of project
def main():
    e = math.e
    m_num = math.floor(e)

    valid_num = num_valid()
    if valid_num != 0:
        ch_num = e_func(valid_num, e)
    else:
        print('Your e number is: ')
        return m_num
    
    print('Your e number is: ')
    return f"{m_num}.{ch_num}"

print(main())