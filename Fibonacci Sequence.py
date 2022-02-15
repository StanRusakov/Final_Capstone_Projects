import sys

print(sys.version)
print(sys.executable)

# number validation
def inp_num():
    num = ''
    while isinstance(num, int) == False or num < 0:
        try:
            num = int(input('\nEnter number:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return num
    
# create Fibonacci Sequence
def create_f_seq(user_input):
    f_list = [0,1]

    for i in range(0,user_input-2):
        f_list.append(f_list[i] + f_list[i+1])

    return f_list

# main function
def main():
    user_input = inp_num()
    fib_seq = create_f_seq(user_input)

    if user_input <= 1:
        print('\nFibonacci Sequence is:\n')
        return fib_seq[0]

    elif user_input == 2:
        print('\nFibonacci Sequence is:\n')
        return [fib_seq[0], fib_seq[1]]

    else:
        print('\nFibonacci Sequence is: ')
        return fib_seq

print(main())