

#m1 = a1 - f(a1)*(b1 - a1)/(f(b1) - f(a1))

def secantMethod(a,b,N):
    a1 = a
    b1 = b
    for n in range(1,N+1):

        m1 = a1 - F(a1)*(b1 - a1)/(F(b1) - F(a1))

        fm1 = F(m1)

        if F(a1)*fm1 < 0:
            a1 = a1
            b1 = m1


        elif F(b1)*fm1 < 0:
            a1 = m1
            b1 = b1



        elif fm1 == 0:
            return m1, n, True


        else:
            return m1, n, False
    return a1 - F(a1)*(b1 - a1)/(F(b1) - F(a1)), n, False