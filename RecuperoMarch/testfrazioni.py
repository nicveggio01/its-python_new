
from frazioni import Frazione

l= [ 
    Frazione(1,2), 
    Frazione(2,4), 
    Frazione(3,5),  
    Frazione(6,9),  
    Frazione(4,7),  
    Frazione(24,36),  
    Frazione(12,36),  
    Frazione(40,60),  
    Frazione(5,11), 
    Frazione(10,45), 
    Frazione(42,78), 
    Frazione(9,15)
    ]

l_s= Frazione.semplifica(l)

f= Frazione(1,1)
f.fractionCompare(l, l_s)


