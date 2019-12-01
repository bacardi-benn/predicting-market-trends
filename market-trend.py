#https://www.expunctis.com/2019/03/07/Not-so-random.html
import autoit
import pandas
import time
import math

#autoit.win_activate("How random can you be? | Lineae ex punctis")

#move mouse so that it hovers over the interactive plot
autoit.mouse_move(920,700)
autoit.mouse_click() #click the interactive plot

spdata = pandas.read_csv(r'C:\Users\bmort\source\data\^GSPC2.csv')
#if the day n's close was lower than the previous day's then...
for i in range(1,spdata['Close'].size):
    if spdata['Close'][i] < spdata['Close'][i - 1]:
        autoit.send("{LEFT}") 
    else:
        autoit.send("{RIGHT}") 


#probably would be better to use autoit.send(the-F5-key)
autoit.mouse_move(85,60) #hover over refresh button
autoit.mouse_click() #click the the button
time.sleep(3) #pause for 3 seconds to allow the screen to refresh

autoit.mouse_move(920,770)
autoit.mouse_click()

#if the opening price was lower than the closing
for i in range(0,spdata['Close'].size):
    if spdata['Open'][i] < spdata['Close'][i]:
        autoit.send("{LEFT}") 
    else:
        autoit.send("{RIGHT}")




def modexp(x, y, p):
    remainder = 1;

    #Update x if it is greater than or equal to p
    x = x % p

    while (y > 0):
        #If y is odd, multiply x with result
        if ((y & 1) == 1):
            remainder = (remainder * x) % p
	#y must be even now
        y = y >> 1
        x = (x * x) % p
    return remainder

def getS_j(n, j):
    sum = 0;

    for k in range(n):
        sum = sum + modexp(16, n - k, (8 * k + j)) / (8 * k + j)
        sum = sum - int(sum)

    eps = 1e-17;

    for k in range(n, n +100):
        quotient = (16.0**(n - k)) / (8 * k + j)
        if (quotient < eps):
            break
        sum = sum + quotient
        sum = sum - int(sum)
	
    return sum


def getnthpi(n):
    number = 4 * getS_j(n, 1) - 2 * getS_j(n, 4) - getS_j(n, 5) - getS_j(n, 6)
    fractionalpart = number - int(number)
    fractionalpart = fractionalpart + 1.0
    return fractionalpart


	#/* last digit displayed is not accurate */
print(getnthpi(0))
print(getnthpi(1000000))

autoit.mouse_move(85,60)
autoit.mouse_click()
time.sleep(3)

autoit.mouse_move(920,770)
autoit.mouse_click()

digits_of_pi = 0
for i in range(0,100, 10):
    digits_of_pi = getnthpi(i)
    pi_temp = digits_of_pi*10
    for position in range(0, 11):
        if int(math.modf(pi_temp)[1]) % 2 == 0:
            autoit.send("{LEFT}") 
        else:
            autoit.send("{RIGHT}")
        pi_temp = 10*math.modf(pi_temp)[0]



