from fractions import Fraction

point1 = input("What is the first point (seperate with a space) ex: 2 -4: ").split()
point2 = input("What is the second point (seperate with a space) ex: 2 -4: ").split()

point1 = list(map(int, point1))
point2 = list(map(int, point2))

x1, y1 = point1
x2, y2 = point2

m1 = y2 - y1
m2 = x2 - x1
m = Fraction(m1, m2)
b = y1 - (m * x1)

print(f"\nThe slope is {m}")
if b < 0:
    print(f"\nThe slope-intercept is y={m}x{b}")
else:
    print(f"\nThe slope-intercept is y={m}x+{b}")
print(f"\nStandard form is {m}x+y={b} ")