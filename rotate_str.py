def rotateString(s, goal):
        if len(s)==len(goal) and s in goal+goal:
            return True
        return False

sd=rotateString("abcde","deabc")
print(sd)