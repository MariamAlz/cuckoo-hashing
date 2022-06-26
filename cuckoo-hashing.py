import random
import math

def getprime(num):  #returns a prime number greater than num
    prime = True
    while True:
        prime = True
        n = random.randint(num, num*2)
        for x in range(2, int(math.sqrt(n))+1):
            if n%x == 0:
                prime = False
                break  
        if prime == True:
            break
    return n

class HashTable():
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.p1 = getprime(10001)
        self.a1 = random.randint(0, self.p1)
        self.b1 = random.randint(0, self.p1)
        self.p2 = getprime(10001)
        self.a2 = random.randint(0, self.p2)
        self.b2 = random.randint(0, self.p2)
        self.arr = [None for i in range (self.m)]
        self.kickcount = 0

    #returns the hash function of a key
    def gethash1(self, key):
        return ((self.a1*key + self.b1)%self.p1)%self.m

    def gethash2(self, key):
        return ((self.a2*key + self.b2)%self.p2)%self.m

    #inserts the key
    def insert (self, key):
        if self.arr[self.gethash1(key)] == key or self.arr[self.gethash2(key)] == key:
            return
        if self.arr[self.gethash1(key)] == None:
            self.arr[self.gethash1(key)] = key
            self.n +=1
            self.kickcount = 0
            print("key "+str(key)+ " inserted at first position "+str(self.gethash1(key)))
        elif self.arr[self.gethash2(key)] == None:
            self.arr[self.gethash2(key)] = key
            self.n +=1
            self.kickcount = 0
            print("key "+str(key)+ " inserted at second position "+str(self.gethash2(key)))
        else:
            temp = self.arr[self.gethash1(key)] 
            self.arr[self.gethash1(key)] = key
            print("key "+str(key)+ " inserted at first position "+str(self.gethash1(key)))
            print("key "+str(temp)+ " kicked")
            
            self.kick(temp, self.gethash1(key))
            self.kickcount+=1
            if self.kickcount >= self.n:
                print("resetting...")
                self.reset()

    def reinsert (self, key, pos):
        if self.arr[self.gethash1(key)] == key or self.arr[self.gethash2(key)] == key:
            return
        if pos ==1:
            if self.arr[self.gethash1(key)] == None:
                self.arr[self.gethash1(key)] = key
                self.n +=1
                self.kickcount = 0
                print("key "+str(key)+ " inserted at first position "+str(self.gethash1(key)))
            else:
                temp = self.arr[self.gethash1(key)] 
                self.arr[self.gethash1(key)] = key
                print("key "+str(key)+ " inserted at first position "+str(self.gethash1(key)))
                print("key "+str(temp)+ " kicked")
                
                self.kick(temp, self.gethash1(key))
                self.kickcount+=1
                if self.kickcount >= self.n:
                    print("resetting...")
                    self.reset()
        if pos == 2:
            if self.arr[self.gethash2(key)] == None:
                self.arr[self.gethash2(key)] = key
                self.n +=1
                self.kickcount = 0
                print("key "+str(key)+ " inserted at second position "+str(self.gethash2(key)))
            else:
                temp = self.arr[self.gethash2(key)] 
                self.arr[self.gethash2(key)] = key
                print("key "+str(key)+ " inserted at second position "+str(self.gethash2(key)))
                print("key "+str(temp)+ " kicked")
                self.kick(temp, self.gethash2(key))
                self.kickcount+=1
                if self.kickcount >= self.n:
                    print("resetting...")
                    self.reset()

    #searches for the key
    def search (self, key):
        if self.arr[self.gethash1(key)] == key:
            return self.gethash1(key)
        elif self.arr[self.gethash2(key)] == key:
            return self.gethash2(key)
        return -1

    #kicks out key
    def kick (self, key, prev):
        if prev == self.gethash1(key):
            self.reinsert(key, 2)
        if prev == self.gethash2(key):
            self.reinsert(key, 1)

    #reset table
    def reset(self):
        temparr = [None for i in range (self.n)]
        i = 0
        for j in range(self.m):
            if self.arr[j] !=None:
                temparr[i] = self.arr[j]
                i+=1
        self.n = 0
        self.p1 = getprime(10001)
        self.a1 = random.randint(0, self.p1)
        self.b1 = random.randint(0, self.p1)
        self.p2 = getprime(10001)
        self.a2 = random.randint(0, self.p2)
        self.b2 = random.randint(0, self.p2)
        self.arr = [None for i in range (self.m)]
        self.kickcount = 0
        for j in range(self.n):
            self.insert(temparr[j])

H = HashTable(1000)
for i in range (500):
    H.insert(random.randint(700,3000))

