# Expt 3.7 – Operator Overloading
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.real*other.imag + self.imag*other.real)

c1 = Complex(2, 3)
c2 = Complex(1, 4)
result = c1 * c2
print(f"Result: {result.real}+{result.imag}i")
