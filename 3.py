import re

str1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = re.sub('[,\.]', '', str1)
splits = str.split()
ans= [len(i) for i in splits]

print(ans)