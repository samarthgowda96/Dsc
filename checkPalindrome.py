inputString= "naman"
def checkPalindrome(str):
 

    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 


ans = checkPalindrome(inputString)
 
if (ans):
    print("True")
else:
    print("False")

