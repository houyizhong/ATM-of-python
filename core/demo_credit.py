import pickle,time,os
import  balance_module
from demo_login import login


filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
info_path=dirname+os.sep+'user.info'
log_path=os.path.dirname(dirname)+os.sep+'logs'

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

def atm_logger(username,operating,money):
	user_dir=log_path+os.sep+username
	if not os.path.exists(user_dir):
		os.mkdir(user_dir)

	atm_log=user_dir+os.sep+'atm.log'

	times=time.strftime('%Y%m%d%H%M%S')
	data='{0}\t{1}\t{2}'.format(times,operating,money)

	log=open(atm_log,'a')
	log.write('{}\n'.format(data))
	log.close()

def consumer_logger(username,stock,price):
	user_dir=log_path+os.sep+username
	if not os.path.exists(user_dir):
		os.mkdir(user_dir)

	cust_log=user_dir+os.sep+'cust.log'

	times=time.strftime('%Y%m%d%H%M%S')
	data='{0}\t{1}\t{2}'.format(times,stock,price)

	log=open(cust_log,'a')
	log.write('{}\n'.format(data))
	log.close()

@login
def query(username):
	user_dir=log_path+os.sep+username
	if not os.path.exists(user_dir):
		print('Sorry,you do not have check.')
	else:
		cust_log=user_dir+os.sep+'cust.log'
		if os.path.exists(cust_log):
			log=open(cust_log,'r')
			print('You check is:')
			print(log.read())
			log.close()
		else:
			print('Sorry,you do not have check.')
	
@login
def inquire(username):
	
	data=read_info()

	
	print('Your balance is :')
	print(data[username]['balance'])

def payment(username,shoplist,bill):

	data=read_info()


	result=judgment(username,bill)
	if result == 'success':
		data=subtract(username,bill,data)
		balance_module.write_balance(data)
		consumer_logger(username,shoplist,bill)
	return result

@login
def transfer(username):
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
				atm_logger(username,'transfer',transfer_money)
			elif result == 'failure':
				print ('Your balance is not enought!\n')
			else:
				print ('Sorry,there have some unknown error!\n')
		else:
			print ('Sorry,your enter money is not a digit!\n')
	else:
		print('Sorry,your enter account is not exist!\n')

@login
def withdraw(username):
	data=read_info()

	withdraw_money=input('Enter your withdraw money:')
	if withdraw_money.isdigit():

		cost_money=float(withdraw_money)*(1+0.05)
		result=judgment(username,cost_money)
		withdraw_money=float(withdraw_money)
		if result == 'success':
			if withdraw_money > (data[username]['balance']/2):
				print ('Sorry,your withdraw money is more than avalid balance!\n')
			else:
				data=subtract(username,cost_money,data)
				balance_module.write_balance(data)
				atm_logger(username,'withdraw',cost_money)
				print ('Your withdraw done!\n')
	else:
		print('Soory,you enter is not digit!\n')

@login
def repay(username):
	data=read_info()

	repay_money=input('Enter your repay money:')

	if repay_money.isdigit():
		repay_money=float(repay_money)
		data=add(username,repay_money,data)
		balance_module.write_balance(data)
		atm_logger(username,'repay',repay_money)
		print('Your repay done!\n')
	else:
		print('Sorry,your enter is not digit!\n')

