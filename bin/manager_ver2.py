import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR=BASE_DIR+os.sep+'core'

sys.path.append(BASE_DIR)
sys.path.append(CORE_DIR)
from core import demo_manage

action_list=['Add account','Edit account','Block account']

while True:
	for index,item in enumerate(action_list):
		print(index+1,item)
	print('"q" is exit.')
	enter_action=input('Enter your choice:')

	if enter_action.isdigit():
		if enter_action == '1':
			demo_manage.add_account()
			continue
		elif enter_action == '2':
			demo_manage.change_account()
			continue
		elif enter_action == '3':
			demo_manage.blacklist()
			continue
	else:
		if enter_action == 'q':
			exit()
		else:
			print('Sorry,your enter invaild!\n')

#core.demo_manage.io()
