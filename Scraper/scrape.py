import csv
import requests
import urllib
from bs4 import BeautifulSoup

url = 'http://www.indianrail.gov.in/mail_express_trn_list.html'
#response = requests.get(url)
#html = response.content

html = html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'table_border'})

# print table.prettify()

# print table.findAll('tr')  List of tr's is returned

# for row in table.findAll('tr'):
#     print row.prettify()

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '').lstrip()
        print text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)


outfile = open("./file.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Train Number", "Train Name", "Train Source Stn", "Source Dep. Time", "Train Destination Stn", "Dest. Arr. Time"])
writer.writerows(list_of_rows)





# list_of_rows = []
# for row in table.findAll('tr')[1:]:
#     list_of_cells = []
#     for cell in row.findAll('td'):
#         text = cell.text.replace('&nbsp;', '')
#         list_of_cells.append(text)
#     list_of_rows.append(list_of_cells)

# outfile = open("./inmates.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
# writer.writerows(list_of_rows)
