s = "Nikhil"

def rev_str(s):
    res = ""
    for i in s:
        res = i+res
    return res

print(rev_str(s))

# Using Recursion


def rev_rec(s):
    if len(s)==0:
        return s
    else:
        return rev_rec(s[1:])+s[0]

print(rev_rec(s))