file1 = open("data.txt", "r")
file_string = file1.read()
list1 = file_string.split("\n")

list_of_lists = []
for i in list1:
	city = i.split(",")
	city_population = [city[0], city[1]]
	list_of_lists.append(city_population)
print(list_of_lists)

conurbation = ["Belo Horizonte", "Contagem", "Betim", "Ibirite", "Santa Luzia", "Sabara"]

population_sum = 0

for i in list_of_lists:
	if i[0] in conurbation:
		population_sum += int(i[1])
print("conurbation population = ", population_sum)

population_sum_2 = 0

for i in list_of_lists:
	if not i[0] in conurbation:
		population_sum_2 += int(i[1])
print("remaining population = ", population_sum_2)

print(population_sum + population_sum_2)
