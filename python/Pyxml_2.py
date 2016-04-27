import xml.sax
class studentHandler(xml.sax.ContentHandler):
	def startDocument(self):
		print "start..."

	def endDocument(self):
		print 'end...'

	def startElement(self,name,attr):
		self.CurrentData = name
		if name == "student":
			print '****student****'
			title = attr['id']
			print 'id:', title

	def characters(self,content):
		if self.CurrentData == 'name':
			self.name = content
		elif self.CurrentData == 'age':
			self.age = content
		elif self.CurrentData == 'dob':
			self.dob = content

	def endElement(self,tag):
		if self.CurrentData == 'name':
			print self.name
		elif self.CurrentData == 'age':
			print self.age
		elif self.CurrentData == 'dob':
			print self.dob
		self.CurrentData = ''

if __name__ == '__main__':
	xml.sax.parse('students.xml',studentHandler())