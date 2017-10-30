import time

test_time=time.strftime('%Y%m%d%H%M%S')
price=1000
stock='dog'

f=open('test.log','a')
f.write('{0}\t{1}\t{2}\n'.format(test_time,stock,price))
f.close()

'''
f=open('credit.log','w')
f.write('{0}\t{1}\t{2}\n'.format('trans_time','detail','money'))
f.close()
'''
