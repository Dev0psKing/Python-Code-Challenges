result = []

for i in range(1, 31):
    listSquares = i * i
    if listSquares >= 30:
        break
    result.append(listSquares)
print(result)
print("The first 5 elements are: ", result[:5])
print("The Last 5 elements are: ", result[-5:])

