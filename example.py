import typecode

x = '$%///*++;%////*++;///++++;///*++;///*+++;-%////*;$@/*+;+++;///;@?-++;%/*++;?'

q = typecode.TypeCode()
q.init(x)
print('\x1b[0;93mLanguages\x1b[0m:')

for lang in q.info_languages:
    print(f'  {lang}')

print('\n\x1b[0;92mBranches\x1b[0m:')

for branch in q.info_branches:
    print(f'  {branch}')

print('\n\x1b[0;92mOperating Systems\x1b[0m:')

for os in q.info_operating_systems:
    print(f'  {os}')