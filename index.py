import pprint
col = int(input('Enter number of columns: '))
row = int(input('Enter number of rows: '))
print(f'{col}x{row}')

arr = [[0] * col] * row
pprint.pprint(arr)

col_clues = []
row_clues = []
for x in range(col):
    col_clues.append(input(f'Column Clue # {x + 1}: ').split())

print(col_clues)

for x in range(row):
    row_clues.append(input(f'Row Clue # {x + 1}: ').split())

print(row_clues)