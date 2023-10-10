def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    odd=0
    while i<len(s):
        if int(s[i])%2==1:
            odd+=int(s[i])
        i+=1
    return odd
print(main("589765"))
print(main("98421"))