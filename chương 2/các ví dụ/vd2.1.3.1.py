import xml.dom.minidom

def main():
    path="D:/Python nâng cao/chương 2/các ví dụ/employee.xml"
    doc=xml.dom.minidom.parse(path)
    print(doc.nodeName)
    print(doc.firstChild.tagName)

expertise = doc.geELementsByTagName('expertise')
print("%d exepertise:" % expertise.length)
for skill in expertise:
    print(skill.getAttribute("name"))
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("name", "AI")
    doc.firstChild.appendChild(newexpertise)
    print(" ")
    expertise = doc.getElementsByTagName("expertise")
    print("%d expertise:" % expertise.length)
for skill in expertise:
    print(skill.getAttribute("name"))
if __name__=="__main__":
    main();
