from urllib.request import urlopen
from bs4 import BeautifulSoup
webb =urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content=webb.read().decode('utf8')
webb.close()
soup = BeautifulSoup(html_content,'html.parser')
table_new =soup.find('table','tableContent')
