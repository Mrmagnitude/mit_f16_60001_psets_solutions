# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:31:33 2025

@author: Mr_Magnitude
"""

#pset 1a

#declaring all variables
annual_salary = float(input('annual salary : '))
portion_saved =float(input('portion to be saved : '))
total_cost = float(input('cost of dream house : '))
current_savings = 0 
interest_rate = 0.04/12
monthly_salary = annual_salary/12
down_payment = total_cost*0.25
amount_save =monthly_salary*portion_saved
month =0

#define a function to invest his savings on a  monthly basis

def invest(save):
    amount = save*interest_rate
    return amount
#initializing a while loop to check and count the number of months needed to achieve the aim
while current_savings<down_payment:
    current_savings+= (amount_save + invest(current_savings))
    month+= 1
#printing the months to the console
print(month)
