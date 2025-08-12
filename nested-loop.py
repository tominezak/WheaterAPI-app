rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))
symbol = input('Enter a symbol: ')

for x in range(rows): #Rows
    for y in range(columns): #columns
        print(symbol, end='')
    print()