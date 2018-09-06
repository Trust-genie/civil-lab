# 2.0.3
""" The idea to slove for primes is not a new one
version 1.0.0, I used brute force. I ' divided the number by every number that
preceads it. I know its amatuer.
    init time= 1.4115116905247785e-05

    process time = 0.021677825450753425 '1 process'
                   0.9991394055995951   '1000 processes'
                   26.6820433043232   '25000 processes'
                
version 2.0.2
 a list of all primes so far and divide by those instead
This will hasten the search for non primes
    process time = 0.020763764698434804 units '1 process'
                   0.986094043463439100 units '1000 processes'
                   18.70246146252287000 units '25000 processes'


version 2.0.3 would be to keep calculations to the minimum when the length of
the primes in listed become to high, it would speed calculations by using half of them
    " The logic is that if the test passes up to half the list
      of primes in listed it passes it would pass the rest   "
In fact logically there is a threshold value at which all divisions would fail.
thats my next update

"""

import time

go = time.perf_counter()
listed = [2, ]
start= 3
stop= 100000
i = 0

condition= 'true'
while condition == 'true':
    for n in range(start, stop):
        for x in listed:
                if n % x == 0:
                    # then this is not of interest
                 break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
            i = i + 1
            listed.append(n)
    
            
    finish_line = time.perf_counter()
    elapsed_time = finish_line - go
                
    print (i + 1, 'primes')
    print ('It took ', elapsed_time, ' units')
    condition = 'false'
    

