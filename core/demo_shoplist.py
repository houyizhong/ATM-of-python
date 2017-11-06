import pickle,os
import demo_credit


filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
product_path=dirname+os.sep+'product.txt'


def shopping():
	
	shopping_list=[]
	price=0
	
	'''read product'''
	f=open(product_path,'rb')
	product_list=pickle.load(f)
	f.close()

	def credit_payment(shoplist,price):
			result=demo_credit.payment(shoplist,price)
			
			if result == 'success':
				print ('You shopping done!')
			elif result == 'failure':
				print ('Sorry,your credit card balance is not enought!\n')
			else:
				print('Sorry,there have some unknown error!\n')

	while True:
		for index,item in enumerate(product_list):
			print(index+1,item)
		user_choice=input("Choice a product code('q' is exit.'pay' is settlement):")
		if user_choice.isdigit():
			user_choice = int(user_choice)
			if  user_choice <= len(product_list) and user_choice > 0:
				user_choice -= 1
				price += int(product_list[user_choice][1])
				shopping_list.append(product_list[user_choice][0])
				print ('Add {} to your shopplist!\n'.format(product_list[user_choice][0]))

			else:
				print("Sorry,product code isn's exist!\n")

		elif user_choice == "q":
			break
		elif user_choice == 'pay':
			print('Your check is {}'.format(price))
			if price != 0:
				credit_payment(shopping_list,price)
			break
		else:
		    print("Your enter invalid!\n")

shopping()
