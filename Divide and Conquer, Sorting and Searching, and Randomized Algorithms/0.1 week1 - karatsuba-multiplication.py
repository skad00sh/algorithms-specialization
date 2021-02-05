def karatsuba(x, y):
    """
    Input: two n-digit positive integers x and y. 
    Output: the product x·y. 
    Assumption: n is a power of 2. (NOT assuming this)

    if n =1  then                   // base case
        compute x·y in one step and return the result
    else 
        a,b := ﬁrst and second halves of x 
        c,d := ﬁrst and second halves of y 
        compute p := a + b and q := c + d using grade-school addition 
        recursively compute ac := a·c, bd := b·d, and pq := p·q 
        compute adbc := pqacbd using grade-school addition 
        compute 10n ·ac + 10n/2 ·adbc + bd using grade-school addition and return the result
    """

    str_x = str(x)
    str_y = str(y)
    if len(str_x) == 1 or len(str_y) == 1:
        return x*y
    else:
        n = max(len(str_x), len(str_y))
        n_half = int(n / 2)
        
        a, b = x // 10**n_half, x % 10**n_half
        c, d = y // 10**n_half, y % 10**n_half
        
        p = a + b
        q = c + d
    
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)
        
        adbc = pq - ac - bd
        
        return 10**(2*n_half) * ac + 10**n_half * adbc + bd
