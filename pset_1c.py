#declaring all variables

annual_salary = int(input('Enter Annual salary : '))
cost_of_home = 1000000
down_payment = cost_of_home*0.25
low = 0
high = 10000
search = 0
monthly_salary = annual_salary/12

# defining a function to get the mid value of the search space

def get_saving_rate():
    global high , low
    rate = (high +low)//2
    return rate

"""defining a function to use the mid value of the search space 
    and return the number of months it will take along with the 
    amount in the current saving account """
    
def get_month(saving_rate):
    global annual_salary ,down_payment
    mon_salary =monthly_salary
    current_saving = 0
    month =0
    while current_saving < down_payment:
        current_saving += mon_salary*saving_rate + current_saving*(0.04/12)
        month +=1
        if month % 6 ==0:
            mon_salary += (mon_salary*0.07)
    return (month ,current_saving)

""" initialize the get_saving_rate function and dividing by 10000 
    to get a four decimal place value"""
    
saving_rate =get_saving_rate()/10000

"""initializing the functions to get both the months and the amount
     in the saving account """

month , current_saving = get_month(saving_rate)
month= month
current_saving= current_saving

"""checking the months and the amount save, the months 
    has to be 36 and the difference between the amount and the downpayment
    must be less than 100 """
    
while month != 36 or current_saving-down_payment >=100 :
    
    if month ==36 and current_saving-down_payment >=100:
        high = saving_rate*10000
        
    elif annual_salary *3 < down_payment:
        print('it is not possible to pay a downpayment in three years')
        break
    elif month < 36:
        high = saving_rate*10000
    else:
        low = saving_rate*10000
    search +=1
    saving_rate = get_saving_rate()/10000
    month,current_saving =get_month(get_saving_rate()/10000)
    month = month
    current_saving =current_saving

"""just an extra line to avoid printing a 0 search value 
    if it is not possible to pay a downpayment """
    
if search>1:
    print('best saving rate : ' ,get_saving_rate()/10000)
    print('number of searches : ' , search)
else:
    pass
   
