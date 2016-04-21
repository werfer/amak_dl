
import math

def baby_step_giant_step(p, g, beta):
    m = math.ceil( math.sqrt(p-1) )
    table = { }

    # babysteps
    for j in range(0, m):
        t = pow(g, j) % p
        table[t] = j

    print("table:", table);

    # giantsteps
    t = beta
    for i in range(0, m):
        print("t:", t)
        if t in table:
            return i*m + table[t];
        else:
            t = (t * pow(g, p-1-m)) % p

    return -1

dl = baby_step_giant_step(37, 5, 4)
print("x =", dl)

