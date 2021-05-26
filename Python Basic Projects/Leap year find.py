#print("Leap year finding")

def is_leap(year):
    if year%4==0:
        if year%100!=0:
            return True
        else:
            if year%400==0:
                return True
            else:
                return False
    else:
        return False
                
            
        
    


year = int(input())
print(is_leap(year))
    
"""for i in range(1990,2023):
    if i%4==0 and i%100!=0 or  i%400==0:
        print(i,"leap year")
    else:
        print(i,"Not leap year")"""
    
    
