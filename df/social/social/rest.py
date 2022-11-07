#var str1=userinput
#find the length of last word of str1



def length(a):
   
    b=0
    x =a.strip()
    for i in range(len(x)):
        if x[i] == "":
            b = 0
            
        else:
            b +=1
            
    return b

if __name__ == "__main__":
    input = "fly me   to   the moon"
    print(length(input))

def leng(s):
    count =0;
    leng = len(s)-1;
    while(leng !=0):
        if (s[leng]== ''):
            return count;
        else:
            count +=1;
        leng -=1;
    return count;

sd = "fly me   to   the moon"
print(leng(sd))


s = "   fly me   to   the moon  "
#s = "Hello World"
print(len(s.strip().split()[-1]))