import re
def strip_str(str):
    bspaceRegex = re.compile(r'(\s+$)')
    fspaceRegex = re.compile(r'(^\s+)')
    str = bspaceRegex.sub('', str)
    str = fspaceRegex.sub('', str)
    return str

str = input("Enter your string")
print(strip_str(str))
