import random
import math
import time

class HashTable:
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.p = self.getprime(10001)
        self.a = random.randint(0, self.p)
        self.b = random.randint(0, self.p)
        self.table = [[] for _ in range(self.m)]
    def getprime(self, num):  #returns a prime number greater than num
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
    H = HashTable(20)
    for i in range (20):
        key = random.randint(500,50000)
        if i == random.randint(0, 20):
            key_for_search = key
        if H.insert(key) == -1:
            i -= 1
    print(H.table)
    H.printHashTable()
    timer = time.perf_counter()
    print("Search for key: ", key_for_search, ", found at position: ", H.search(key_for_search))
    timer = time.perf_counter() - timer
    print("Search time = " + str(timer))