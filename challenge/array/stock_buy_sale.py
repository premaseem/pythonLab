# Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another.

a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Brute Force
ans = ""
mp=0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if  a[j] - a[i] > mp:
            mp = a[j] - a[i]
            ans = "" + str(i) + " - " + str(j)

print(mp, ans)

#
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit

print(buy_and_sell_once(A))
