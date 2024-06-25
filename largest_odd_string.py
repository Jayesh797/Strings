def largest_odd(num):
    for i in range(len(num)-1,-1,-1):
        if(int(num[i])%2):
            return num[:i+1]
    return ""

sd=largest_odd("2346")
print(sd)