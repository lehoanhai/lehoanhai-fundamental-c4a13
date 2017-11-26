from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
website = urlopen(url)
html_content = website.read().decode('utf8')
# put html_content into soup
soup = BeautifulSoup(html_content,"html.parser")
# 3. Find table data
table_data = soup.find('table',id = 'tableContent')
# temp = open('temp.html','w')
# temp.write(table_data.prettify())
# temp.close()

# 4. Find all trs
trs = table_data.find_all('tr')

# tr = trs[0]

data_list=[]

for tr in trs:
    tds = tr.find_all('td')
    data = {}
    # td = tds[0]
    for index, td in enumerate(tds):
        content = td.string
        if content != None:
            if index ==0:
                data['title'] = content.strip()
            elif index==1:
                data['Quy 2 - 2016'] = content
            # print(content.strip())
            elif index == 2:
                data['Quy 1 - 2017'] = content
    if data != {}:
        data_list.append(data)
# print (data)
print(data_list)
