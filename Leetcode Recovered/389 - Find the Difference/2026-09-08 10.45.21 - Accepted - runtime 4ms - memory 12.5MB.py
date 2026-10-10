class Solution(object):
    def findTheDifference(self, s, t):
                t_dict={}
                s_dict={}
                for word in t:
                    if word not in t_dict:
                        t_dict[word]=1
                    else:
                        t_dict[word]+=1
                for word in s:
                    if word not in s_dict:
                        s_dict[word]=1
                    else:
                        s_dict[word]+=1
                
                inc_item=[i for i in t_dict if i not in s_dict or s_dict[i]<t_dict[i]]
                return inc_item[0]