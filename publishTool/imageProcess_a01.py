import maya.cmds as cmds
import ice,os


imageFolder = "C:/temp/images"


os.listdir(imageFolder)

#imageReadFormat = ['tif','tiff','exr','EXR','gz','tga','TGA','bmp','BMP','gif','GIF','tex','tx','jpg','png','PNG','JPG','TEX']
imageReadFormat = ['exr','EXR','tex','TEX','tif']

imageSaveFormat = {'tif8':'ice.constants.FMT_TIFF8',
                   'tif16':'ice.constants.FMT_TIFF16',
                   'tifFloat':'ice.constants.FMT_TIFFFLOAT',
                   'exrHalf':'ice.constants.FMT_EXRHALF',
                   'exrFloat':'ice.constants.FMT_EXRFLOAT',
                   'exrUINT32':'ice.constants.FMT_EXRUINT32',
                   'png':'ice.constants.FMT_PNG',
                   'jpg':'ice.constants.FMT_JPEG'}




               
for i in os.listdir(imageFolder):
    if i.split('.')[-1] in imageReadFormat:
        imageFullName = imageFolder + '/' + i
        imageLoad = ice.Load(imageFullName)
        #print imageFullName
        imageDataBox = imageLoad.DataBox()  #xmin, xmax, ymin, ymax]
        imageChannel = imageLoad.Ply()
        imageMetaData = imageLoad.GetMetaData()
        print imageMetaData
      ##  fileName = 'image.tif'
      #  image = ice.Load(fileName)
        #print imageLoad.DataBox()
        
