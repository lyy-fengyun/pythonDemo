#! /usr/bin/env python
# -*- coding:utf-8 -*-

try:
    import xml.etree.cElementTree as ET
except importError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='crm.xml')
root = tree.getroot()
print root
print root.tag,root.attrib
data = {}
for elem in tree.iter():
    if elem.text[0] =='\n':
        print elem.tag+' {'+elem.text
    else:
        print '\t'+elem.tag+"="+elem.text

#data[elem.tag] = elem.text
#print data

