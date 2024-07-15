import xml.etree.ElementTree as ET

miarbol = ET.parse('ejemplo.xml')

miraiz = miarbol.getroot()

print(miraiz.tag)
print(miraiz)
print("------")
print(miraiz[0].tag)
print(miraiz[1].tag)

print("-----")
for i in miraiz[0]:
    print(i.tag + ":" +i.text)
print("-----")
for i in miraiz[1]:
    print(i.tag + ":" +i.text)

print("--------")
for i in miraiz.findall("animal"):
    nombre = i.find('nombre').text
    print(nombre + "\n")

# nuevoarbol= ET.ElementTree()
nuevaraiz = ET.Element("Personas")

persona = ET.SubElement(nuevaraiz, "persona")
nombre = ET.SubElement(persona,"Javier")
nombre.text= "bbqhbdihbquwhbdfuhq"

nuevoarbol = ET.ElementTree(nuevaraiz)
nuevoarbol.write("nuevo.xml" , encoding="UTF-8" ,  xml_declaration= True)