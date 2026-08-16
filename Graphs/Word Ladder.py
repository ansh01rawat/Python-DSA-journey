class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        q.append((beginWord, 1))
        word_set = set(wordList)
        visit = {beginWord}
        while q:
            curr_word, level = q.popleft()
            if curr_word == endWord:
                return level
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == curr_word[i]:
                        continue
                    new_word = curr_word[:i] + ch + curr_word[i + 1:]
                    if new_word in word_set and new_word not in visit:
                            q.append((new_word, level + 1))
                            visit.add(new_word)
        return 0
