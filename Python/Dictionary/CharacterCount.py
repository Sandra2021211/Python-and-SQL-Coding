# Input: "banana"

# Output:
# {
# 'b':1,
# 'a':3,
# 'n':2
# }

# Code:

def character_count(s):
    count={}

    for ch in s:
        count[ch]=count.get(ch,0)+1
    
    return count