def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    odd=0
    while i<len(s):
        if int(s[i])%2==1:
            odd+=1
        i+=1
    return "Number of odd digits:",odd
print(main("1567534"))
print(main("3489769"))