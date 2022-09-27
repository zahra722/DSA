# def reverseWord(t):
#     n=len(t)
#     i=0
#     j=n-1
#     while(i<j):
#         tp = t[i]
#         t[i]=t[j]
#         t[j]=tp
#         i+=1
#         j-=1
# n = int(input("enter your value"))
# lt =[]
# for i in range(0,n):
#     lt.append(int(input()))
# reverseWord(lt)
# print(lt)


# class Solution:
#     def reverseWord(self,s:list[str])->None:
#         i,j=0,len(s)-1
#         while(i<j):
#             s[i],s[j] = s[j],s[i]
#             i,j=i+1,j-1
#         return reverseWord(s)

        #  recusion o(n)


def reverseWord(s):
    def revers(l,r):
        if l<r:
            s[l],s[r]=s[r],s[l]
            revers(l+1,r-1)
    revers(0,len(s)-1)
    return reverseWord
   

