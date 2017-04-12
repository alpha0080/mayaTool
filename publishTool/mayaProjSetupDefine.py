# -*- coding: utf-8 -*-
# fileName, workspace.mel
# define Maya project setup
#
# release Note
#2017/03/13 according Maya Original Setup
#

class workSpaceDefine():
    
    
    def mayaOriginalProjSetup(self,option):
        
        if self.option == "maya2017":
        

            self.mayaProjSetupDefine = {{"fluidCache":"cache/nCache/fluid"},
                                        {"JT_ATF":"data"},
                                        {"images":"images"},
                                        {"offlineEdit":"scenes/edits"},
                                        {"STEP_ATF Export":"data"},
                                        {"furShadowMap":"renderData/fur/furShadowMap"},
                                        {"INVENTOR_ATF Export":"data"},
                                        {"scripts":"scripts"},
                                        {"STL_ATF":"data"},
                                        {"DAE_FBX":"data"},
                                        {"shaders":"renderData/shaders"},
                                        {"NX_ATF":"data"},
                                        {"furFiles":"renderData/fur/furFiles"},
                                        {"CATIAV5_ATF Export":"data"},
                                        {"OBJ":"data"},
                                        {"FBX export":"data"},
                                        {"furEqualMap":"renderData/fur/furEqualMap"},
                                        {"BIF":"data"},
                                        {"DAE_FBX export":"data"},
                                        {"CATIAV5_ATF":"data"},
                                        {"SAT_ATF Export":"data"},
                                        {"movie":"movies"},
                                        {"ASS Export":"data"},
                                        {"move":"data"},
                                        {"mayaAscii":"scenes"},
                                        {"autoSave":"autosave"},
                                        {"NX_ATF Export":"data"},
                                        {"sound":"sound"},
                                        {"mayaBinary":"scenes"},
                                        {"timeEditor":"Time Editor"},
                                        {"JT_ATF Export":"data"},
                                        {"iprImages":"renderData/iprImages"},
                                        {"FBX":"data"},
                                        {"renderData":"renderData"},
                                        {"CATIAV4_ATF":"data"},
                                        {"fileCache":"cache/nCache"},
                                        {"eps":"data"},
                                        {"3dPaintTextures":"sourceimages/3dPaintTextures"},
                                        {"STL_ATF Export":"data"},
                                        {"mel":"scripts"},
                                        {"translatorData":"data"},
                                        {"particles":"cache/particles"},
                                        {"scene":"scenes"},
                                        {"SAT_ATF":"data"},
                                        {"PROE_ATF":"data"},
                                        {"WIRE_ATF Export":"data"},
                                        {"sourceImages":"sourceimages"},
                                        {"clips":"clips"},
                                        {"furImages":"renderData/fur/furImages"},
                                        {"INVENTOR_ATF":"data"},
                                        {"STEP_ATF":"data"},
                                        {"depth":"renderData/depth"},
                                        {"IGES_ATF Export":"data"},
                                        {"sceneAssembly":"sceneAssembly"},
                                        {"IGES_ATF":"data"},
                                        {"teClipExports":"Time Editor/Clip Exports"},
                                        {"ASS":"data"},
                                        {"audio":"sound"},
                                        {"bifrostCache":"cache/bifrost"},
                                        {"Alembic":"data"},
                                        {"illustrator":"data"},
                                        {"diskCache":"data"},
                                        {"WIRE_ATF":"data"},
                                        {"templates":"assets"},
                                        {"OBJexport":"data"},
                                        {"furAttrMap":"renderData/fur/furAttrMap"},
                                        {"RIB_Archive":"data"}}



defineSetup = workSpaceDefine.mayaOriginalProjSetup('maya2017')

#workspaceDefine.mayaOriginalProjSetup('maya2017')