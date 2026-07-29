class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=collections.defaultdict(list)
        #if beginWord not in wordList:
        wordList.append(beginWord)
        res=0
      
        visit=set([beginWord])
        q=deque([beginWord])
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+ "*" +word[j+1:]
                nei[pattern].append(word)
        
        while q:
            res+=1
            for i in range(len(q)):
                qword=q.popleft()
                if qword == endWord:
                    return res
                for c in range(len(qword)):
                    pattern=qword[:c]+ "*" +qword[c+1:]
                    for neigh in nei[pattern]:
                        if neigh not in visit:
                            visit.add(neigh)
                            q.append(neigh) 
                            
        return 0


