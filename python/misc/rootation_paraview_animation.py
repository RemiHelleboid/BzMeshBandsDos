# import the simple module from the paraview
from paraview.simple import *
import numpy as np
import argparse
import inspect
# disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

si_extremas = [[-12.5891, -8.1794],
               [-8.30847, -1.66159e-13],
               [-4.54238, -2.71896e-14],
               [-3.96281, 0.0],
               [1.04034, 4.9053],
               [1.16998, 6.85878],
               [3.37964, 12.2698],
               [3.99022, 12.2698],
               [6.48798, 12.8557],
               [7.31058, 13.4927],
               [8.25655, 16.0562],
               [11.4688, 16.4623],
               [12.569, 18.7686],
               [12.569, 19.3298],
               [15.5224, 21.5633],
               [17.5502, 27.3715],
               [17.5502, 27.3715],
               [18.4023, 27.3941],
               [21.4196, 28.6273],
               [21.4516, 29.9285],
               [22.2918, 30.2796],
               [22.2918, 31.0066],
               [26.0339, 33.7144],
               [26.8845, 34.6376],
               [28.3037, 36.0478],
               [28.5333, 36.356],
               [29.3058, 37.5507],
               [29.3592, 43.4564],
               [33.2726, 43.9431],
               [33.6085, 43.9431],
               [35.1483, 43.9431],
               [35.8883, 44.497],
               [36.2965, 44.497],
               [36.2965, 44.533],
               [39.5456, 45.9688],
               [39.8383, 46.1416],
               [41.3132, 47.4013],
               [41.709, 48.0407],
               [42.3173, 49.2082],
               [43.8589, 50.619],
               [45.0952, 52.5127],
               [45.0952, 53.0229],
               [45.8357, 54.1446],
               [45.8872, 54.5142],
               [45.8872, 56.4409],
               [46.0035, 57.9422],
               [46.0846, 58.0097],
               [46.5917, 58.0097],
               [46.5917, 60.2646],
               [46.5917, 60.5861],
               [47.5444, 61.2098],
               [49.7131, 61.2098],
               [50.4511, 63.0419],
               [51.5336, 63.8502],
               [51.6383, 64.5733],
               [53.5386, 64.6788],
               [53.8414, 66.3079],
               [53.8414, 66.6578],
               [55.3743, 67.0306],
               [61.6536, 71.9235]]



def plot_iso_surface(filename_vtu, band_index, min_energy, max_energy, number_iso_values, out_file, nb_frames):

    print("------------------- COMPUTE THE ISO SURFACE ANIMATION ------------------- ")

    list_energies = np.linspace(min_energy, max_energy, number_iso_values)
    band_str = "band_" + str(band_index)

    min_energy = si_extremas[band_index][0] - 0.25
    max_energy = si_extremas[band_index][1] + 0.25

    print("band_index: ", band_index)
    print("min_energy: ", min_energy)
    print("max_energy: ", max_energy)

    # create a new 'XML Unstructured Grid Reader'
    medium_1_bz_meshvtu = XMLUnstructuredGridReader(registrationName='fine_1_bz_mesh.vtu', FileName=[
                                                    'fine_1_bz_mesh.vtu'])
    medium_1_bz_meshvtu.PointArrayStatus = ['band_0', 'band_1', 'band_2', 'band_3', 'band_4', 'band_5',
                                            'band_6', 'band_7', 'band_8', 'band_9', 'band_10', 'band_11', 'band_12', 'band_13', 'band_14', 'band_15']

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # get layout
    # layout2 = GetLayout()

    # --------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    # layout2.SetSize(1200, 1200)

    # -----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.0, 0.0, 4.5]
    renderView1.CameraFocalPoint = [0.0, 0.0, -2.361534228613564]
    renderView1.CameraParallelScale = 1.7320508075688772

    # get display properties
    medium_1_bz_meshvtuDisplay = GetDisplayProperties(
        medium_1_bz_meshvtu, view=renderView1)

    # set scalar coloring
    ColorBy(medium_1_bz_meshvtuDisplay, ('POINTS', band_str))

    # rescale color and/or opacity maps used to include current data range
    medium_1_bz_meshvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    medium_1_bz_meshvtuDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for band_str
    band_0LUT = GetColorTransferFunction(band_str)

    # get opacity transfer function/opacity map for band_str
    band_0PWF = GetOpacityTransferFunction(band_str)

    # rescale color and/or opacity maps used to exactly fit the current data range
    medium_1_bz_meshvtuDisplay.RescaleTransferFunctionToDataRange(False, True)

    # create a new 'Contour'
    contour1 = Contour(registrationName='Contour1', Input=medium_1_bz_meshvtu)
    contour1.ContourBy = ['POINTS', band_str]
    contour1.Isosurfaces = [-1000.379030287270895]
    contour1.PointMergeMethod = 'Uniform Binning'

    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0

    # get animation track
    contour1ContourValuesTrack = GetAnimationTrack(
        'ContourValues', index=-1, proxy=contour1)

    # create keyframes for this animation track

    # create a key frame
    keyFrame23966 = CompositeKeyFrame()
    keyFrame23966.KeyValues = [min_energy]

    # create a key frame
    keyFrame23967 = CompositeKeyFrame()
    keyFrame23967.KeyTime = 1.0
    keyFrame23967.KeyValues = [max_energy]

    # initialize the animation track
    contour1ContourValuesTrack.KeyFrames = [keyFrame23966, keyFrame23967]

    # get animation scene
    animationScene1 = GetAnimationScene()

    # show data in view
    contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'
    contour1Display.ColorArrayName = ['POINTS', band_str]
    contour1Display.LookupTable = band_0LUT
    contour1Display.SelectTCoordArray = 'None'
    contour1Display.SelectNormalArray = 'None'
    contour1Display.SelectTangentArray = 'None'
    contour1Display.OSPRayScaleArray = band_str
    contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour1Display.SelectOrientationVectors = 'None'
    contour1Display.ScaleFactor = 1.1564823173178673e-19
    contour1Display.SelectScaleArray = band_str
    contour1Display.GlyphType = 'Arrow'
    contour1Display.GlyphTableIndexArray = band_str
    contour1Display.GaussianRadius = 5.782411586589336e-21
    contour1Display.SetScaleArray = ['POINTS', band_str]
    contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour1Display.OpacityArray = ['POINTS', band_str]
    contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
    contour1Display.DataAxesGrid = 'GridAxesRepresentation'
    contour1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    contour1Display.ScaleTransferFunction.Points = [
        -8.17501889820678, 0.0, 0.5, 0.0, -8.173066139221191, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    contour1Display.OpacityTransferFunction.Points = [
        -8.17501889820678, 0.0, 0.5, 0.0, -8.173066139221191, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(medium_1_bz_meshvtu, renderView1)

    SetProperties(renderView1, Background=[0, 0, 0])
    renderView1.Update()

    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, False)

    # Properties modified on animationScene1
    animationScene1.NumberOfFrames = nb_frames

    # update the view to ensure updated data information
    renderView1.Update()

    # # get animation scene
    # animationScene1 = GetAnimationScene()
    
    # # reset view to fit data bounds
    # # renderView1.ResetCamera(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, True)
    
    # create a key frame


    # # get camera animation track for the view
    cameraAnimationCue1 = GetCameraTrack(view=renderView1)

    
    # create a key frame
    keyFrame10297 = CameraKeyFrame()
    keyFrame10297.Position = [-4.302322923455295, 0.0, 0.0]
    keyFrame10297.FocalPoint = [2.389807506447166, 0.0, 0.0]
    keyFrame10297.ViewUp = [0.0, 0.0, 1.0]
    keyFrame10297.ParallelScale = 1.7320508075688772
    keyFrame10297.PositionPathPoints = [-4.30232, 0.0, 0.0, -2.6824526443328667, -3.363689223651854, 0.0, 0.95735626457893, -4.194451855138103, 0.0, 3.8762563797539356, -1.8667066884802535, 0.0, 3.8762563797539364, 1.8667066884802517, 0.0, 0.957356264578932, 4.194451855138103, 0.0, -2.6824526443328653, 3.363689223651855, 0.0]
    keyFrame10297.FocalPathPoints = [0.0, 0.0, 0.0]
    keyFrame10297.ClosedPositionPath = 1

    # create a key frame
    keyFrame10298 = CameraKeyFrame()
    keyFrame10298.KeyTime = 1.0
    keyFrame10298.Position = [-4.302322923455295, 0.0, 0.0]
    keyFrame10298.FocalPoint = [2.389807506447166, 0.0, 0.0]
    keyFrame10298.ViewUp = [0.0, 0.0, 1.0]
    keyFrame10298.ParallelScale = 1.7320508075688772

    # initialize the animation track
    cameraAnimationCue1.Mode = 'Path-based'
    cameraAnimationCue1.KeyFrames = [keyFrame10297, keyFrame10298]


    # save animation
    SaveAnimation(out_file, renderView1, ImageResolution=[1920, 1080],
                #   FontScaling='Do not scale fonts',
                  FrameRate=30,
                  FrameWindow=[0, nb_frames-1])


def print_agrs(band_file, min_energy, max_energy, band_index):
    print("band_file: ", band_file)
    print("band_index: ", band_index)
    print("min_energy: ", min_energy)
    print("max_energy: ", max_energy)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='PROG', description='Test')
    parser.add_argument("-f", "--filename", dest="file",
                        required=True, type=str)
    parser.add_argument("-b", "--index-band", dest="band",
                        required=False, type=int, default=0)
    parser.add_argument("-m", "--min-energy", dest="min_iso_energy",
                        required=False, type=float, default=-10)
    parser.add_argument("-M", "--max-energy", dest="max_iso_energy",
                        required=False, type=float, default=10)
    parser.add_argument("-n", "--number_iso_values", dest="number_iso_values",
                        required=False, type=int, default=10)
    parser.add_argument("-F", "--nb-frame", dest="nb_frames",
                        required=False, type=int, default=120)
    parser.add_argument("-o", dest="out_dir", required=False,
                        type=str, default="results/")
    args = vars(parser.parse_args())

    bands_file = args["file"]
    bands_index = args["band"]
    min_iso_energy = args["min_iso_energy"]
    max_iso_energy = args["max_iso_energy"]
    number_iso_values = args["number_iso_values"]
    nb_frames = args["nb_frames"]
    out_dir = args["out_dir"]

    out_file = out_dir + "/Si_steady_animation_" + \
        f"{bands_index:03d}" + "th_band_iso.avi"

    # print_agrs(bands_file, min_iso_energy, max_iso_energy, bands_index)

    plot_iso_surface(bands_file, bands_index, min_iso_energy,
                     max_iso_energy, number_iso_values, out_file, nb_frames)
