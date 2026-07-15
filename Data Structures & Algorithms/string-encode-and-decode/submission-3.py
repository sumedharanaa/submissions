class Solution:

    def encode(self, strs: List[str]) -> str:
        st_new=""
        for i in strs:
            st_new+=i
            st_new+=";"
        return st_new

    def decode(self, s: str) -> List[str]:
        li=[]
        temp=""
        for i in s:
            if i==';':
                li.append(temp)
                temp=""
            else:
                temp+=i
        return li
