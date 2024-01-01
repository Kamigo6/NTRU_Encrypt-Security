import poly


class Ntru:
    N, p, q = None, None, None
    f, g, h = None, None, None
    f_p, f_q, D = None, None, None

    def __init__(self, N_new, p_new, q_new):
        self.N = N_new
        self.p = p_new
        self.q = q_new
        D = [0] * (self.N + 1)
        D[0] = -1
        D[self.N] = 1
        self.D = D  # x^N - 1

    def genPublicKey(self, f_new, g_new):
        self.f = f_new
        self.g = g_new
        # s_f*f + t_f*(x^N - 1) = gcd_f = 1 
        # => s_f*f = 1 in ring Z[x]/x^N - 1
        [gcd_f, s_f, t_f] = poly.extEuclidPoly(self.f, self.D) 
        
        self.f_p = poly.modPoly(s_f, self.p)
        print("Inverse of f modulo p: ", self.f_p)
        self.f_q = poly.modPoly(s_f, self.q)
        print("Inverse of f modulo q: ", self.f_q)
        self.h = self.reModulo(poly.multPoly(self.f_q*self.p, self.g), self.D, self.q)
        if not self.runTests():
            print("Failed!")
            quit()

    def getPublicKey(self):
        return self.h

    def setPublicKey(self, public_key):
        self.h = public_key

    def encrypt(self, message, randPol):
        if self.h != None:
            e_tilda = poly.addPoly(poly.multPoly(self.h, randPol), message)
            e = self.reModulo(e_tilda, self.D, self.q)
            return e
        else:
            print("Cannot Encrypt Message Public Key is not set!")
            print("Cannot Set Public Key manually or Generate it")

    def decrypt(self, encryptedMessage):
        a = self.reModulo(poly.multPoly(self.f,encryptedMessage), self.D, self.q)
        # print("a = ", a)
        b = self.reModulo(poly.cenPoly(a, self.q), self.D, self.p)
        # print("b = ", b)
        c = self.reModulo(poly.multPoly(self.f_p, b), self.D, self.p)
        # print("c = ", c)
        return a, b, c

    def reModulo(self, num, div, modby):
        [_, remain] = poly.divPoly(num, div)
        return poly.modPoly(remain, modby)

    def runTests(self):
        # Condition
        return True
