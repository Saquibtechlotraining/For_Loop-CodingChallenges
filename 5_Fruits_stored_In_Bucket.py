# Take name of 5 fruit from user through loop and store into a bucket made by list and print name of each fruit
# in the bucket:-

size = 5
bucket = []
for i in range(0, size):
    fruits_name = input(f"Enter the {i+1} fruit name:")
    bucket.append(fruits_name)
print("Bucket Fruits:", bucket)

count = 1                                 # For counting the fruits
for fruit in bucket:
    print(f"Fruit {count}:",fruit)
    count = count + 1
