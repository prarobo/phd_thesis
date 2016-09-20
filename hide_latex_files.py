#!/usr/bin/python

FILE_EXTN = [
".aux",
".acn",
".bbl",
".glo",
".log",
".ist",
".out",
".gz",
".lot",
".toc",
".glg",
".alg",
".gls",
".acr",
".blg",
".backup"]

import glob
import os
import pprint

filepath = os.path.realpath(__file__)
filedir = os.path.dirname(filepath)

files = []
for e in FILE_EXTN:
  files.extend(glob.glob(os.path.join(filedir,'*'+e)))

pprint.pprint(files)

file_handle = open(os.path.join(filedir, '.hidden'), 'w')

for l in files:
  file_handle.write("%s\n" % os.path.basename(l))
