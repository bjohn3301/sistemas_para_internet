from math import sqrt

a = 2
b = 7
c = 3.5
l = False
v = True

r1 = (b == a * c) and (l or v)
r2 = (b > a) or (b == a ** a)
r3 = (l and b // a >= c) or not (a <= c)
r4 = (not l) or (v and sqrt(a + b) >= c)
r5 = (b / a == c) or (b / a != c)
r6 = l or (b ** a <= c * 10 + a * b)

print(r1, r2, r3, r4, r5, r6)
