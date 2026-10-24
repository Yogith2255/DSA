class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        c=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans=[]
        for i in words:
            p=""
            for j in i:
                p+=c[al.index(j)]
            ans.append(p)
        return len(set(ans))