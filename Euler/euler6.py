
num = 100

sumofsquarenums = 0
sumofnums = 0

for number in range(1, num+1):
    sumofsquarenums += number**2
    sumofnums += number

print(sumofnums**2 - sumofsquarenums)
