class EcuacionSegundoGrado:
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    # Getter y Setter para a
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, valor):
        if isinstance(valor, (int, float)):
            self._a = valor
        else:
            raise ValueError("a debe ser un número")

    # Getter y Setter para b
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, valor):
        if isinstance(valor, (int, float)):
            self._b = valor
        else:
            raise ValueError("b debe ser un número")

    # Getter y Setter para c
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, valor):
        if isinstance(valor, (int, float)):
            self._c = valor
        else:
            raise ValueError("c debe ser un número")

    def solucionESG(self):
        d = math.pow(self.b, 2) - 4 * self.a * self.c
        if d >= 0:
            r1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        return None, None
