import FreeCAD
from xml.dom import minidom
import inspect
import ImportGui
import Mesh

App.newDocument("Unnamed1")
App.setActiveDocument("Unnamed1")
App.ActiveDocument=App.getDocument("Unnamed1")
Gui.ActiveDocument=Gui.getDocument("Unnamed1")

ImportGui.insert(u"C:/Users/isekaitenseiproject/Downloads/happymini_body.stp","Unnamed")
inspect.getmembers(FreeCAD.getDocument("Unnamed1"))
members = inspect.getmembers(FreeCAD.getDocument("Unnamed1"))

doc = minidom.parseString(members[3][1])
parts = doc.getElementsByTagName("Object")
__objs__ = []


for p in parts:
	__objs__.append(FreeCAD.getDocument("Unnamed1").getObject(p.attributes['name'].value))

Mesh.export(__obj__, u"C:/Users/isekaitenseiproject/Downloads/happymini-cad.obj")
del __obj__
