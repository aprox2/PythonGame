import math as m
agl = 10


print(1.25/(1+m.exp(-(0.07 * agl - 2))) - 0.2)

