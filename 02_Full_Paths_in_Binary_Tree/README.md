## Full Paths in Binary Tree

In a binary rooted tree, each node is assigned one of given Q distinct colors.
A so-called regulating value D is positive a integer.
We say that a node x is (c, D)-full, if the subtree which root is x contains exactly D nodes of color c.
Furhermore, we say that a path from the root to some leaf in the tree is full if it contains at least one (c, D)-full node for each color c out of given C colors.

# Input

The first input line contains three integers N, C, D separated by spaces and representing the number of nodes in the tree, the number of node colors and the regulating value.
We assume that the nodes are labeled 0, 1, ..., N−1 and the colors are labeled 0, 1, ..., C−1. The label of the tree root is always 0.
The next line contains N integers, separated by spaces, which represent the list of colors of particular nodes. The colors are listed in ascending order of node labes. The first integers represents the color of node 0, the second integer represents the color of node 1, etc.
Next, there are N −1 text lines, each specifies one edge in the tree. The line contains two integers a, b separated by space. Integer a is the label of the parent of the node which label is b.
It holds, 2 ≤ N ≤ 150000, 2 ≤ C ≤ 10, 2 ≤ D ≤ 20.

# Output

The output contains one text line with a single integer representing the number of full paths in the input tree. 

## Example 1

Input

25 3 4
0 2 0 0 0 1 1 2 0 0 2 0 1 2 2 1 2 2 2 2 0 2 2 0 0
20 23
7 22
8 20
11 18
13 17
14 16
3 13
4 11
5 9
6 7
1 6
2 4
0 1
0 2
2 3
1 5
6 8
5 10
4 12
3 14
7 21
8 19
14 15
20 24

Output

8


## Example 2

Input

16 2 3
0 0 1 1 0 0 1 1 0 1 0 1 0 1 1 1
0 1
1 2
2 3
1 4
4 5
4 6
0 7
7 8
8 9
8 10
7 11
11 12
11 13
13 14
13 15

Output

5

## Example 3

Input

6 5 1
0 1 2 3 4 4
3 4
3 5
2 3
1 2
0 1

Output

2
