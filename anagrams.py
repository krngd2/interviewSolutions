# Given an array of strings, return all groups of strings that are anagrams. 
# Represent a group by a list of integers representing the index in the original list. 
 
# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]


class Solution:
 
    def anagrams(self, arr):
        self.resultArr = [] 
        self.pos = []
        for i in range(len(arr)) :  
            if sorted(list(arr[i])) in self.resultArr:  
                self.pos[self.resultArr.index(sorted(list(arr[i])))].append(i+1)
            else: 
                self.resultArr.append(sorted(list(arr[i])) )
                self.pos.append([i+1]) 
        # print(self.resultArr)
        return self.pos

# Example

# anag = Solution()
# string1 = [ "abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", 
#             "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", 
#             "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", 
#             "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", 
#             "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", 
#             "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", 
#             "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", 
#             "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]

# # string2 = [ "cat", "dog", "god", "tca" ]

# print(anag.anagrams(string1))
# print(anag.anagrams(string2))