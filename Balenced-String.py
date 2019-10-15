#This is to check if in a string the brackets are opened and closed in a right order. 

br = [['(', ')'], ['{', '}'], ['[', ']']]

stk = []
v = False

s = list(input("Enter the string :"))

def isopen(ch) :
    
    for b in br :
        if b[0] == ch :
            return True
        
    return False    
        
def check(ch) :
    for b in br :
        if b[0] == stk[0] :
            sind = br.index(b)
        if b[1] == ch:
            cind = br.index(b)
            
    if(sind == cind):
        return True
    else :
        return False
        

for i in s:
    if(isopen(i)) :
        stk.insert(0, i)
    else :
        if len(stk) == 0 :
            break
            
        if check(i) :
            stk.pop(0)
        
            
if len(stk) == 0 :
    v = True

if v :
    print("String is balenced")
else :
     print("String is not balanced")
