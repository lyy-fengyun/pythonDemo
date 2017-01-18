#!/usr/bin/python
#-*- coding:utf-8 -*-

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f','--file',dest='filename',
                  help='write report to FILE', metavar='file')
parser.add_option('-q','--quit',action='store_false',dest='verbose',default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
