import pickle

info_dict={'root':{'passwd':'python','balance':10000},
	'test':{'passwd':'test','balance':10000}}

blacklist=['blacklist']

f=open('user.info','wb')
pickle.dump(info_dict,f)
f.close()


pro_list=[['iphone', 6200], ['mac pro', 12000], ['bike', 800], ['book', 55], ['coffee', 31], ['windows pc', 4900]]
f=open('product.txt','wb')
pickle.dump(pro_list,f)
f.close()

f=open('blacklist.txt','wb')
pickle.dump(blacklist,f)
f.close()
