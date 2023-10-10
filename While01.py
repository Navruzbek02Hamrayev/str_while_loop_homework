def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    digit=0
    while i<len(s):
        if s[i].isdigit():
            digit+= 1
        i+= 1
    return "Number of digits:", digit
print(main("python 2022"))
print(main("e324xE"))