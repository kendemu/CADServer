import FreeCAD
import FreeCADGui
from xml.dom import minidom
import inspect
import Mesh

FreeCADGui.setupWithoutGUI()
FreeCAD.loadFile(u"C:/Users/isekaitenseiproject/Downloads/happymini_body.stp")

documents = FreeCAD.activeDocument()
members = inspect.getmembers(documents)

doc = minidom.parseString(members[3][1])
parts = doc.getElementsByTagName("Object")
__objs__ = []


typelist = ["Part::Feature", "App::Part"]

for p in parts:
    if p.attributes['type'].value in typelist:
	       __objs__.append(documents.getObject(p.attributes['name'].value))

print("exporting")

Mesh.export(__objs__, u"C:/Users/isekaitenseiproject/Downloads/happymini-cad.obj")
del __objs__
