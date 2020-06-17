import re 

res = re.match('AV', 'AVVVVVVVVAAVVAVAVA AJSDHASHDASJHDJH')
print(res.group())
print(res.start())
print(res.end())


res = re.search('lab', 'qqqqblalblalblalbllal lablalb lablaba asd')
print(res.group())

res = re.findall('python', "python code - the best code forever Python python")
print(res)
