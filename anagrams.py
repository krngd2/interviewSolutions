# Given an array of strings, return all groups of strings that are anagrams. 
# Represent a group by a list of integers representing the index in the original list. 
 
# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]


class Anagrams:

    def getList(self, arr):
        self.resultArr = []                   # reference to result  
        for i in range(len(arr)) :            # Loop through array of strings
            j = i + 1                         
            while j <= len(arr)-1:              
                if sorted(list(arr[i])) == sorted(list(arr[j])): # list(string) will spilt string into single letters, sort the list and compare them    
                    self.resultArr.append([i+1,j+1])    # if true append it to the results adding +1 to match he expected output
                j+=1                        
        return self.resultArr                 # return the values 

# Example

# anag = Anagrams()
# strings = ['cat', 'dog', 'god', 'tca'] 
# print(anag.getList(strings))