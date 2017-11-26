from gmail import *
# ramdom choice
from random import choice
file_names = ['li do 1.txt','li do 2.txt','li do 3.txt']
file_name = choice(file_names)

reasons =['Ebola',"dau bung",'dau dau']
reason = choice(reasons)
# read it
ld = open(file_name,encoding='utf-8')
text = ld.read()
ld.close()
text =text.replace('{{reason}}', reason)
# send it
gmail = GMail('i2fury4u@gmail.com','12345hai')
msg = Message('Test',\
        to='C4e13labhuynq@gmail.com',\
        html=text)
gmail.send(msg)
