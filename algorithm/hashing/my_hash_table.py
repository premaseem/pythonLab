
class MyHashTable():
    def __init__(self, size):
        self.size = size
        self.buckets = [ [] for item in range(self.size)]

    def __str__(self):
        print("total buckets in hash table are :")
        return "".join(str(index) for index in self.buckets)

    def generate_hash(self, key):
        return abs(hash(key) % self.size)

    def set_value(self, key, *v):
        my_hashed_key = self.generate_hash(key)
        bucket = self.buckets[my_hashed_key]
        if self.update_value(key, *v) is None:
            bucket.append((key, *v))

    def update_value(self,key, *v):
        my_hashed_key = self.generate_hash(key)
        bucket = self.buckets[my_hashed_key]
        for index, item in enumerate(bucket):
            if key == item[0]:
                bucket[index] = (key, *v)
                return "updated successfully"
        return None

    def get_value(self, key):
        my_hashed_key = self.generate_hash(key)
        bucket = self.buckets[my_hashed_key]
        for item in bucket:
            if key == item[0]:
                return item

        return "Invalid key"

    def delete_value(self, key):
        my_hashed_key = self.generate_hash(key)
        bucket = self.buckets[my_hashed_key]
        for index, item in enumerate(bucket):
            if key == item[0]:
                del bucket[index]
                return "deleted successfully"
        return "item not found"


if __name__ == "__main__":
    o = MyHashTable(256)
    o.set_value("prem@gmail.com", "some information")
    o.set_value("sony@gmail.com", "some information", "some other medical information")
    print(o)
    print(o.get_value("dick@gmail.com"))
    print(o.get_value("prem@gmail.com"))
    o.set_value("prem@gmail.com", "some updated information")
    print(o.get_value("prem@gmail.com"))
    print(o.delete_value("prem@gmail.com"))
    print("get after delete")
    print(o.get_value("prem@gmail.com"))