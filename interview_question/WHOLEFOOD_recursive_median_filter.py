"""
Recursive Median Filter

Programming challenge description:
Finally, you get the latest measurements in your scientific experiment. It was not easy to collect that data. A lot of noise is present in the space around your secret laboratory. But you know that it's not hard to improve the quality of the measured signal, applying a median filter to the raw data from analog-to-digital converters.

In standard median filter output is at some point is the median value of N samples around that point. Another way to describe that is a window of size N elements slides over the input signal, element by element. On every step, the median of the elements in the window is written to the output.

The median of the set of integers is the middle element in the sorted list of these numbers.

In recursive median filter output is the median of elements in the current window. But now, in the left half of that window input signal is replaced by output from the previous steps.


Write a program that filters out the noise from the raw data, using the recursive median filter.

For simplicity, assume that the size of the filter window is always odd.
Do not process the boundaries of the input signal, where it's not enough elements to compose a window of the necessary size. In other words, just crop the signal. If the filter's window size is 5 you will lose 2 first and 2 last elements.
Also, use input elements at the beginning of the signal where there are no outputs for the left part of the filter's window.

For example, let's filter signal 17 18 19 37 21 22 23 85 25 26 using a window of size 3. For the first 3 elements 17 18 19 the median is 18. Shifting filter's window to the next 3 elements 18 19 37 gives 19 as an output. 19 37 21 outputs 21, and so on.

Input:
The first line contains an odd integer, the size of the filter's window. Each next line of the input has a comma-separated series of positive integers. That is raw data of the measured signal. For example:

3
5,5,5,15,5,5,5
1,2,3,25,5,6,52,7,8
Output:
Print out a comma-separated series of integers, that is a result of applying the recursive median filter to the raw input data. For example:

5,5,5,5,5
2,3,5,5,6,7,7

===============
Test 1:
3
7,7,7,7,17,7,7,7,7,77,7,7,7
Expected Output
7,7,7,7,7,7,7,7,7,7,7

Test 2:
3
0,87,173,258,342,422,5499,573,642,707,766,819,866,9906,939,965,984,996,1000
0,34,69,104,139,173,207,9241,275,309,342,374,406,438,469,499,529,559,587,615,642,669,694,9719,743,766,788,809,829,848,866,882,898,913,927,9939,951,961,970,978,984,990,994,997,999,1000

Expected Output
87,173,258,342,422,573,573,642,707,766,819,866,939,939,965,984,996
34,69,104,139,173,207,275,275,309,342,374,406,438,469,499,529,559,587,615,642,669,694,743,743,766,788,809,829,848,866,882,898,913,927,951,951,961,970,978,984,990,994,997,999

"""
# Algo
# input as array of numbers
# take window size and get median (middle number for sorted window size)
# print median and replace median number for next window

def filter_signal(s,data):
    arr = data.split(",")
    arr = list(map(lambda x: int(x),arr))
    ans = []
    # print(arr)
    for x in range(0,len(arr)-s+1):
        med = get_median(s,arr[x:x+s])
        arr[x+1] = med
        ans.append(med)
    s = ",".join(map(str,ans))
    # print(s)
    return s

def get_median(s,data):
    d = sorted(data)
    return d[s//2]

t1 = "7,7,7,7,17,7,7,7,7,77,7,7,7"
ans = filter_signal(3,t1)
print(ans)
print("7,7,7,7,7,7,7,7,7,7,7")
print(t1)
if ans == "7,7,7,7,7,7,7,7,7,7,7":
    print("pass")

t2 = "0,87,173,258,342,422,5499,573,642,707,766,819,866,9906,939,965,984,996,1000"
ans = filter_signal(3,t2)
print(ans)
print("87,173,258,342,422,573,573,642,707,766,819,866,939,939,965,984,996")
print(t2)
if ans == "87,173,258,342,422,573,573,642,707,766,819,866,939,939,965,984,996":
    print("Pass")

t3 = "0,34,69,104,139,173,207,9241,275,309,342,374,406,438,469,499,529,559,587,615,642,669,694,9719,743,766,788,809,829,848,866,882,898,913,927,9939,951,961,970,978,984,990,994,997,999,1000"
ans = filter_signal(3,t3)
print(ans)
print(t3)
if ans == "34,69,104,139,173,207,275,275,309,342,374,406,438,469,499,529,559,587,615,642,669,694,743,743,766,788,809,829,848,866,882,898,913,927,951,951,961,970,978,984,990,994,997,999":
    print("Pass")