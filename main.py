import sys

filename = input("Enter file name: ")

with open(filename, 'r') as f:
    data = f.readlines()

line_count = 0
file_count = 0
f = open(f'output_{file_count}.csv', 'w')
for line in data:
    f.write(line)
    line_count += 1
    if line_count >= 100:
        file_count += 1
        line_count = 0
        f = open(f'output_{file_count}.csv', 'w')

