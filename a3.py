str=input("enter a string")
count=0
vov="AEIOUaeiou"
for i in str:
          if i in vov:
             count=count+1
else:
    print(count)
