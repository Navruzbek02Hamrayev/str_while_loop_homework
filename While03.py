import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    punc=0
    while i<len(s):
        if s[i] in string.punctuation:
            punc+=1
        i+=1
    return "Number of punctuations:",punc
print(main("#hashtag@$"))
