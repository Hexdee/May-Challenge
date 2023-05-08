import itertools

# Define the integer string
num_str = '1867'

# Generate all permutations of the integer string
perms = list(itertools.permutations(num_str))

# Check each permutation for divisibility by 7
divisible_perms = []
for perm in perms:
    num = int(''.join(perm))
    if num % 7 == 0:
        divisible_perms.append(num)

# If there are no divisible permutations, print a message and exit
if not divisible_perms:
    print("No permutations are divisible by 7")
    exit()

print(perms)
print(divisible_perms)

# Compute the average of the smallest and largest divisible permutations
avg = (min(divisible_perms) + max(divisible_perms)) / 2

# Print the result
print("The average of the smallest and largest divisible permutations is:", avg)

