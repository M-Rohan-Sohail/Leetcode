class Solution(object):
    def letterCombinations(self, digits):
            digit_letter_dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
            result=[]
            def helper(index,curr):
                if index==len(digits):
                    result.append(curr)
                    return
                index_letter=digits[index]
                curr_letters=digit_letter_dict[int(index_letter)]
                for letter in curr_letters:
                    curr=curr+letter
                    helper(index+1,curr)
                    curr=curr[:-1]
            helper(0,"")
            return result