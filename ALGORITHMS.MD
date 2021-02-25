
## Greedy Algorithms
In greedy algorithm approach, decisions are made from the given solution domain. As being greedy, the closest solution that seems to provide an optimum solution is chosen.
Greedy algorithms try to find a localized optimum solution, which may eventually lead to globally optimized solutions. However, generally greedy algorithms do not provide globally optimized solutions.

    For the currency system, where we have coins of 1, 7, 10 value, counting coins for value 18 will be absolutely optimum but for count like 15, it may use more coins than necessary. 
    For example, the greedy approach will use 10 + 1 + 1 + 1 + 1 + 1, total 6 coins. 
    Whereas the same problem could be solved by using only 3 coins (7 + 7 + 1)

Hence, we may conclude that the greedy approach picks an immediate optimized solution and may fail where global optimization is a major concern.

## Sliding Window 
The sliding window algorithm can be used to solve problems that involve linear sequences, such as arrays. A window is a contiguous sequence which is part of an array. As the name suggests, the window is slid over the array. Some operations are performed on elements within this window, and then the window is slid further.
Sliding window is a sub-list that runs over an underlying collection

This technique shows how a nested for loop in some problems can be converted to a single for loop to reduce the time complexity.

``` 
# O(n*k) solution for finding the sum 
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
 
        # Update result if required.
        max_sum = max(current_sum, max_sum)
 
    return max_sum


# O(n) solution for finding
# maximum sum of a subarray of size k
def maxSum(arr, k):


	# Compute sum of first window of size k
	window_sum = sum(arr[:k])

	# first sum available
	max_sum = window_sum

	# Compute the sums of remaining windows
    # by removing first element of previous
	# window and adding last element of the current window.
	for i in range(n - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum


```

## Divide and conquer (D&C)

A divide-and-conquer algorithm works by recursively breaking the problem down into two or more subproblems of the same or related type, until these subproblems become simple enough to be solved directly [1]. 
Then one combines the results of sub problems to form the final solution.

    1. Divide. Divide the problem {S}S into a set of subproblems: {S_1, S_2, ... S_n\}
     where n≥2, i.e. there are usually more than one subproblem.
    
    2. Conquer. Solve each subproblem recursively. 
    
    3. Combine. Combine the results of each subproblem.
    
As you can see, divide-and-conquer algorithm is naturally implemented in the form of recursion. Another subtle difference that tells a divide-and-conquer algorithm apart from other recursive algorithms is that we break the problem down into two or more subproblems in the divide-and-conquer algorithm, rather than a single smaller subproblem. 
The latter recursive algorithm sometimes is called decrease and conquer instead, such as Binary Search.

## Decrease and conquer (D&C) 
Binary Search, is example of D&C where problem is broken and reduced or decreased till it become a single unit and gets solved. 

## Dynamic programming
Dynamic programming is used where we have problems, which can be divided into similar sub-problems, so that their results can be re-used. Mostly, these algorithms are used for optimization. Before solving the in-hand sub-problem, dynamic algorithm will try to examine the results of the previously solved sub-problems. The solutions of sub-problems are combined in order to achieve the best solution.

So we can say that −

    The problem should be able to be divided into smaller overlapping sub-problem.
    
    An optimum solution can be achieved by using an optimum solution of smaller sub-problems.
    
    Dynamic algorithms use Memoization.
  
# Tree Traversal 
Traversal is a process to visit all the nodes of a tree and may print their values too. Because, all nodes are connected via edges (links) we always start from the root (head) node. That is, we cannot randomly access a node in a tree. There are three ways which we use to traverse a tree −
If a binary tree is traversed in-order, the output will produce sorted key values in an ascending order.

```
    1 
   2 3 
  4 5 
```
## Depth First Traversals:
    (a) Inorder (Left, Root, Right) : 4 2 5 1 3
    (b) Preorder (Root, Left, Right) : 1 2 4 5 3
    (c) Postorder (Left, Right, Root) : 4 5 2 3 1

In this traversal method, the left subtree is visited first, then the root and later the right sub-tree. We should always remember that every node may represent a subtree itself.

## Breadth First or Level Order Traversal : 
    Level Order (Root, left, right) : 1 2 3 4 5
    
