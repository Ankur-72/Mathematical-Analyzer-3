# Hey there! This is my assignment for WK3. Here, I have created a for loop and written some code to categorise those numbers into odd and even numbers. I hope you like it.

print("Hey, the numbers that have been taken for this experiment are 0 to 100")
print("These are the even numbers amongst them:")
for x in range(101):
    if x % 2 ==0:
        print(x)
        
print("These are the odd numbers amongst them:")
for x in range(101):
    if x % 2:
        print(x)