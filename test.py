import xml.etree.ElementTree as et
tree = et.parse('jobs.xml')
root = tree.getroot()

# to print the root element
print(root.tag)

# to print the root attribute
print(root.attrib)

# to print nodes in xml with the text of each tag
for k in range(0,3):
    for i in root[k]:
        print(i.tag)
        print(i.text)

# to find the text of a particular tag within each record
for x in root.findall('job'):
    company_name = x.find('city').text
    ref_number = x.find('referencenumber').text
    print(company_name,ref_number)

# to find the text/name of a particular tag
print(root[0][2].text)
print(root[0][2].tag)




