import sys
import math

print(sys.version)
print(sys.executable)

# input validation
def inp_func():
    user_inp = ''
    while user_inp.isalpha() == False and user_inp != 'Y' and user_inp != 'N':
        try:
            user_inp = input('\nPress Y to search next Prime Number or N for stop searching.\n').upper()
        except:
            print('\nWrong input. Please, enter Y or N!\n')
            continue
    
    if user_inp == 'Y':
        return True
    elif user_inp == 'N':
        return False

# generate prime number
def def_pr(temp_num):
    for i in range(2, int(math.sqrt(temp_num)) + 1):
            if temp_num % i == 0:
                # not prime
                return False
    # is prime
    return True

# main function
def main():
    keep_asking = True
    temp_num = 2

    while keep_asking:
        user_input = inp_func()

        if user_input == False:
            print('\nThank you!')
            keep_asking = user_input
            break

        else:
            gen_num = True
            while gen_num:
                gen_pr = def_pr(temp_num)
                if gen_pr == True:
                    print(f"Next Prime Number is: {temp_num}")
                    temp_num += 1
                    gen_num = False
                    break
                else:
                    temp_num += 1

print(main())