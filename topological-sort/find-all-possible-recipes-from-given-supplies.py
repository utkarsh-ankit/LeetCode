from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)
        all_items = set(supplies)

        # Build graph and indegree
        for i in range(len(recipes)):
            recipe = recipes[i]
            indegree[recipe] = 0
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                indegree[recipe] += 1

        # Initialize queue with available supplies
        queue = deque(supplies)
        res = []

        while queue:
            item = queue.popleft()
            for nei in graph[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    res.append(nei)
                    all_items.add(nei)  # Now this recipe is also available

        return res
