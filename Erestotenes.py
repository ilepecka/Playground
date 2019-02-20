
limit = int(input("Podaj limes superior > "))
limit = limit + 1
results = []

for i in range(limit):
    results.append(True)

for i in range(2, limit):
    multiplier = 2
    while i * multiplier < limit:
        results[i * multiplier] = False
        multiplier = multiplier + 1

counter = 0

for i in range(2, limit):
    if results[i] == True:
        counter = counter + 1
        # print(i, end='\n')
        
print(counter)
print('Koniec')
