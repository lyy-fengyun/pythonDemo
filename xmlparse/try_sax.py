import  string
import xml.sax from xml.sax.handler
class QuotationHandler(ContentHandler):
    """Crude extractor for quotations.dtd compliant XML document"""
    def __init__(self):
        self.in_quote = 0
        self.thisquote = ''
    def startDocument(self):
        print'--- Begin Document ---'
    def startElement(self, name, attrs):
        if name == 'quotation':
            print 'QUOTATION:'
            self.in_quote = 1
        else:
            self.thisquote = self.thisquote + '{'
    def endElement(self, name):
        if name == 'quotation':
            print string.join(string.split(self.thisquote[:230]))+'...',
            print '('+str(len(self.thisquote))+' bytes)\n'
            self.thisquote = ''
            self.in_quote = 0
        else:
            self.thisquote = self.thisquote + '}'
    def characters(self, ch):
        if self.in_quote:
        self.thisquote = self.thisquote + ch
if __name__ == '__main__':
    parser = xml.sax.make_parser()
    handler = QuotationHandler()
    parser.setContentHandler(handler)
    parser.parse("sample.xml")