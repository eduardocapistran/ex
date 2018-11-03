if __name__ == '__main__':
    s = raw_input()
    an, a, d, l, u = (0,0,0,0,0)

    for c in s:
        if c.isalnum():
            an = an+1
        if c.isalpha():
            a += 1
        if c.isdigit():
            d += 1
        if c.islower():
            l += 1
        if c.isupper():
            u += 1
    print an>0
    print a>0
    print d>0
    print l>0
    print u>0
