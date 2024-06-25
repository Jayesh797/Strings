def removeOuterParentheses(string):
    op=0
    close=0
    start=0
    res=""
    for i in range(len(string)):
        if(string[i]==")"):
            close+=1
        else:
            op+=1
        if(close==op):
            res=res+string[start+1:i]
            start=i+1
    return res

sd=removeOuterParentheses("(()())(())(()(()))")
print(sd)