#---------------------Loops to print numbers from 1 to 20, skipping multiples of 5--------------


for i in range(1, 21):
    if i % 5 == 0:
        continue
          
    print(i, end=" ")
