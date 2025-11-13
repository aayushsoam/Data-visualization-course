import math

# ==========================
# Module: shape.py
# Contains classes for:
#   - Cylinder
#   - Cone
#   - Cube
#   - Cuboid
#   - Sphere
# Each class includes:
#   - csa() → Curved Surface Area
#   - tsa() → Total Surface Area
#   - vol() → Volume
# ==========================


# ---------- CYLINDER ----------
class cylinder:
    def __init__(self, r, h):                           # Constructor to initialize radius (r) and height (h)
        self.r, self.h = r, h

    def csa(self): return 2 * math.pi * self.r * self.h # Curved Surface Area = 2πrh

    def tsa(self): return 2 * math.pi * self.r * (self.h + self.r)  # Total Surface Area = 2πr(h + r)

    def vol(self): return math.pi * self.r**2 * self.h  # Volume = πr²h


# ---------- CONE ----------
class cone:
    def __init__(self, r, h):                           # Constructor to initialize radius (r) and height (h)
        self.r, self.h = r, h

    def l(self): return math.sqrt(self.r**2 + self.h**2)  # Slant height = √(r² + h²)

    def csa(self): return math.pi * self.r * self.l()     # Curved Surface Area = πrl

    def tsa(self): return math.pi * self.r * (self.l() + self.r)  # Total Surface Area = πr(r + l)

    def vol(self): return (1/3) * math.pi * self.r**2 * self.h     # Volume = (1/3)πr²h


# ---------- CUBE ----------
class cube:
    def __init__(self, a):                              # Constructor to initialize side length (a)
        self.a = a

    def csa(self): return 4 * self.a**2                 # Curved Surface Area = 4a²

    def tsa(self): return 6 * self.a**2                 # Total Surface Area = 6a²

    def vol(self): return self.a**3                     # Volume = a³


# ---------- CUBOID ----------
class cuboid:
    def __init__(self, h, l, b):                        # Constructor to initialize height (h), length (l), breadth (b)
        self.h, self.l, self.b = h, l, b

    def csa(self): return 2 * self.h * (self.l + self.b)  # Curved Surface Area = 2h(l + b)

    def tsa(self): return 2 * (self.l*self.b + self.b*self.h + self.h*self.l)  # Total Surface Area = 2(lb + bh + hl)

    def vol(self): return self.h * self.l * self.b        # Volume = l × b × h


# ---------- SPHERE ----------
class sphere:
    def __init__(self, r):                              # Constructor to initialize radius (r)
        self.r = r

    def csa(self): return 4 * math.pi * self.r**2        # Curved Surface Area = 4πr²

    def tsa(self): return 4 * math.pi * self.r**2        # Total Surface Area = 4πr² (same as CSA for sphere)

    def vol(self): return (4/3) * math.pi * self.r**3    # Volume = (4/3)πr³
