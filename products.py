import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#使用者輸入
def user_input(products):
	while True:
		name = input("輸入產品名子:")
		if name == "q":
			break
		price = input("輸入產品價格:")
		price = int(price)
		products.append([name,price])
	print (products)
	return products

#印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0],"的價格是",product[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for product in products:
			f.write(product[0]+ ','+ str(product[1])+ '\n')



def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('找到檔案')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = read_file(filename)
	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()