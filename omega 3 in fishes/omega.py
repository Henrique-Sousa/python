from bs4 import BeautifulSoup

#source: https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/fats-and-cholesterol/types-of-fat/omega-3-fats/
html = open("seafoods.html", "r")
soup = BeautifulSoup(html, 'html.parser')

tab = soup('tr')
tam = len(tab)
dic = {}
for i in range(1,tam):
	name =  soup('tr')[i].find_all('td')[0].text.strip("\n")
	size = float(soup('tr')[i].find_all('td')[1].text.replace(' oz', ''))
	omega = float(soup('tr')[i].find_all('td')[2].text.replace(",", ""))
	dic[name] = omega/size

for w in sorted(dic, key=dic.get, reverse=True):
	print(w, dic[w])
