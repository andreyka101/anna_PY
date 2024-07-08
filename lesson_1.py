# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
a1 = 4.6
spi=[1,2,3,2]
print(spi.count(2))
print("uuu")

spi_2 = spi
spi_copy = spi.copy()
spi.append(88)
print(spi_2)
print(spi_copy)


# for i in spi:
#     print(i*2)

for i in range(len(spi)):
    print(spi[i])

# i = 0
# while i != len(spi):
#     print(spi[i])
#     i+=1


