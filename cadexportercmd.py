import FreeCAD
import FreeCADGui
from xml.dom import minidom
import inspect
import Mesh
import sys
import os


#FreeCADGui.setupWithoutGUI()
path = os.getcwd + "/" + sys.argv[1]
print(path)                            

FreeCAD.loadFile(path)

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


exportfile = sys.argv[1].strip(".stp") + ".obj"
exportpath = os.getcwd() + "/" + export


Mesh.export(__objs__, exportpath)
del __objs__
