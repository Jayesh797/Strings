def romanToInt(self, s):
        lookup={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        n=len(s)
        i=n-1
        output=0
        while(i>=0):
            if(i<n-1 and lookup[s[i]]<lookup[s[i+1]]):
                output-=lookup[s[i]]