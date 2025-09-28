class Emp:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.F = -1
        self.G = -1

def F(v):
    if v.F != -1:
        return v.F
    
    x = G(v)
    y = v.fun

    for u in v.emp:
        y += G(u)
    
    v.F = max(x,y)
    return v.F
    
def G(v):
    if v.G != -1:
        return v.G
    
    v.G = 0

    for u in v.emp:
        v.G += F(u)
    
    return v.G


a = Emp(50)
b = Emp(25); c = Emp(10); d = Emp(20); a.emp = [b,c,d]
e = Emp(10); f = Emp(30); b.emp = [e,f]
g = Emp(8); c.emp = [g]
h = Emp(18); i = Emp(1); j = Emp(1); d.emp = [h,i,j]

print(max(F(a), G(a)))

