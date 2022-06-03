def baskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Raiz fora dos reais")
    else:
        x1 = (-b - delta**1/2)/(2*a)
        x2 = (-b + delta**1/2)/(2*a)
        return {"x1": x1, "x2": x2}

variavel = 10