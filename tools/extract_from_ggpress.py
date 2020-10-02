#! /usr/bin/python3

from bs4 import BeautifulSoup

with open("fgo.html") as file:
  soup = BeautifulSoup(file.read())
  data = soup.findAll('tr')

  id = 0
  for d in data:
    if '<strong>Event Drops</strong>' in str(d):
      continue

    # TODO for some reason, if there are newlines in between the "li -> /li" it doesn't render...?
    print(("<li data-id=\"playthrough_0_%s\"><table>%s</table></li>" % (id , d)).replace("\n", ""))
    id += 1
    print("")