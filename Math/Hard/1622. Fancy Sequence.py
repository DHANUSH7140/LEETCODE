class Fancy:
    MOD = (10**9) + 7
    def __init__(self):
        self.v = []
        self.mul = 1
        self.a = 0

    def append(self, val: int) -> None:
        i = pow(self.mul, self.MOD - 2, self.MOD) % self.MOD
        val = (val - self.a) % self.MOD
        val = (val * i) % self.MOD
        self.v.append(val)
    def addAll(self, inc: int) -> None:
        self.a = (self.a + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.a = (self.a * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        return (self.v[idx] * self.mul + self.a) % self.MOD if idx < len(self.v) else -1


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
