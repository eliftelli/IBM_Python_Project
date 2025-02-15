#!/usr/bin/env python
# coding: utf-8

# In[8]:


points = [(15,12), (7,8), (9,16), (8,22)]

def euclideanDistance (point1, point2):
    return ((point1[0]-point2[0]) ** 2 + (point1[1]-point2[1]) ** 2) ** 0.5

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
    
min_distance = min(distances)
print("Min Distance:", min_distance)


# In[ ]:




