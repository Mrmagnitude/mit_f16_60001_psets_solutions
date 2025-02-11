# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:31:33 2025

@author: Mr_Magnitude
"""
 #declaring all variables
annual_salary = float(input('annual salary : '))
portion_saved =float(input('portion to be saved : '))
total_cost = float(input('cost of dream house : '))
current_savings = 0
interest_rate = 0.04/12

monthly_salary = annual_salary/12
down_payment = total_cost*0.25
month =0

#define a function to invest his savings on a  monthly basis

def invest(save):
    amount = save*interest_rate
    return amount

#get the percentage of the semi annual raise
semi_annual_raise = float(input('enter raise % : '))


 # define a function to raise the salary by the percentage given
def semi_raise(salary):
     return salary*semi_annual_raise


while current_savings<down_payment:
    current_savings+= (monthly_salary*portion_saved + invest(current_savings))
    month+= 1
    if month%6 ==0 :
        monthly_salary +=semi_raise(monthly_salary)

print(month)