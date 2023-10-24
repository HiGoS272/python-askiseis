sum = 0
max = -1
c1=0
c2=0
c3=0
xa=0
xb=0
xc=0
for i in range (3): 
    type1 = raw_input("Give The Type Of Container. A or B or C:")
    weight = int(input("Give The Weight Of Container:"))
    
    while weight<0 or weight>32500:
      weight = int(input("Give The Weight Of Container:"))

    sum = sum + weight
    
    if type1 == "A":
      c1 = c1 + 1
      xa = xa+weight
    elif type1 == "B":
  
      c2 = c2 + 1
      xb = xb + weight
      
    elif type1 == "C":
      
      c3 = c3 + 1
      xc = xc + weight
      
    if weight>max:
      max=weight
      max_t=type1
        
    

print sum
mo = sum / 3
print mo
print c1 , c2 , c3
print xa 
print xb
print xc

        
    
