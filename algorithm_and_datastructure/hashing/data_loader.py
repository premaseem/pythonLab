import random
import uuid
import algorithm_and_datastructure.hashing.my_hash_table as mh

days = ["Monday", "Tuesday", "Wednesday", "Sunday"]
domains = ["gmail.com", "yahoo.com", "sexy.com"]

def generate_data(size):
    data = []
    for i in range(size):
        email = str(uuid.uuid4())[:20]
        domain = random.choice(domains)
        day = random.choice(days)
        rec = (email+"@"+domain, day)
        data.append(rec)
    data.append(("prem@gmail.com","tuesday"))

    return data

def write_data(data):
    with open("data_file","x") as f:
        for rec in data:
            line = rec[0]+":"+rec[1]+"\n"
            f.write(line)


def read_and_load(f):
    o = mh.MyHashTable(256)
    with open(f,"r") as file:
        lines = file.readlines()
        for line in lines:
            k,v = line.split(":")
            print("setting kv", k,v)
            o.set_value(k,v,"abc","xyz")
    print(o.get_value("prem@gmail.com"))


d = generate_data(100)
write_data(d)
read_and_load("data_file")