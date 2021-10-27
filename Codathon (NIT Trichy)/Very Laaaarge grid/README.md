# Problem : Very Laaaarge grid
Link to question : https://assessment.hackerearth.com/challenges/college/codathon-long/algorithm/fe5f51c208c94356bfb99ec864f504b6/

Problem statement : You are given an infinite 2D grid. You are in cell (SX,SY) and want to go to cel (FX,FY). Each of the adjacent cells having a common edge are connected by a road. You can select a road to travel between the adjacent cells. You need 1 unit of energy to travel on any roads. Therefore, to travel from (SX,SY) to (FX,FY), you require a huge amount of energy. There are N tunnels built. Each tunnel connectes a pair of cells (X1,Y1) and (X2,Y2). If you take a tunnel to go from one cell to another, then you need K units of energy.

Input format:
First line : K (=energy to travel any tunnel)
Second line : SX SY FX FY
Third line : N (=number of tunnels)
Next lines : N lines denoting tunnels (X1 Y1 X2 Y2)

# Understanding the question
This seemed like a really really hard problem from the top. I skipped the question the first time I saw and left it there for 2 days. It was almost frightening to read this question. Because, over the top it looks like a problem that needs some fancy algorithms like A* or something, particularly since it has such a long range.

But, on reading it few times, the question will start to become much simpler and simpler. Try drawing it on a paper. The question could be better read in the following way then.
> You know, if there were no tunnels, you will have to travel FX-SX distance along X axis and FY-SY distance along Y axis to reach there. That is, a total of abs(FX-SX)+abs(FY-SY). Check if using any combination of tunnels will give a better route. Thats all. You will get score.

Also, you know each tunnel takes the same cost, K. 

# Towards a solution
Now it somewhat start making sense as a problem that could work with searching algorithms without directional sense.

Then, work on paper for sometime and you hit this thought.
> Oh wait, there is always a minimum distance we know. At the beginning, it is abs(FX-SX)+abs(FY-SY) but as we try using tunnels, we might be able to find smaller minimums. And, we have to search only those combinations of tunnels for which total cost is lower than this given minimum. That must limit the complexity to terms of N, ie, number of tunnels, and NOT the distance (which is apparantly big)

So, some workable Breadth first solution idea comes up. We could do a very conventional search that starts from the given origin, (SX,SY). Then check each tunnel as a possible path. But, there are many points where we could optimise.
> 1. If the cost to reach the end of a tunnel, ie, { distance from origin to beignning of that tunnel + K  } is higher than the present min_distance, its pointless to check further on that route. Leave it and move on.
> 2. If we find that at a tunnels end, the cost to reach from origin to that tunnels end + cost to reach to dest from that tunnels end is lower than present min_distance, then we could safely say that the new minimum must be this value. Because apparantly this tunnel turned out to be a better route.

# How the search works

Even though the BFS is pretty conventional, there are few things customised. So, this is how it works.
> We create a new array, **q** which will act as a.... [drummrolls....] "QUEUE".

> It is suppose to contain all the points we have reached (using tunnels)

> The format of each item in the queue could be ideally [ x_coordinate , y_coordinate , cost_to_reach_there ]

> So, initially the queues value will be **q=[[ SX , SY , 0 ]]** because we havent spent anything to reach there

> Now we do a BFS. We do a while loop as long as q is not empty. We take the first element in the **q**. Taking an element from the **q** means, now we are trying to search for possibile routes that starts from this position.

> We try to move from this point(x,y) to each tunnels. We calculate the price to reach the ending of the tunnel from this point(x,y). That will be distance from (x,y) to opening of the tunnel + k. If that distance is higher than the present minimum distance, leave it. Doesnt concern us. Else, this could be a potential route. So, add it to end of queue.

> Also, find the cost to reach from that end of tunnel to our destination. If the total cost is less than present_minimum_distance, we could update the present_minimum_distance by this value, because apparantly this is a better route. We wont have to consider route options longer than this now.

> Dont forget that tunnel is not one way. We should consider both possibilities, ie, cost to enter from point A of the tunnel and exit from point B as well as enter from point B and exit from point A. That is visible in the code clearly.

Keep doing this as long as there are possible routes left in the **q** and by the end, we will be having our shortest path stored in the min_distance variable.

**If you enjoyed reading this, a follow on GitHub would be nice. I will try to write and share useful stuff here. **
