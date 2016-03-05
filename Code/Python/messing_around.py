"""
Test program for Data Bootcamp course @ NYU Stern
"""
def pocket_change(P, N, D, Q):
    value = .01*P + .05*N + .1*D + .25*Q
    return value

change = pocket_change(1, 2, 3, 4)
print (change)
