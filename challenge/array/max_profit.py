# <p>Suppose you are given a list of integers, <code>prices</code>, that represent the price of Google's stock over time. <code>prices[i]</code> is the price of the stock on day <code>i</code>. You must buy the stock once and then later sell it. You are not allowed to sell before you buy.</p>
# <p>Write a function that returns an integer, which is the maximum profit you can make from buying the stock and then later selling it. If the list is empty, return <code>0</code>.</p>

def solution(prs):
    max = 0
    for x in range(len(prs) - 1):
        for y in range(x + 1, len(prs)):
            profit = prs[y] - prs[x]
            if profit > max:
                max = profit
    return max


assert  11 is solution([6,0,-1,10])