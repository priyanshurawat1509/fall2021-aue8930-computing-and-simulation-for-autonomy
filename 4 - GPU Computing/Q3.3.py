import math
import time
import threading
lock = threading.Lock()
count = 1000000
no_threads = 10
Calculations = count/no_threads
result = 0
prime_numbers = []
mythreads=[]


def is_Prime(n):
   if n == 1:
      return False
   if n == 2:
      return True
   if n > 2 and n % 2 ==0:
      return False

   max_divisor = math.floor(math.sqrt(n))
   for d in range(3, 1 + max_divisor,2):
     if n % d ==0:
        return False
   return True
 

def summation_prime_numbers(k,Calculations):
    global result
    
    prime_numbers = [x for x in range(int(((k-1)*Calculations))+1, int(k*Calculations)+1) if is_Prime(x) ==True]
    lock.acquire()
    result+=sum(prime_numbers)
    lock.release()
    
 
start_time = time.time()
for i in range(1,no_threads+1):
        x = threading.Thread(target=summation_prime_numbers, args=(i,Calculations))
        x.start()
        mythreads.append(x)
for j in range(0,no_threads):
        mythreads[j].join()


print(result)

print("--- %s seconds ---" % (time.time() - start_time))
