#! /usr/bin/env python
# -*- coding:utf-8 -*-
from xml.etree import ElementTree as et;
import json

#从xml文件读取结点 转换为json格式，并保存到文件中
print('read node from xmlfile, transfer them to json, and save into jsonFile:')
root=et.parse("./crm.xml");
output=''
f=open('./crm.json','a');
for each in root.getiterator("person"):
    tempDict=each.attrib
    for childNode in each.getchildren():
        tempDict[childNode.tag]=childNode.text
    tempJson=json.dumps(tempDict,ensure_ascii=False)
    print(tempJson)
    output = tempJson
    f.write(tempJson+"\n");
f.close()

#从json文件中读取，并打印
print('read json from jsonfile:')
for eachJson in open('./crm.json','r'):
    tempStr=json.loads(eachJson);
    print(tempStr)