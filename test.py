import math as m


for x in range(10):
    exp = (m.fabs(x-1 + 300*2**((x-1)/4)))/4
    print(int(exp))
