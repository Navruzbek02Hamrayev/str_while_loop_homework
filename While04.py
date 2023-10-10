def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    upper=0
    while i<len(s):
        if s[i].islower():
            upper+=1
        i+=1
    return "Number of uppercase letters:",upper
print(main("CodeschoolUz"))