#! /usr/bin/python3

from bs4 import BeautifulSoup

with open("fgo.html") as file:
  soup = BeautifulSoup(file.read())
  data = soup.findAll('tr')

  id = 0
  for d in data:
    if '<strong>Event Drops</strong>' in str(d):
      continue

    print("<li data-id=\"playthrough_0_%s\"><table>%s</table></li>" % (id , d))
    id += 1
    print("")