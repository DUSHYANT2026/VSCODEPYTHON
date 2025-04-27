class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m
    
    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def random(self):
        return self.next() / self.m

# Example usage
if __name__ == "__main__":
    lcg = LCG(seed=12345)
    
    print("10 random numbers from LCG:")
    for _ in range(10):
        print(lcg.random())