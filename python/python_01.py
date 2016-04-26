print "hello world!!"
print r"\\\n\\"
print 3>2
print "Hello %s"%"world"
print "%2d-%02d"%(3,1)
print "%.2f"%3.1415926
print "%s-0%s"%(3,1)
print "%s" %3.1415936

classmates = ["James","Bob","Tom"]
print classmates
print len(classmates)
print classmates[2]
print classmates[-1]
classmates.append("Adam")
print classmates
classmates.insert(0,"Tim")
print classmates
classmates.pop();
classmates.pop(0);
print classmates
s = ["c","cpp",["javaSE","javaEE"]]
print classmates[2][0]
l = []
print len(l)

classmates = ("James","Tim","Bob")
print classmates
classmates = ()
print classmates
t = (1)
print t
t = (1,)
print t

d = {"Tim":30,"Tom":45,"Vector":88}
print d["Tim"]
d["Adam"] = 12
print 'Adam'in d
print d
print d.get('NO')
print d.get('NO',-1)
print d.pop('Adam')
print d

s = set([1,2,3])
print s
s = set([1,2,3,2,4])
print s
s.add(8)
print 5 in s
s.remove(4)
t = set([4,6,8])
print s&t
print s|t
s = 'Hello world 86'
print s.isalnum()
print s.isalpha()
print s.isdigit()
print s.islower()
print s.istitle()
print s.isupper()
print s.isspace()
print s.upper()
print s.lower()
print s.title()
print s.capitalize()