class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # We can approach this problem by using dp
        
        # first, load every word in the list into a hashmap which stores their chain length
        words.sort(key=len)
        hashmap = {word : 1 for word in words}
        
        
        # Now, iterate through each word, and cut off a letter. See if we can chain with another word
        
        max_chain = 1
        
        for word in words:
            for i in range(len(word)):
                subword = word[:i] + word[i+1:]
                
                if subword in hashmap:
                    hashmap[word] = max(hashmap[word], hashmap[subword] + 1)
                    max_chain = max(max_chain, hashmap[word])
                    
                    
        return max_chain
