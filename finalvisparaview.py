# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# This was produced in paraview by:
# Oliver Pye (n9703977)
# o.pye@connect.qut.edu.au
# Queensland University of Technology
# November 2018
# ----------------------------------------------------------------

################################ NOTE ##############################
# Before use, the path of the data files must be changed on lines:
# 53 & 63

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [610, 553]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-1.6284265408999978, -0.5021853210000025, -0.0679689377999999]
renderView1.StereoType = 0
renderView1.CameraPosition = [-1.6284265408999978, -0.5021853210000025, 232.01706176549934]
renderView1.CameraFocalPoint = [-1.6284265408999978, -0.5021853210000025, -0.0679689377999999]
renderView1.CameraParallelScale = 60.068026029217144
renderView1.Background = [0.0, 0.0, 0.0]

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [610, 553]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, 0.0, -1e-20]
renderView2.StereoType = 0
renderView2.CameraPosition = [0.0, 0.0, 200.7639004871873]
renderView2.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView2.CameraParallelScale = 51.96152101515131
renderView2.Background = [0.0, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
cSVReader2 = CSVReader(FileName=['~/plaindata.txt'])
cSVReader2.FieldDelimiterCharacters = ' '

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=cSVReader2)
tableToPoints2.XColumn = 'x'
tableToPoints2.YColumn = 'y'
tableToPoints2.ZColumn = 'z'

# create a new 'CSV Reader'
cSVReader1 = CSVReader(FileName=['~/height_data.txt'])
cSVReader1.FieldDelimiterCharacters = ' '

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=cSVReader1)
tableToPoints1.XColumn = 'x'
tableToPoints1.YColumn = 'y'
tableToPoints1.ZColumn = 'z'

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'temp'
tempLUT = GetColorTransferFunction('temp')
tempLUT.RGBPoints = [-0.000810898, 0.0, 0.0, 0.0, -0.00027083984596911696, 0.501960784314, 0.0, 0.0, 0.0002692183080617661, 1.0, 0.501960784314, 0.0, 0.0008108982583509999, 1.0, 1.0, 1.0]
tempLUT.ColorSpace = 'RGB'
tempLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temp'
tempPWF = GetOpacityTransferFunction('temp')
tempPWF.Points = [-0.000810898, 0.0, 0.5, 0.0, 0.0008108982583509999, 1.0, 0.5, 0.0]
tempPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tableToPoints1
tableToPoints1Display = Show(tableToPoints1, renderView1)
# trace defaults for the display properties.
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = ['POINTS', 'temp']
tableToPoints1Display.LookupTable = tempLUT
tableToPoints1Display.OSPRayScaleArray = 'temp'
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.SelectOrientationVectors = 'None'
tableToPoints1Display.ScaleFactor = 7.0902835594599996
tableToPoints1Display.SelectScaleArray = 'None'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.GlyphTableIndexArray = 'None'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# show color legend
tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tempLUT in view renderView1
tempLUTColorBar = GetScalarBar(tempLUT, renderView1)
tempLUTColorBar.Title = 'temp'
tempLUTColorBar.ComponentTitle = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tableToPoints2
tableToPoints2Display = Show(tableToPoints2, renderView2)
# trace defaults for the display properties.
tableToPoints2Display.Representation = 'Surface'
tableToPoints2Display.ColorArrayName = ['POINTS', 'temp']
tableToPoints2Display.LookupTable = tempLUT
tableToPoints2Display.OSPRayScaleArray = 'temp'
tableToPoints2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints2Display.SelectOrientationVectors = 'None'
tableToPoints2Display.ScaleFactor = 5.9999996821
tableToPoints2Display.SelectScaleArray = 'None'
tableToPoints2Display.GlyphType = 'Arrow'
tableToPoints2Display.GlyphTableIndexArray = 'None'
tableToPoints2Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints2Display.PolarAxes = 'PolarAxesRepresentation'

# show color legend
tableToPoints2Display.SetScalarBarVisibility(renderView2, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tempLUT in view renderView2
tempLUTColorBar_1 = GetScalarBar(tempLUT, renderView2)
tempLUTColorBar_1.Title = 'Temperature'
tempLUTColorBar_1.ComponentTitle = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(tableToPoints2)
# ----------------------------------------------------------------
