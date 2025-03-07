# from pkg.poly import Poly 
# a = Poly(1,2,3)  #an, ...., a0 
# b = Poly(1,0,1,1,2,3)
# c = a+b 
# print(c) #Poly ( 1,0,1, 2,4,6)

class Poly():

    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)
    
    # def __add__(self, other):
    #     # Determine the length of the longer polynomial
    #     max_len = max(len(self.coeffs), len(other.coeffs))
        
    #     # Extend both polynomials to the length of the longer one
    #     self.extend([0] * (max_len - len(self)))
    #     other.extend([0] * (max_len - len(other)))
        
    #     # Add corresponding coefficients
    #     result = [self[i] + other[i] for i in range(max_len)]
        
    #     return result


    def __add__(self, other):
        # Pad the shorter list with zeros at the front
        diff = len(other.coeffs) - len(self.coeffs)
        a_padded = [0] * max(0, diff) + self.coeffs
        b_padded = [0] * max(0, -diff) + other.coeffs

        return Poly(*[x + y for x, y in zip(a_padded, b_padded)])

    def __repr__(self):
        return f"Poly{tuple(self.coeffs)}"

