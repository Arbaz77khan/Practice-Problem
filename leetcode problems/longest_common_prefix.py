class Solution(object):
    def longestCommonPrefix(self, strs):
        size = len(strs)
        #print(strs)

        if (size == 0):
            return ""
    
        if (size == 1):
            return strs[0]

        end = len(strs[0])
        for s in strs:
            length = len(s)
            if length < end:
                end = length

        # print(end)
        if (end == 0 or end == None):
            return ""
        firstWord = strs[0]
        output = ""
        
        
        for i in range(0,end):
            wordCount = 1
            #print(firstWord[i]) 
            for j in range(1, size):
                nextWord = strs[j]
                #print(nextWord[i])
                if(firstWord[i] == nextWord[i]):
                    wordCount = wordCount + 1
                    #print(wordCount)
                else:
                    return output
            if (wordCount == len(strs)):  
                #print(firstWord[i])      
                output = output + firstWord[i]
        return output
        

object = Solution()

obj = object.longestCommonPrefix(["","cbc","c","ca"])

print(obj)