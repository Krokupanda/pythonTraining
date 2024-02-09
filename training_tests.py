a = int(input())
b = int(input())
c = int(input())

if 0 < a:
    pos_a = a
else:
    pos_a = 0    
if 0 < b:
    pos_b = b
else:
    pos_b = 0
if 0 < c:
    pos_c = c
else:
    pos_c = 0
print(pos_a + pos_b + pos_c)