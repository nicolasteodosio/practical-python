# mortgage.py
#
# Exercise 1.7

if __name__ == '__main__':

    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    extra_payment_start_month = 60
    extra_payment_end_month = 108
    extra_payment = 1000
    months = 1
    while principal > 0:
        if months in [extra_payment_start_month, extra_payment_end_month]:
            payment = payment + extra_payment
        else:
            payment = 2684.11
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        months += 1

    print('Total paid', total_paid)
    print('Months ', months)
