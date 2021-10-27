# Problem : Node power
Link to question : https://assessment.hackerearth.com/challenges/college/codathon-long/algorithm/68b5420d41934ba697542978d0be8d78/

Problem statement : You are given N nodes of a graph, initially pair-wise disjoint. Every node has a positive integer value denoted by an array A.
The power of a node is the product of all distinct prime factors of the value of the node. And the power of a group of nodes is the sum of powers of individual nodes in that connected component.

You are given Q queries, each of which is one of the following :

Query 1 : 1 X
=> A new node with integer X is added to the graph. The index of this node is number_of_nodes+1.

Query 2 : 2 X Y
=> Nodes with indices X and Y are connected along with their groups (if any) and form a new group.

Query 3 : 3 X
=> Print the number of connected components with power strictly greater than X that are currently available.

Note: Type 2 queries can have repetitions and the same node can connect to itself.

Input format

First line: 
2 space-separated integers N and Q denoting the initial number of nodes and number of queries respectively
Second line: contains N space-separated integers denoting the array A

Next Q lines: A single query in each line
Note: Query can be of 3 types as described in the question
Output format
Print a single integer in a new line for every query of type 3.

# Understanding the question
Here, I am trying to write a kind-of-close-to-working solution, giving more focus to the method to reach it than the solution. For this question, it was 80% work was about actually understanding the question. Lets try to dive in. If you dont understand something, read it 10 times (that usually works for me.) 

So, there will be an initial given array. Cool. Lets do that first. Let the array be
> [ 1 , 2 , 3 , 4 , 5 ]
