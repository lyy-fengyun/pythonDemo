#coding=utf-8
#!/usr/bin/python
import xml.sax
class InterBossHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.InterBoss=''
        self.version=''
        self.TestFlag=''
        self.BIPType=''
        self.BIPCode=''
        self.ActivityCode=''
        self.ActionCode=''
        self.RountingInfo=''
        self.OrigDemain=''
        self.RouteType=''
        self.Routing=''
        self.HomeDomain=''
        self.RouteValue