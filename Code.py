import random
import numpy as np
from numpy import ndarray

num_of_customers = input("enter the number of customers:")

a = 0.2
b = 0.125

ln = np.log

num_of_customers = int(num_of_customers)

IAT = ndarray((num_of_customers,),int)
ST = ndarray((num_of_customers,),int)
AT = ndarray((num_of_customers,),int)
SS = ndarray((num_of_customers,),int)
SE = ndarray((num_of_customers,),int)
W = ndarray((num_of_customers,),int)
Q = ndarray((num_of_customers,),int)

for it in range(num_of_customers):

  IAT[it] = -ln(1-random.random())//a
  ST[it] = -ln(1-random.random())//b
  

def myfunc(I,S,NUM_OF_CUSTOMERS):
    print("customer  IAT  ST   AT   SS   SE    WT")
    for it in range(NUM_OF_CUSTOMERS):
        if it == 0:
            AT[0] = I[0]
        else:
            AT[it] = I[it]+AT[it-1]
         
        
    for it in range(NUM_OF_CUSTOMERS):
         if it==0:
             SS[0] = AT[0]
             SE[0] = SS[0] + S[0]  
         elif AT[it]>= SE[it-1]:
             SS[it] = AT[it]
             SE[it] = SS[it] + S[it]
            
         else:
            SS[it] = SE[it-1]
            SE[it] = SS[it] + S[it]
    
    for it in range(NUM_OF_CUSTOMERS):
        if it==0:
            W[0] = 0
        else:
            W[it] = SS[it] - AT[it]
            
            
        
        
    for it in range(NUM_OF_CUSTOMERS):
        print(f"c{it+1}","       ",IAT[it],"  ",ST[it]," ",AT[it],"   ",SS[it]," ",SE[it]," ",W[it])
myfunc(IAT,ST,num_of_customers)