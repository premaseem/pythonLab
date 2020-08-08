
def hello():
    print("hello is will not be invoked while importing")
    print("hello will only invoke only when run as stand alone")

if __name__ == "__main__":
    hello()