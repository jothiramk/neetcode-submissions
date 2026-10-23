class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        pattern_map = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+ "*" + word[j+1:]
                pattern_map[pattern].append(word)
        
        #now do a BFS
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1
        while queue:            
            for i in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == endWord:
                    return res
                #find the current word's pattern 
                for j in range(len(cur_word)):
                    pattern = cur_word[:j]+ "*" + cur_word[j+1:]
                    for neigh in pattern_map[pattern]:
                        if neigh not in visited:
                            queue.append(neigh)
                            visited.add(neigh)
            res += 1
        return 0

        