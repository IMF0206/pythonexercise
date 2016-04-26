fo = open('foo.txt','wb')
#print 'file name: ',fo.name
#print 'closed? ',fo.closed
#print 'mode',fo.mode
#print 'space', fo.softspace
fo.write('runoob.com\nvery good site\n')
fo.close()
fo = open('foo.txt','r+')
str = fo.read(10)
print 'the words we read is:',str
position = fo.tell()
str = fo.read(10)
print 'the words we read is:',str
position = fo.seek(0,0)
str = fo.read(10)
print 'the words we read is:',str
fo.close()
#print 'closed?',fo.closed