class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if not initialBoxes:
            return 0

        c = 0
        visited = set()
        waiting = set()
        i = 0

        # Treat initialBoxes as a growing queue; use index i to walk through it
        while i < len(initialBoxes):
            box = initialBoxes[i]
            i += 1

            # If we’ve already opened this box, skip it
            if box in visited:
                continue

            # If it’s unlocked (status==1), open it now
            if status[box] == 1:
                visited.add(box)
                c += candies[box]

                # Add any keys found inside this box
                for k in keys[box]:
                    if status[k] == 0:
                        status[k] = 1
                        # If we were “waiting” on that box, re-enqueue it
                        if k in waiting:
                            waiting.remove(k)
                            initialBoxes.append(k)

                # Add contained boxes to our queue
                for nb in containedBoxes[box]:
                    initialBoxes.append(nb)

            else:
                # Box is locked and we don't have its key yet—mark it as waiting
                waiting.add(box)

        return c


            


        