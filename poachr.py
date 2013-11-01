#!/usr/bin/python
import argparse
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os, os.path

parser = argparse.ArgumentParser()
parser.add_argument('timestamp')

args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))

response = open(script_path + '/data/snapshots/' + args.timestamp + '.html', 'r');

html = response.read()

soup = BeautifulSoup(html)

buddyicons = soup.find('div', 'InfoCase').findAll('img')

names = []
nsids = []

for buddyicon in buddyicons:
	names.append(buddyicon["alt"])
	x = re.search('buddyicons/(.*).jpg', buddyicon["src"])
	nsids.append(x.group(1))

name_file = open(script_path + '/' + 'names.txt', 'w')

for name in names:
  name_file.write("%s\n" % name)

name_file.close()

nsid_file = open(script_path + '/' + 'nsids.txt', 'w')

for nsid in nsids:
  nsid_file.write("%s\n" % nsid)

nsid_file.close()