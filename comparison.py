import random
import math
import time

class HashTable_Cuckoo():
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.p1 = self.getprime(10001)
        self.a1 = random.randint(0, self.p1)
        self.b1 = random.randint(0, self.p1)
        self.p2 = self.getprime(10001)
        self.a2 = random.randint(0, self.p2)
        self.b2 = random.randint(0, self.p2)
        self.arr = [None for i in range (self.m)]
        self.kickcount = 0
    #returns a prime number greater than num
    def getprime(self, num):
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
    #returns the hash function of a key
    def gethash1(self, key):
        return ((self.a1*key + self.b1)%self.p1)%self.m
    def gethash2(self, key):
        return ((self.a2*key + self.b2)%self.p2)%self.m
    #inserts the key
    def insert (self, key, resize):
        if self.arr[self.gethash1(key)] == key or self.arr[self.gethash2(key)] == key:
            return -1
        elif resize == False:
            self.n +=1
        if self.arr[self.gethash1(key)] == None:
            self.arr[self.gethash1(key)] = key
            self.kickcount = 0
        elif self.arr[self.gethash2(key)] == None:
            self.arr[self.gethash2(key)] = key
            self.kickcount = 0
        else:
            temp = self.arr[self.gethash1(key)] 
            self.arr[self.gethash1(key)] = key
            self.kickcount+=1
            if self.kickcount >= self.m/10:
                self.reset(key)
            self.kick(temp, self.gethash1(key))

    def reinsert (self, key, pos):
        if self.arr[self.gethash1(key)] == key or self.arr[self.gethash2(key)] == key:
            return
        if pos ==1:
            if self.arr[self.gethash1(key)] == None:
                self.arr[self.gethash1(key)] = key
                self.kickcount = 0
            else:
                temp = self.arr[self.gethash1(key)] 
                self.arr[self.gethash1(key)] = key
                self.kickcount+=1
                if self.kickcount >= self.m/10:
                    self.reset(key)
                self.kick(temp, self.gethash1(key))
        if pos == 2:
            if self.arr[self.gethash2(key)] == None:
                self.arr[self.gethash2(key)] = key
                self.kickcount = 0                
            else:
                temp = self.arr[self.gethash2(key)] 
                self.arr[self.gethash2(key)] = key
                self.kickcount+=1
                if self.kickcount >= self.m/10:
                    self.reset(key)
                self.kick(temp, self.gethash2(key))
                
    #searches for the key
    def search (self, key):
        if self.arr[self.gethash1(key)] == key:
            return self.gethash1(key)
        elif self.arr[self.gethash2(key)] == key:
            return self.gethash2(key)
        return -1

    #kicks out key
    def kick(self, key, prev):
        if prev == self.gethash1(key):
            self.reinsert(key, 2)
        if prev == self.gethash2(key):
            self.reinsert(key, 1)

    #reset table
    def reset(self, kickedkey):
        temparr = [0 for x in range (self.n)]
        temparr[0] = kickedkey
        i = 1
        for j in range(self.m):
            if self.arr[j] !=None:
                temparr[i] = self.arr[j]
                i=i+1
        if (self.n/self.m >= 0.5):
            self.m = self.m*2
            print("resized to "+str(self.m)+ " n = "+str(self.n))
        self.p1 = self.getprime(10001)
        self.a1 = random.randint(0, self.p1)
        self.b1 = random.randint(0, self.p1)
        self.p2 = self.getprime(10001)
        self.a2 = random.randint(0, self.p2)
        self.b2 = random.randint(0, self.p2)
        self.arr = [None for i in range (self.m)]
        self.kickcount = 0
        for j in range(self.n):
            self.insert(temparr[j], True)

class HashTable_Chaining():
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.p = self.getprime(10001)
        self.a = random.randint(0, self.p)
        self.b = random.randint(0, self.p)
        self.table = [[] for _ in range(self.m)]
    def getprime(self, num): #returns a prime number greater than num
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
    def HashFunction(self, k): #returns the hash function of a key
        return ((self.a * k + self.b) % self.p) % self.m
    def insert(self, k): #inserts the key
        key = self.HashFunction(k)
        self.table[key].append(k)
    def search(self, k): #searches for the key
        key_value = self.HashFunction(k)
        for i in range(len(self.table[key_value])):
            if (self.table[key_value][i] == k):
                return self.HashFunction(k)
        return -1
    def printHashTable(self): #print the hash table
        for i in range(len(self.table)):
            print(i, end = " ")
            for j in self.table[i]:
                print("-->", end = " ")
                print(j, end = " ")
            print()

if __name__ == "__main__": #main function
    totTimeCuckoo = 0
    totTimeChaining = 0
    Iterations = 10
    m = 1000
    k = 3000
    for j in range (Iterations):
        H_Cuckoo = HashTable_Cuckoo(m)
        H_Chaining = HashTable_Chaining(m)
        for i in range (k):
            key = random.randint(750,50000)
            if H_Cuckoo.insert(key, False) == -1:
                i -=1
            if H_Chaining.insert(key) == -1:
                i -=1
            if i == random.randint(0, k):
                key_for_search = key
        CuckooTimer = time.perf_counter()
        print("\nIteration ", j+1, "/", Iterations,": Cuckoo: Search for key: ", key_for_search , ", at: ", H_Cuckoo.search(key_for_search))
        CuckooTimer = time.perf_counter() - CuckooTimer
        totTimeCuckoo += CuckooTimer
        print("Iteration ", j+1, "/", Iterations,": Cuckoo Search Time = " + str(CuckooTimer))
        ChainingTimer = time.perf_counter()
        print("Iteration ", j+1, "/", Iterations,": Chaining: Search for key: ", key_for_search , ", at: ", H_Chaining.search(key_for_search))
        ChainingTimer = time.perf_counter() - ChainingTimer
        totTimeChaining += ChainingTimer
        print("Iteration ", j+1, "/", Iterations,": Chaining Search Time = " + str(ChainingTimer))
        if (CuckooTimer < ChainingTimer):
            print("Iteration ", j+1, "/", Iterations,": ", CuckooTimer, " < ", ChainingTimer, " => Cuckoo Hashing faster in search\n")
        elif (CuckooTimer > ChainingTimer):
            print("Iteration ", j+1, "/", Iterations,": ", ChainingTimer, " < ", CuckooTimer, " => Chaining Hashing faster in search\n")
        else:
            print(CuckooTimer, " == ", ChainingTimer, "\n")
    print ("Total time for Cuckoo Hashing over", Iterations, "iterations = ", totTimeCuckoo)
    print ("Total time for Chaining Hashing over", Iterations, "iterations = ", totTimeChaining)
    if (totTimeCuckoo < totTimeChaining):
        print(totTimeCuckoo, " < ", totTimeChaining, " => Cuckoo Hashing faster in search over", Iterations, "iterations")
    elif (totTimeCuckoo > totTimeChaining):
        print(totTimeChaining, " < ", totTimeCuckoo, " => Chaining Hashing faster in search over", Iterations, "iterations")
    else:
        print(totTimeCuckoo, " = ", totTimeChaining)
    
