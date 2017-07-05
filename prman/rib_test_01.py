import prman, getpass, time
ri = prman.Ri()
#fileName = 'C:/mayaProjs/testProj/renderman/ribarchives/ribTest_01.rib'
filename = "__render"

#ri.Begin(fileName)
ri.Begin(ri.RENDER)

ri.ArchiveRecord(ri.COMMENT, 'File ' +filename)# ri.ArchiveRecord ¡A¼g¤Jµù¸Ñ
ri.ArchiveRecord(ri.COMMENT, "Created by " + getpass.getuser())
ri.ArchiveRecord(ri.COMMENT, "Creation Date: " +time.ctime(time.time()))


ri.Display("Teapot.exr","framebuffer","rgba")
ri.Format(500,500,1)
ri.Projection(ri.PERSPECTIVE,{"fov":[35]})

ri.WorldBegin()

ri.Sphere(1,-1,1,360)

ri.Color([1,1,1])

ri.Opacity([1,1,1])

ri.TransformBegin()

ri.AttributeBegin()

ri.Color([0,1,1])

ri.Opacity([0.2,0.2,0.2])

ri.Sphere(1,-1,1,360)



ri.AttributeEnd()





ri.TransformEnd()
ri.WorldEnd()





ri.End()