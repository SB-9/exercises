# average calculator made By samuel Burgess on 17'th Feb 2022

number_in_average = int(input("How many numbers to average?: "))
counter = 1
total = 0
while counter <= number_in_average:
    number = int(input(f"Enter number {counter}: "))
    total += number
    counter += 1
print("average is",total/number_in_average)
