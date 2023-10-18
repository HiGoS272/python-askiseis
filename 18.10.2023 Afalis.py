sum = 0
c = 0
def my_function(t):
    if time < = 40:
        pay = t * 5

    elif  time < = 50:
        pay = 40*5+( t-40) * 7
    else:
        40 * 5 + (50 - 40) * 7 + ( t - 50 ) * 9

    return pay
        

for i in range (48):
    employee = raw_input("Give A Name of employee:")
    time = input("Give the time of work:")

    

    
    pay = my_function(time)
    sum = pay + sum
    print employee , pay

    if pay > 700:
        c = c + 1
pososto = ( c / 48.0 ) * 100
print pososto
print c
print sum
        
        
    
