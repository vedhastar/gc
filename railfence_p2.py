string=input("enter a string")
def RailFence(txt):
      result=""
      for i in range(len(string)):
           if(i%2==0):
               result==string[i]
      for i in range(len(string)):
           if(i%2!=0):
                result += string[i]
      return result
print(RailFence(string))
