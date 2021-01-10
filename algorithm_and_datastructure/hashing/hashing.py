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

    def resize(self):
        self.size = self.size * 2
        self.new_bucket = [ [] for e in range(self.size)]

        for i, bucket in enumerate(self.buckets):
            if bucket:
                index = self.generate_hash(bucket[0].id)
                self.new_bucket[index] = bucket
        print(f"old bucket {self.buckets} new bucket {self.new_bucket}")
        self.buckets = self.new_bucket


    def insert_data(self,k):
        if -1 == self.retrieve_data(k.id):
            self.buckets[self.generate_hash(k.id)].append(k)
        op = sum([1 for x in self.buckets if x])
        if op > self.size * 0.6:
            # trigger resize
            print("triggered resize")
            self.resize()

    def remove_data(self,k):
        if -1 != self.retrieve_data(k.id):
            print("removing ",k)
            bucket = self.buckets[self.generate_hash(k.id)]
            for i, e in enumerate(bucket):
                if k.id == e.id:
                    print("removing inside loop",k)
                    bucket.pop(i)

    def update_data(self,k):
        self.remove_data(k)
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
    hd = HashData("prem","fax","bra","penty")
    o.insert_data(HashData("prem","fax","bra","penty"))
    ash = HashData("seema","ashim")
    o.insert_data(ash)
    ash = HashData("seema45","ashim")
    o.insert_data(ash)
    print(o.buckets)
    # o.insert_data("seema")
    # o.remove_data(ash)
    o.update_data(hd)
    print(o.buckets)
    print(o.retrieve_data("prem"))
    print(o.retrieve_data("aseem1"))
    # o.resize()
    ash = HashData("zebra","ashim")
    o.insert_data(ash)
    print(o.buckets)
    o.insert_data(HashData("prem1","fax","bra","penty"))
    o.insert_data(HashData("prem2","fax","bra","penty"))
    o.insert_data(HashData("prem3","fax","bra","penty"))
    o.insert_data(HashData("prem4","fax","bra","penty"))
    o.insert_data(HashData("prem5","fax","bra","penty"))
    o.insert_data(HashData("prem6","fax","bra","penty"))
    o.insert_data(HashData("prem7","fax","bra","penty"))
    o.insert_data(HashData("prem8","fax","bra","penty"))