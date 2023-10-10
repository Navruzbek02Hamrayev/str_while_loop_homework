def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    even=0
    while i<len(s):
        if int(s[i])%2==0:
            even+=1
        i+=1
    return even
print(main("56786543250"))
print(main("123456"))