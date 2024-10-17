import hashlib
class BloomFilter:
    def __init__(self,m,k, hashFun) -> None:
        self.m = m
        self.vector = [0]*m 
        self.k = k
        self.hashFun = hashFun
        self.data  = {}
        self.falsePositive = 0

    def insert(self,key,value):
        self.data[key] = value
        for i in range(self.k):
            # print(self.hashFun(key + str(i)) % self.m)
            self.vector[self.hashFun(key + str(i)) % self.m] = 1
    
    def contains(self,key):
        for i in range(self.k):
            if self.vector[self.hashFun(key + str(i)) % self.m] == 0:
                return False
        return True
    
    def get(self,key):
        if self.contains(key):
            try:
                return self.data[key]
            except:
                self.falsePositive += 1

def hashFun(x):
    h = hashlib.sha256(x.encode("utf-8"))
    return int(h.hexdigest(),base=16)
# print(hashFun("this is new"))
b = BloomFilter(100,10,hashFun)
b.insert("this is a test key", "this is a new value")
print(b.get("this is a"))
print(b.get("this is a new value"))
