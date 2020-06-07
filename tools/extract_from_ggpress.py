#! /usr/bin/python3

from bs4 import BeautifulSoup

with open("__path_to_data.html__from_fgo gamepress") as file:
  soup = BeautifulSoup(file.read())
  data = soup.findAll('tr')

  for d in data:
    if '<strong>Event Drops</strong>' in str(d):
      continue
    print(d)
    print("")