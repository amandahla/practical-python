# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment_set = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

months = 1
while principal > 0:
    payment = payment_set
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = payment_set + extra_payment

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if principal > 0:
        print(months,total_paid, principal)
    
    months += 1

print('Total paid', round(total_paid,1))
print('Months', months-1)
