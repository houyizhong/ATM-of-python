import pickle,time,os
import  balance_module
from demo_login import login


filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
info_path=dirname+os.sep+'user.info'

def read_info():
	f=open(info_path,'rb')
	data=pickle.load(f)
	f.close()
	return data

def add(username,bill,data):

	balance=data[username]['balance']
	balance += bill
	data[username]['balance']=balance
	return data

def subtract(username,bill,data):

	balance=data[username]['balance']
	balance -= bill
	data[username]['balance']=balance
	print ('Your balance is {}\n'.format(balance))
	return data

def judgment(username,bill):
	data=read_info()

	balance=data[username]['balance']
	if balance >= bill:
		return 'success'
	else:
		print ('Your balance is not enought!\n')
		return 'failure'

def atm_logger(operating,money):
	times=time.strftime('%Y%m%d%H%M%S')
	data='{0}\t{1}\t{2}'.format(times,operating,money)

	log=open('atm.log','a')
	log.write('{}\n'.format(data))
	log.close()

def consumer_logger(stock,price):
	times=time.strftime('%Y%m%d%H%M%S')
	data='{0}\t{1}\t{2}'.format(times,stock,price)

	log=open('cust.log','a')
	log.write('{}\n'.format(data))
	log.close()

def inquire():
	
	data=read_info()

	username=login()
	
	print('Your balance is :')
	print(data[username]['balance'])


def payment(shoplist,bill):

	data=read_info()

	username=login()

	result=judgment(username,bill)
	if result == 'success':
		data=add(username,bill,data)
		balance_module.write_balance(data)
		consumer_logger(shoplist,bill)
	return result

def transfer():
	username=login()
	
	data=read_info()

	transfer_account=input('Enter transfer account:')
	transfer_money=input('Enter transfer money:')

	if transfer_account in data:
		if transfer_money.isdigit:
			transfer_money=float(transfer_money)
			result=judgment(username,transfer_money)
			if result == 'success':
				data=subtract(username,transfer_money,data)
				data=add(transfer_account,transfer_money,data)
				print ('Your transfer done!\n')
				balance_module.write_balance(data)
				atm_logger('transfer',transfer_money)
			elif result == 'failure':
				print ('Your balance is not enought!\n')
			else:
				print ('Sorry,there have some unknown error!\n')
		else:
			print ('Sorry,your enter money is not a digit!\n')
	else:
		print('Sorry,your enter account is not exist!\n')


def withdraw():
	username=login()
	data=read_info()

	withdraw_money=input('Enter your withdraw money:')
	if withdraw_money.isdigit():

		cost_money=float(withdraw_money)*(1+0.05)
		result=judgment(username,cost_money)
		if result == 'success':
			if withdraw_money > (data[username]['balance']/2):
				print ('Sorry,your withdraw money is more than avalid balance!\n')
			else:
				data=subtract(username,cost_money,data)
				balance_module.write_balance(data)
				atm_logger('withdraw',cost_money)
				print ('Your withdraw done!\n')
	else:
		print('Soory,you enter is not digit!\n')


def repay():
	username=login()
	data=read_info()

	repay_money=input('Enter your repay money:')

	if repay_money.isdigit():
		repay_money=float(repay_money)
		data=add(username,repay_money,data)
		balance_module.write_balance(data)
		atm_logger('repay',repay_money)
		print('Your repay done!\n')
	else:
		print('Sorry,your enter is not digit!\n')

