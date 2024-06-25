def isAnagram(s, t):
        mapS,mapT={},{}
        if(len(s)==len(t)):
            for c1,c2 in zip(s,t):
                if(c1 in mapS):
                    mapS[c1]+=1
                else:
                    mapS[c1]=1
                if(c2 in mapT):
                    mapT[c2]+=1
                else:
                    mapT[c2]=1
            if(mapS==mapT):
                return True
        return False

sd=isAnagram("anagram","nagaram")
print(sd)