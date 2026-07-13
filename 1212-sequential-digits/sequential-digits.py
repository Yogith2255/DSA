class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def recur(low,high,num,add,ans):
            s_low=list(str(num))
            for i in range(len(s_low)-1):
                if int(s_low[i+1])-int(s_low[i])!=1:
                    if(int(s_low[i])+1)>=10:
                        new_num = 10 ** len(str(num))
                        new_add = 10 ** len(str(num))
                        return recur(new_num, high, new_num, new_add, ans)
                    for j in range(i+1, len(s_low)):
                        s_low[j] = str(int(s_low[j-1]) + 1)
            num = int("".join(s_low))   # <-- ADD THIS

            if num > high:
                return ans
            ans.append(num)

        
            if str(num)[-1] == '9':
                new_low = int("1" + "0"*len(str(num)))
                new_add = 10 ** len(str(num))
                return recur(new_low, high, new_low, new_add, ans)
            
            next_num = int(str(int(str(num)[0]) + 1) + "0"*(len(str(num))-1))
            return recur(low, high, next_num, add, ans)
        
        
        l = len(str(low))
        start = 10 ** (l - 1)
        add = start

        ans = []
        final = recur(start, high, start, add, ans)
        fn=[]
        for i in final:
            if low<=i and i<=high:
                fn.append(i)
        return fn
        