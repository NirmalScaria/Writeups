k=int(input())
sx,sy,fx,fy=map(int,input().split())
n=int(input())
tunnels=[]
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    tunnels+=[[x1,y1,x2,y2]]
# Possible positions : x,y,cost
min_distance=abs(sx-fx)+abs(sy-fy)
q=[[sx,sy,0]]

while(q!=[]):
    position=q.pop(0)
    for tunnel in tunnels:
        dis1_to_opening=position[2]+k+abs(position[0]-tunnel[0])+abs(position[1]-tunnel[1])
        if(dis1_to_opening<min_distance):
            q+=[[tunnel[2],tunnel[3],dis1_to_opening]]
        dis1_to_end=dis1_to_opening+abs(tunnel[2]-fx)+abs(tunnel[3]-fy)
        min_distance=min(min_distance,dis1_to_end)

        dis2_to_opening=position[2]+k+abs(position[0]-tunnel[2])+abs(position[1]-tunnel[3])
        if(dis2_to_opening<min_distance):
            q+=[[tunnel[0],tunnel[1],dis2_to_opening]]
        dis2_to_end=dis2_to_opening+abs(tunnel[0]-fx)+abs(tunnel[1]-fy)
        min_distance=min(min_distance,dis2_to_end)
print(min_distance)