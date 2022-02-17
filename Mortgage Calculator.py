import sys
import os
import datetime
from dateutil.relativedelta import relativedelta

print(sys.version)
print(sys.executable)

# purchase value input
def purchase_value_func():
    p_v_amount = ''
    while isinstance(p_v_amount, int) == False or p_v_amount < 1000 or p_v_amount > 500000:
        try:
            p_v_amount = int(input('\nPurchase cost (1000 - 500000):\n'))
        except:
            print('\nWrong input. Please, enter NUMBER 1000 - 500000!\n')
            continue
    else:
        return p_v_amount

# down payment amount input
def down_payment_func(purchase_value):
    d_p_amount = ''
    while isinstance(d_p_amount, int) == False or d_p_amount < purchase_value * 0.1 or d_p_amount > purchase_value * 0.9:
        try:
            d_p_amount = int(input(f'\nDown payment amount ({purchase_value * 0.1} - {purchase_value * 0.9}):\n'))
        except:
            print(f'\nWrong input. Please, enter NUMBER {purchase_value * 0.1} - {purchase_value * 0.9}!\n')
            continue
    else:
        return d_p_amount

# loan term input
def loan_term_func():
    l_term = ''
    while isinstance(l_term, int) == False or l_term < 6 or l_term > 360:
        try:
            l_term = int(input('\nLoan term (6 - 360):\n'))
        except:
            print('\nWrong input. Please, enter NUMBER 6 - 360!\n')
            continue
    else:
        return l_term

# mortgage calculator class
class M_Calc:

    interest_rate = 7
    interest_rate_month = (interest_rate / 12) * 0.01

    def __init__(self, purchase_value, down_payment, loan_term, todays_date) -> None:
        self.purchase_value = purchase_value
        self.down_payment = down_payment
        self.loan_amount = purchase_value - down_payment
        self.loan_term = loan_term
        self.todays_date = todays_date

    def user_param(self):
        f_w = open("demo_loan_file.txt", mode = 'w')
        
        print('\nParameters for calculation:', file = f_w)
        print(f"\tPurchase Value: {self.purchase_value}$", file = f_w)
        print(f"\tDown Payment: {self.down_payment}$ ({self.down_payment / self.purchase_value * 100 :.2f}%)", file = f_w)
        print(f"\tLoan Amount: {self.loan_amount}$", file = f_w)
        print(f"\tLoan Anual Rate: {self.interest_rate}%", file = f_w)
        print(f"\tLoan Term: {self.loan_term} months", file = f_w)
        print(f"\tStart Date: {self.todays_date}", file = f_w)

        f_w.close()

    def calc_result(self):
        years_c, month_c = divmod(self.loan_term, 12)
        loan_payoff = self.todays_date + relativedelta(years = years_c, months = month_c)
        count_down = self.loan_term
        total_payment = self.loan_amount * (self.interest_rate_month * ((1 + self.interest_rate_month) ** self.loan_term)) / (((1 + self.interest_rate_month) ** self.loan_term) - 1)
        f_a = open("demo_loan_file.txt", mode = 'a')
        print("\nLoan payment schedule: ", file = f_a)
        
        for month in range(1, self.loan_term + 1):
            interest = self.loan_amount * self.interest_rate_month
            principal = total_payment - interest
            self.loan_amount -= principal
            print(f"{month}  {total_payment:.2f}$  {principal:.2f}$  {interest:.2f}$  {self.loan_amount:.2f}$", file = f_a)
            count_down -= 1
        print(f"\tLoan pay-off date: {loan_payoff}", file = f_a)
        print(f"\tTotal payment per all period: {total_payment * self.loan_term:.2f}$", file = f_a)

        f_a.close()

    def __str__(self) -> str:
        pass

# main function
def main():
    purchase_value = purchase_value_func()               # user input $
    down_payment = down_payment_func(purchase_value)     # user input %
    loan_term = loan_term_func()                         # user input (month)
    todays_date = datetime.date.today()

    compute_res = M_Calc(purchase_value, down_payment, loan_term, todays_date)

    compute_res.user_param()
    compute_res.calc_result()

print(main())