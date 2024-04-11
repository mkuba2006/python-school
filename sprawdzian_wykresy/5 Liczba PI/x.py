import random
T = 0
R = 0
ilosc = int(input("Podaj ilość: "))

for _ in range(ilosc):    
    a = random.uniform(0, 1)    
    b =  random.uniform(0, 1)    
    if a ** 2 + b ** 2 <= 1:        
        T += 1 # punkty na okregu    
    else:       
        R += 1 # punkty poza okregiem
        
print((4 * T) / (R + T))