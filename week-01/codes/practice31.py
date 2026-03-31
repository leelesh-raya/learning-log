spam="aa  b"

def compressString(s):
    y=''
    x=''
    for i in range(len(s)):
        x+=s[i]
        if i==len(s)-1:
            if s[i]!=s[i-1]:
                y+=s[i]+'1'
            else:
                y+=s[i]+str(len(x))

                
        elif s[i]!=s[i+1]:
            y+=s[i]+str(len(x))
            x=''
    return y

               

            


print(compressString(spam))

            
        
