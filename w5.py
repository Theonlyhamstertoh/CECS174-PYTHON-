x, y = 3, 5
b1, b2, b3, b4 = True, False, x == 3, y < 3
print("b3 ", b3)
print("b4 ", b4)
print("not b1  ", not b1)
print("not b2  ", not b2)
print("not b3  ", not b3)
print("not b4 ", not b4)
print("b1 and b2  ", b1 and b2)
print("b1 or b2  ", b1 or b2)
print("b1 and b3  ", b1 and b3)
print("b1 or b3  ", b1 or b3)
print("b1 and b4  ", b1 and b4)
print("b1 or b4  ", b1 or b4)
print("b2 and b3 ", b2 and b3)
print("b2 or b3 ", b2 or b3)
print("b1 and b2 ", b1 and b2)
print("b1 or b2 and b3  ", b1 or b2 and b3)
print("b1 and b2 and b3  ", b1 and b2 and b3)

print("s.	b1 or b2 or b3 ", b1 or b2 or b3)
print("t.	not b1 and b2 and b3  ", not b1 and b2 and b3)
print("u.	not b1 or b2 or b3 ", not b1 or b2 or b3)
print("v.	not (b1 and b2 and b3)  ", not (b1 and b2 and b3))
print("w.	not (b1 or b2 or b3)  ", not (b1 or b2 or b3))
print("x.	not b1and not b2 and not b3 ", not b1 and not b2 and not b3)
print("y.	not b1 or not b2 or not b3 ", not b1 or not b2 or not b3)
print("z.	not (not b1 and not b2 and not b3)  ",
      not (not b1 and not b2 and not b3))
print("aa.	not (not b1 or not b2 or not b3)  ",
      not (not b1 or not b2 or not b3))
