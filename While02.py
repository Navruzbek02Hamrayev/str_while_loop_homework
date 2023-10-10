import string
def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    letters=0
    while i<len(s):
        if s[i].isalpha():
            letters+=1
        i+=1 
    return "Number of letters:",letters
print(main( "Python 2022"))
print(main("e324xE"))