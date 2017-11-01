import pickle,os
import balance_module


filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
info_path=dirname+os.sep+'user.info'
blackfile_path=dirname+os.sep+'blacklist.txt'

def read_info():
	f=open(info_path,'rb')
	data=pickle.load(f)
	f.close()
	return data

def add_account():
	data=read_info()
	count_name=input('Enter add account("b" is back):')
	if count_name == 'b':
		pass
	else:
		count_balance=input('Enter account balance("b" is back):')
		if count_balance.isdigit():
			count_balance=int(count_balance)
			count_passwd=input('Enter account password("b" is back):')
			if count_passwd == 'b':
				pass
			else:
				data[count_name]={'passwd':count_passwd,'balance':count_balance}
				balance_module.write_balance(data)
				print('Done')
		elif count_balance == 'b':
			pass
		else:
			print('Sorry,your enter balance is not digit!\n')

def change_account():
	data=read_info()
	change_name=input('Enter change account name:')
	if change_name in data:
		change_balance=input('Enter change account balance:')
		if change_balance.isdigit():
			change_balance=int(change_balance)
			data[change_name]['balance']=change_balance
			balance_module.write_balance(data)
			print ('Done')
		elif change_balance == 'b':
			pass
		else:
			print('Sorry,your enter is not digit!\n')
	elif change_name == 'b':
		pass
	else:
		print ('Sorry,your choose account is not exist!\n')
	

def blacklist():
	f=open(blackfile_path,'rb')
	list=pickle.load(f)
	f.close()

	data=read_info()
	blacklist_name=input('Enter blacklist account name:')
	if blacklist_name in data:
		list.append(blacklist_name)
		f=open(blackfile_path,'wb')
		pickle.dump(list)
		f.close()
	elif blacklist_name == 'b':
		pass
	else:
		print ('Sorry,you choose account is not exist!\n')
