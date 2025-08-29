# Expt 3.6 – Method Overloading Simulation
class MathOps:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = MathOps()
print(obj.add(2))
print(obj.add(2, 3))
print(obj.add(2, 3, 4))
