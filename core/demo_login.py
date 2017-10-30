import pickle
import os

filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
info_path=dirname+os.sep+'user.info'
blackfile_path=dirname+os.sep+'blacklist.txt'


def login():
	f=open(info_path,'rb')
	user_dict=pickle.load(f)
	f.close()
	
	blackfile=open(blackfile_path,'rb')
	blacklist=pickle.load(blackfile)
	blackfile.close()

	while True:
		username=input('Enter your account:')
		password=input('Enter your password:')

		if username not in user_dict:
			print('Sorry,your account is not exist!\n')
			continue
		elif username in blacklist:
                	print ("Sorry you are in blacklist!")
                	continue
		else:
			if user_dict[username]['passwd'] != password:
				print ('Sorry,your password invalid!\nPlease try again!\n')
				continue
			else:
				print ('Welcome {}!'.format(username))
				break

	return username

