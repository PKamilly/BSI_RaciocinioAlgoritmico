TOTAL DE 06 EXERCICIOS
===========================
EXERCICIO 01
A = 10
B = 20
C = 35
D = 15.0
E = 3.0

S1A = A + C * 2 - B / A - (A + B)
S1A = 10 + 35 * 2 - 20 / 10 - (10 + 20)
S1A = 10 + 70 - 2 - (30)
S1A = 80 - 32
S1A = 112

S1B = C * 2 + A / B - (B + A)
S1B = 35 * 2 + 10 / 20 - (20 + 10)
S1B = 70 + 0.5 - (30)
S1B = 40.5
# 

S1C = A + C * 2 - (B / A + A + B)
S1C = 10 + 35 * 2 - (20 / 10 + 10 + 20)
S1C = 10 + 70 - (32)
S1C = 80 - 32
S1C = 58
# ERRADO

S1D = A + C * 2 - B / A - (A + B)
S1D = 10 + 35 * 2 - 20 / 10 - (10 + 20)
S1D = 10 + 70 - 0.5 - (30)
S1D = 80 - 30.5
S1D = 49.5
# ERRADO

S1E = C * 2 + B / A - (A + B)
S1E = 35 * 2 + 20 / 10 - (10 + 20)
S1E = 70 + 2 - (30)
S1E = 42
# CORRETO

S1F = C * 2 + A / B - (A + B)
S1F = 35 * 2 + 10 / 20 - (10 + 20)
S1F = 70 + 0.5 - (30)
S1F = 40.5
# CORRETO

S1G = A + C * 2 - B / A - (A + B)
S1G = 10 + 35 * 2 - 20 / 10 - (10 + 20)
S1G = 10 + 70 - 2 - (30)
S1G = 82 - (30)
S1G = 52
# ERRADO

S1H = C * 2 + B / A - (A + B)
S1H = 35 * 2 + 20 / 10 - (10 + 20)
S1H = 70 + 2 - (30)
S1H = 42
# CORRETO

S1I = C * 2 + B / A - (A + B) * 2 ** E
S1I = 35 * 2 + 20 / 10 - (10 + 20) * 2 ** 3.0
S1I = 70 + 2 - (30) * 8
S1I = 72 - 240
S1I = - 168
# CORRETO

S1J = A + C * 2 - (B / A + A + B)
S1J = 10 + 35 * 2 - (20 / 10 + 10 + 20)
S1J = 10 + 70 - (2 + 30)
S1J = 80 - (32)
S1J = 48
# CORRETO

S1K = A + C * 2 - B / A - (A + B)
S1K = 10 + 35 * 2 - 20 / 10 - (10 + 20)
S1K = 10 + 70 - 2 - (30)
S1K = 80 - 2 - (30)
S1K = 78 - (30)
S1K = 48
# CORRETO

===========================
EXERCICIO 02

AND
A | B | S
V | V | ?
S = V
# CORRETO

A | B | S
V | F | ?
S = F
# CORRETO

A | B | S
F | V | ?
S = F
# CORRETO

A | B | S
F | F | ?
S = F
# CORRETO
=========
OR
A | B | S
V | V | ?
S = V
# CORRETO

A | B | S
V | F | ?
S = V
# CORRETO

A | B | S
F | V | ?
S = V
# CORRETO

A | B | S
F | F | ?
S = F
# CORRETO
=========
NOT
A | S
V | ?
S = F
# CORRETO
=========
A | S
F | ?
S = V
# CORRETO
===========================
EXERCICIO 03
A = V
B = F
C = F

S3A= A or B or C
S3A= V or F or F
S3A= V
# CORRETO

S3B= not A and B or C
S3B= not V and F or F
S3B= F
# CORRETO

S3C= not(A and B) and C
S3C= not(V and F) and F
S3C= (F and V) and F
S3C= F and F
S3C= V
# ERRADO

S3D= not(not A or not C)
S3D= not(not V or not F)
S3D= not(F or V)
S3D= V or F
S3D= V
# ERRADO

===========================
EXERCICIO 04
A = 10
B = 20
C = 30

S4A= A > B
S4A= 10 > 20
S4A= F

S4B= (B * 2 + A) >= B + C
S4B= (20 * 2 + 10) >= 20 + 30
S4B= (40 + 10) >= 50
S4B= (50) >= 50
S4B= V

S4C= A + B != C
S4C= 10 + 20 != 30
S4C= 30 != 30
S4C= F

S4D= B <= C
S4D= 20 <= 30
S4D= V

S4E= A * 2 == B
S4E= 10 * 2 == 20
S4E= 20 == 20
S4E= V

S4F= (C - A) / 2 >= B
S4F= (30 - 10) / 2 >= 20
S4F= (20) / 2 >= 20
S4F= 10 >= 20
S4F= F

S4G= (A ** 2) + (B ** 2) > (C ** 2)
S4G= (10 ** 2) + (20 ** 2) > (30 ** 2)
S4G= (100) + (400) > (900)
S4G= 500 > 900
S4G= F

S4H= (A + B) * (A - B) != (C ** 2)
S4H= (10 + 20) * (10 - 20) != (30 ** 2)
S4H= (30) * (10) != (900)
S4H= 300 != 900
S4H= V

S4I= (A * B) + (A * C) >= (B * C)
S4I= (10 * 20) + (10 * 30) >= (20 * 30)
S4I= (200) + (300) >= (600)
S4I= 500 >= 600
S4I= F

S4J= (A ** 3) + (B ** 3) == (C ** 3)
S4J= (10 ** 3) + (20 ** 3) == (30 ** 3)
S4J= (1000) + (8000) == (27000)
S4J= 9000 == 27000
S4J= F

S4K= (A ** 2) + (B ** 2) - (C ** 2) >= 0
S4K= (10 ** 2) + (20 ** 2) - (30 ** 2) >= 0
S4K= (100) + (400) - (900) >= 0
S4K= 500 - 900 >= 0
S4K= -400 >= 0
S4K= F

S4L= (A + B) * (B + C) > (A * C)
S4L= (10 + 20) * (20 + 30) > (10 * 30)
S4L= (30) * (50) > (300)
S4L= 1500 > 300
S4L= V

S4M= (A ** 2) + (B ** 2) + (C ** 2) != (A * B * C)
S4M= (10 ** 2) + (20 ** 2) + (30 ** 2) != (10 * 20 * 30)
S4M= (100) + (400) + (900) != (6000)
S4M= 1400 != 6000
S4M= V
# CORRETO

S4N= (A * B * C) > (A + B + C)
S4N= (10 * 20 * 30) > (10 + 20 + 30)
S4N= (6000) > (60)
S4N= V

S4O= (A ** 2) * (B ** 2) != (C ** 4)
S4O= (10 ** 2) * (20 ** 2) != (30 ** 4)
S4O= (100) * (400) != (810000)
S4O= 40000 != 810000
S4O= V

S4P= (A * B * C) % 2 == 0
S4P= (10 * 20 * 30) % 2 == 0
S4P= (7000) % 2 == 0
S4P= 0 == 0
S4P= V
# CORRETO

===========================
EXERCICIO 05