import time
def count_down(n):
    # base case
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return count_down(n-1)

print(count_down(5))