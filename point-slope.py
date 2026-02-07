from fractions import Fraction

y1 = input("What is y1?: ")
x1 = input("What is x1?: ")
m = input("What is the slope? (no repeating fractions like 1/3 for now): ")
m = Fraction(m)
print(m)

y1 = float(y1)
x1 = float(x1)


x1 = x1 * -1

b = m * x1 + y1
x = m

if b < 0:
    print(f"Slope-Intercept form is: y={m}x{b}")
else:
    print(f"Slope-Intercept form is: y={m}x+{b}")
if m < 0:
    m = m * -1
    print(f"Standard form is: {m}x+y={b}")
else:
    print(f"Standard form is: -{m}x+y={b}")
