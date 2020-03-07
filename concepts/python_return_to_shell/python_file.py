import sys

dict = {"hi":"man", "bye":"women"}
if __name__ == "__main__":
    try:
        key = sys.argv[1]
    except:
        pass
        key = "nothing"
    print(dict.get(key))
