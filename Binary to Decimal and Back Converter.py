import sys

print(sys.version)
print(sys.executable)

# choose convertion
def choose_func():
    ch_conv = input('\nDecimal to Binary press D. Binary to Decimal press B.\n').upper()
    while ch_conv.isalpha() == False and ch_conv != 'D' and ch_conv != 'B':
        try:
            print(f"\nWrong letter. Press D or B.\n")
            ch_conv = input('\nDecimal to Binary press D. Binary to Decimal press B.\n').upper()
        except:
            print('\nWrong input. Please, enter letter!\n')
            continue
    else:
        return ch_conv

# check decimal number
def dec_num_func():
    d_num = int(input('\nDecimal number:\n'))
    while d_num < 0:
        try:
            print("To low number. The lowest is 1.")
            d_num = int(input('\nDecimal number:'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return d_num

# check binary number
def binar_num_func():
    dec_nums = [2,3,4,5,6,7,8,9]
    b_num = input('\nBinary number:\n')
    sep_num = sep_num_func(b_num)
    while len(b_num) < 4 or b_num.isdigit() == False or any(items in sep_num for items in dec_nums):
        try:
            print("Wrong number. Binary number should consist only 0`s and 1`s.")
            b_num = input('\nBinary number:')
            sep_num = sep_num_func(b_num)
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return b_num

# separate user input number on digits
def sep_num_func(b_num):
    nums = [int(num) for num in b_num]
    return nums

# convert decimal to binary
def dec_to_binar_func(dec_num):
    binar_list = []
    while dec_num != 0:
        remainder = dec_num % 2
        binar_list.append(int(remainder))
        dec_num = (dec_num - remainder) / 2
    while len(binar_list) % 4 != 0:
        binar_list.append(0)
    return binar_list[::-1]

# convert binary to decimal
def binar_to_dec_func(binar_num):
    dec_num = 0
    
    for i, num in enumerate(binar_num[::-1]):
        res = int(num) * (2 ** i)
        if res != 0:
            dec_num += res

    return dec_num

# main function
def main():
    choose = choose_func()

    if choose == 'D':
        dec_num = dec_num_func()
        dec_to_binar = dec_to_binar_func(dec_num)
        print("Binary number:")
        return dec_to_binar
    
    else:
        binar_num = binar_num_func()
        binar_to_dec = binar_to_dec_func(binar_num)
        print("Decimal number:")
        return binar_to_dec

print(main())