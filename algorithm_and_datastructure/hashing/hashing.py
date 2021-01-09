# hashing with resizing

class HashData:
    def __init__(self,id,*values):
        self.id = id
        self.values = values

    def __str__(self):
        return self.id + str(self.values)

    def __repr__(self):
        return self.id + str(self.values)

class HashTable:
    def __init__(self,size):
        self.size = size
        self.buckets = [[] for e in range(size)]

    def generate_hash(self,k):
        s = sum([ord(e) for e in k])
        hash_index = s % self.size
        return hash_index

    def insert_data(self,k):
        if -1 == self.retrieve_data(k.id):
            self.buckets[self.generate_hash(k.id)].append(k)

    def retrieve_data(self,k):
        bucket = self.buckets[self.generate_hash(k)]
        for e in bucket:
            if k == e.id:
                return e
        return -1


if __name__ == "__main__":
    o = HashTable(12)
    hd = HashData("prem","email","phone")
    o.insert_data(hd)
    # o.insert_data("prem")
    hd = HashData("prem","fax",("bra","penty"))
    o.insert_data(hd)
    # o.insert_data("seema")
    print(o.buckets)
    print(o.retrieve_data("prem"))
    print(o.retrieve_data("aseem1"))