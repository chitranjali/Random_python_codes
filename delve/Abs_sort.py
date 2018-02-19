'''Sort on absolute values'''

l = [-4, -6, -5, 1, 4, 5]
#Key will apply the function to each ele on list
#key is like a function
s_li = sorted(l,key=abs)
print(s_li)