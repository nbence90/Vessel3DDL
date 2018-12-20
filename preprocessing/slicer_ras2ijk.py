# Get the fiducial node 
fiducialNode = getNode('F') 

# Get the volume for the first data point 
volumeID = fiducialNode.GetNthFiducialAssociatedNodeID(0) 

# Set up coordinates 
coordsRAS = [0,0,0,0] 
coordsXYZ = [0,0,0] 

# Get RAS coordinates (saved in list coordsRAS) 
fiducialNode.GetNthFiducialWorldCoordinates(0, coordsRAS) 

# Don't need the last data point for our purposes 
del coordsRAS[-1] 

# This bit here is taken and modified from the dataprobe.py slicer module. 
sliceNode = slicer.mrmlScene.GetNthNodeByClass(0, 'vtkMRMLSliceNode') 
appLogic = slicer.app.applicationLogic() 
sliceLogic = appLogic.GetSliceLogic(sliceNode) 
layerLogic = sliceLogic.GetLabelLayer() 

# Get the xyz coordinates 
slicer.vtkMRMLAbstractSliceViewDisplayableManager.ConvertRASToXYZ(sliceNode,coordsRAS,coordsXYZ) 

# Get the IJK coordinates 
xyToIJK = layerLogic.GetXYToIJKTransform() 
coordsIJK = xyToIJK.TransformDoublePoint(coordsXYZ) 

# Make into int 
coordsIJK = map(int, coordsIJK) 

print coordsRAS 
print coordsXYZ 
print coordsIJK 
