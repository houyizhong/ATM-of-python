#-*- coding:utf-8 -*-
#owner:houyizhong
#version:1.0

import pickle
import os

filename=os.path.abspath(__file__)
dirname=os.path.dirname(filename)
info_path=dirname+os.sep+'user.info'

def write_balance(data):
	f=open(info_path,'wb')
	pickle.dump(data,f)
	f.close()
