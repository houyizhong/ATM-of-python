import os
import sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORE_DIR=BASE_DIR+os.sep+'core'

sys.path.append(BASE_DIR)
sys.path.append(CORE_DIR)

from core import demo_credit

#print(sys.path)

action_list=['Query check','Transfer','Query balance','Withdraw','Repay']

while True:
	for index,item in enumerate(action_list):
		print(index+1,item)
	print('"q" is exit.')
	enter_action=input('Enter your choice:')

	if enter_action.isdigit():
		if enter_action == '1':
			'''Query check'''
			demo_credit.query()
			continue
		elif enter_action == '2':
			'''Transfer'''
			demo_credit.transfer()
			continue
		elif enter_action == '3':
			'''Query balance'''
			demo_credit.inquire()
			continue
		elif enter_action == '4':
			'''Withdraw'''
			demo_credit.withdraw()
			continue
		elif enter_action == '5':
			'''Repay'''
			demo_credit.repay()
			continue
		else:
			print ('Sorry,you enter invaild!\n')
			continue
	else:
		if enter_action == 'q':
			exit()
		else:
			print('Sorry,your enter invaild!\n')


 
