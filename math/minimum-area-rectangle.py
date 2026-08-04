class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #what do we mean by min area, we have to notic eon the parallel thing, so first clue is that if paralled, the or y value has to be common, we can utlise that, then we can have a hashmap that have have values for each x and y axis in soeted order, then to make a rectabncke, it has to be of same parllel length, if we can check aht, we can vcaldulate thea reare and we have have the min value to check>?
        
        #we can make sure that if 2 points, if we consider them as a diagonal, (x1,y1) and (x2,y2) as two points, the other two point so f thre rectancle should be (x1,y2) and (x2,y1). We can skip the point sthat have the same x and y value, since they are parallel and cant be a diagonal.

        # if we have those 2 points exist on our hashset. If yes, we calcualte the area and track the minimum.

        # hmap={tuple(i) for i in points}
        # area=float("inf")

        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         x1,y1=points[i]
        #         x2,y2=points[j]

        #         if x1==x2 or y1==y2:
        #             continue
                
        #         if (x1,y2) in hmap and (x2,y1) in hmap:
        #             area= min(area, abs(x2-x1)*abs(y2-y1))

        # return area if area!=float("inf") else 0


        hmap={tuple(i) for i in points}
        area=float('inf')

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1=points[i]
                x2,y2=points[j]

                if x1==x2 or y1==y2:
                    continue

                if (x1,y2) in hmap and (x2,y1) in hmap:
                    area=min(area, abs(x2-x1)*abs(y2-y1))

        return area if area!=float('inf') else 0





        