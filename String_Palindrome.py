# Check if a string is palindrome or not


s = "saippuakivikauppias"

def palindrome(s):
    if len(s)<2:
        return True
    i = 0
    j = len(s)-1
    while(j>=i):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

print(palindrome(s))
