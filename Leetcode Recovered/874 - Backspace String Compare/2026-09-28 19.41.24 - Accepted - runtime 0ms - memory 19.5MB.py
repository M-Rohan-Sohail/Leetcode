class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            stack_s=[]
            stack_t=[]
            for char_s in s:
                  if char_s=="#":
                       if len(stack_s)>0:
                            stack_s.pop(-1)
                  else:
                       stack_s.append(char_s)
            for char_t in t:
                  if char_t=="#":
                       if len(stack_t)>0:
                            stack_t.pop(-1)
                  else:
                       stack_t.append(char_t)
            if stack_s==stack_t:
                 return True
            else:
                 return False