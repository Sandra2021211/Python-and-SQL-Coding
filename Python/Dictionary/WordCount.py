# Input: 

# text = "data engineering data python python sql"

# Output:

# {
# 'data':2,
# 'engineering':1,
# 'python':2,
# 'sql':1
# }

# Code: 

def word_count(text):
    count={}

    words=text.split()

    for word in words:

        count[word]=count.get(word,0)+1

    return count