import  math



num1=input("enter first integer")
num2=input("enter second number")
num3=input("enter third number")

num1=int(num1)
num2=int(num2)
num3=int(num3)


print("maximum_sum is ", num1 if (num1>num2 and num1>num3) else num2 if (num2>num1 and num2>num3) else num3)

print("minimum_sum is ", num1 if (num1<num2 and num1<num3) else num2 if (num2<num1 and num2<num3) else num3 )













































# minimum_sum=min(num1,min(num2, num3))
# maximum_sum=max(num1, max(num2, num3))
# print(" the minimum_sum number is ", minimum_sum, "and the maximum_sum number is ", maximum_sum)
# minimum_sum=num2
# maximum_sum=num2
# if (num3<minimum_sum and num2>minimum_sum):minimum_sum=num3
# if(num3>maximum_sum and num2<maximum_sum):maximum_sum=num3

# elif(num2<minimum_sum and num3>minimum_sum):minimum_sum=num2
# elif(num2>maximum_sum and num3<maximum_sum):maximum_sum=num2
# print()
# elif (num1<minimum_sum and num2>minimum_sum):minimum_sum=num1
# elif(num1>maximum_sum and num2<maximum_sum):maximum_sum=num1
# print()


