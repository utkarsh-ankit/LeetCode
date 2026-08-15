class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
            
        words=[beginWord]+wordList
        adj=defaultdict(list)
        
        def is_neighbour(word1,word2):
            diff=0
            
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    diff+=1
                if diff>1:
                    return False
                    
            return diff==1
            
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if is_neighbour(words[i],words[j]):
                    adj[words[i]].append(words[j])
                    adj[words[j]].append(words[i])
                    
        queue=deque([(beginWord,1)])
        visited={beginWord}
        
        while queue:
            word, length=queue.popleft()
            
            if word==endWord:
                return length
                
            for neighbor in adj[word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length+1))
        return 0