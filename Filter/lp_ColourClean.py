# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named lp_ColourCleanExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from lp_ColourCleanExt import *
except ImportError:
    pass

def getPluginID():
    return "lp_ColourClean"

def getLabel():
    return "lp_ColourClean"

def getVersion():
    return 1

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "Cleans channels in different colourspaces, e.g. to cleanup noise in a screen.\n\nINPUTS\nimg = connect the main plate you want to clean\nmask = masks the effect by a connected alpha-channel\n\nHOW TO USE IT\nJust hook up an image, from here on it\'s straight forward. Choose which colourspace you want to work in, choose which cannels you want to clean and choose the operation that should be used.\nBack in the day, I liked to use a media on colourchannels for greenscreens, as this virtually can help with low colour subsampling. Usually you never want to clean in the luma-components, but you never know.\nJust make sure to not clean in all channels, else it\'s nothing but a common blur or median :)\n\nHOW DOES IT WORK\nA colourspace transformation and a blue/median of the given channels, not more not less :)"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.userNatron = lastNode.createPageParam("userNatron", "Controls")
    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessR", "R")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Processes red component.\nIf you e.g. choose YUV colourspace, it\'s applied to Y.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessR = param
    del param

    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessG", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Processes green component.\nIf you e.g. choose YUV colourspace, it\'s applied to U.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessG = param
    del param

    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessB", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Processes blue component.\nIf you e.g. choose YUV colourspace, it\'s applied to V.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessB = param
    del param

    param = lastNode.createChoiceParam("c_operation", "operation")
    entries = [ ("Blur", ""),
    ("Median", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Chooses which kinda operation should be used to clean the channels.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.c_operation = param
    del param

    param = lastNode.createChoiceParam("Blur1filter", "blur filter")
    param.setDefaultValue(1)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Filter for the blur operation only. The quasi-Gaussian filter should be appropriate in most cases. The Gaussian filter is more isotropic (its impulse response has rotational symmetry), but slower.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1filter = param
    del param

    param = lastNode.createChoiceParam("cspace", "colourspace")
    entries = [ ("YUV", ""),
    ("YPbPr", ""),
    ("YCbCr", ""),
    ("HSV", ""),
    ("RGB", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Chooses the colourspace in which the cleaning should be applied.\nUsually you don\'t want to clean in all channels, so make sure to enable only the right ones above; e.g., if you wanted to work in YUV it makes sense to not clean in Y.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.cspace = param
    del param

    param = lastNode.createDouble2DParam("Blur1size", "Size")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(20, 1)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Size of the blur or median operation. (note: median works not in axis, so if you hit the 2 to only the w value will be used)")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(9.529999999999999, 0)
    param.setValue(9.529999999999999, 1)
    lastNode.Blur1size = param
    del param

    param = lastNode.createSeparatorParam("sep01", " ")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp(" ")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createBooleanParam("invmask", "invert mask")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Inverts the connected mask.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.invmask = param
    del param

    param = lastNode.createStringParam("credit", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("lp_ColourClean v1.0\n(c) 2016 by lucas pfaff")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.credit = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['userNatron', 'Node', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "RGBToYPbPr7091"
    lastNode = app.createNode("net.sf.openfx.RGBToYPbPr709", 1, group)
    lastNode.setScriptName("RGBToYPbPr7091")
    lastNode.setLabel("RGBToYPbPr7091")
    lastNode.setPosition(2311, 402)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToYPbPr7091 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "RGBToYPbPr7091"

    # Start of node "RGBToHSV1"
    lastNode = app.createNode("net.sf.openfx.RGBToHSV", 1, group)
    lastNode.setScriptName("RGBToHSV1")
    lastNode.setLabel("RGBToHSV1")
    lastNode.setPosition(2934, 411)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToHSV1 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "RGBToHSV1"

    # Start of node "RGBToYUV7091"
    lastNode = app.createNode("net.sf.openfx.RGBToYUV709", 1, group)
    lastNode.setScriptName("RGBToYUV7091")
    lastNode.setLabel("RGBToYUV7091")
    lastNode.setPosition(2030, 409)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToYUV7091 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "RGBToYUV7091"

    # Start of node "RGBToYCbCr7091"
    lastNode = app.createNode("net.sf.openfx.RGBToYCbCr709", 1, group)
    lastNode.setScriptName("RGBToYCbCr7091")
    lastNode.setLabel("RGBToYCbCr7091")
    lastNode.setPosition(2617, 418)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToYCbCr7091 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "RGBToYCbCr7091"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(2018, 536)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9.529999999999999, 0)
        param.setValue(9.529999999999999, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("Nearest")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(2063, 317)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(2344, 317)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(2650, 317)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(2979, 312)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Blur2"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur2")
    lastNode.setLabel("Blur2")
    lastNode.setPosition(2299, 534)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur2 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9.529999999999999, 0)
        param.setValue(9.529999999999999, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("Nearest")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur2"

    # Start of node "Median1"
    lastNode = app.createNode("net.sf.cimg.CImgMedian", 2, group)
    lastNode.setScriptName("Median1")
    lastNode.setLabel("Median1")
    lastNode.setPosition(2163, 537)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupMedian1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9, 0)
        del param

    del lastNode
    # End of node "Median1"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(2018, 692)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "switch_cspace"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("switch_cspace")
    lastNode.setLabel("switch_cspace")
    lastNode.setPosition(2018, 1008)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupswitch_cspace = lastNode

    del lastNode
    # End of node "switch_cspace"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(2018, 1273)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "img"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("img")
    lastNode.setLabel("img")
    lastNode.setPosition(2018, 160)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupimg = lastNode

    del lastNode
    # End of node "img"

    # Start of node "YUVToRGB7091"
    lastNode = app.createNode("net.sf.openfx.YUVToRGB709", 1, group)
    lastNode.setScriptName("YUVToRGB7091")
    lastNode.setLabel("YUVToRGB7091")
    lastNode.setPosition(2030, 816)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupYUVToRGB7091 = lastNode

    del lastNode
    # End of node "YUVToRGB7091"

    # Start of node "mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("mask")
    lastNode.setLabel("mask")
    lastNode.setPosition(3719, 155)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupmask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "mask"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(3719, 458)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(3719, 319)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("clampWhite")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade1"

    # Start of node "Blur3"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur3")
    lastNode.setLabel("Blur3")
    lastNode.setPosition(2605, 533)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur3 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9.529999999999999, 0)
        param.setValue(9.529999999999999, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("Nearest")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur3"

    # Start of node "Median2"
    lastNode = app.createNode("net.sf.cimg.CImgMedian", 2, group)
    lastNode.setScriptName("Median2")
    lastNode.setLabel("Median2")
    lastNode.setPosition(2450, 532)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupMedian2 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9, 0)
        del param

    del lastNode
    # End of node "Median2"

    # Start of node "Blur4"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur4")
    lastNode.setLabel("Blur4")
    lastNode.setPosition(2934, 529)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur4 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9.529999999999999, 0)
        param.setValue(9.529999999999999, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("Nearest")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur4"

    # Start of node "Median3"
    lastNode = app.createNode("net.sf.cimg.CImgMedian", 2, group)
    lastNode.setScriptName("Median3")
    lastNode.setLabel("Median3")
    lastNode.setPosition(2750, 529)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupMedian3 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9, 0)
        del param

    del lastNode
    # End of node "Median3"

    # Start of node "Median4"
    lastNode = app.createNode("net.sf.cimg.CImgMedian", 2, group)
    lastNode.setScriptName("Median4")
    lastNode.setLabel("Median4")
    lastNode.setPosition(3085, 529)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupMedian4 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9, 0)
        del param

    del lastNode
    # End of node "Median4"

    # Start of node "Switch2"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch2")
    lastNode.setLabel("Switch2")
    lastNode.setPosition(2299, 680)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch2 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch2"

    # Start of node "Switch3"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch3")
    lastNode.setLabel("Switch3")
    lastNode.setPosition(2605, 676)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch3 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch3"

    # Start of node "Switch4"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch4")
    lastNode.setLabel("Switch4")
    lastNode.setPosition(2934, 675)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch4 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch4"

    # Start of node "YPbPrToRGB7091"
    lastNode = app.createNode("net.sf.openfx.YPbPrToRGB709", 1, group)
    lastNode.setScriptName("YPbPrToRGB7091")
    lastNode.setLabel("YPbPrToRGB7091")
    lastNode.setPosition(2311, 815)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupYPbPrToRGB7091 = lastNode

    del lastNode
    # End of node "YPbPrToRGB7091"

    # Start of node "YCbCrToRGB7091"
    lastNode = app.createNode("net.sf.openfx.YCbCrToRGB709", 1, group)
    lastNode.setScriptName("YCbCrToRGB7091")
    lastNode.setLabel("YCbCrToRGB7091")
    lastNode.setPosition(2617, 812)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupYCbCrToRGB7091 = lastNode

    del lastNode
    # End of node "YCbCrToRGB7091"

    # Start of node "RGBToHSV2"
    lastNode = app.createNode("net.sf.openfx.RGBToHSV", 1, group)
    lastNode.setScriptName("RGBToHSV2")
    lastNode.setLabel("RGBToHSV2")
    lastNode.setPosition(2934, 807)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupRGBToHSV2 = lastNode

    del lastNode
    # End of node "RGBToHSV2"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(2018, 1138)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(1896, 1164)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(1896, 317)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(3764, 1164)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Blur5"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur5")
    lastNode.setLabel("Blur5")
    lastNode.setPosition(3227, 524)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur5 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9.529999999999999, 0)
        param.setValue(9.529999999999999, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur5"

    # Start of node "Median5"
    lastNode = app.createNode("net.sf.cimg.CImgMedian", 2, group)
    lastNode.setScriptName("Median5")
    lastNode.setLabel("Median5")
    lastNode.setPosition(3396, 522)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupMedian5 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(9, 0)
        del param

    del lastNode
    # End of node "Median5"

    # Start of node "Dot8"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot8")
    lastNode.setLabel("Dot8")
    lastNode.setPosition(3272, 312)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot8 = lastNode

    del lastNode
    # End of node "Dot8"

    # Start of node "Dot9"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot9")
    lastNode.setLabel("Dot9")
    lastNode.setPosition(3272, 432)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot9 = lastNode

    del lastNode
    # End of node "Dot9"

    # Start of node "Switch5"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch5")
    lastNode.setLabel("Switch5")
    lastNode.setPosition(3227, 678)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch5 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch5"

    # Start of node "Dot10"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot10")
    lastNode.setLabel("Dot10")
    lastNode.setPosition(3272, 822)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot10 = lastNode

    del lastNode
    # End of node "Dot10"

    # Now that all nodes are created we can connect them together, restore expressions
    groupRGBToYPbPr7091.connectInput(0, groupDot2)
    groupRGBToHSV1.connectInput(0, groupDot4)
    groupRGBToYUV7091.connectInput(0, groupDot1)
    groupRGBToYCbCr7091.connectInput(0, groupDot3)
    groupBlur1.connectInput(0, groupRGBToYUV7091)
    groupDot1.connectInput(0, groupimg)
    groupDot2.connectInput(0, groupDot1)
    groupDot3.connectInput(0, groupDot2)
    groupDot4.connectInput(0, groupDot3)
    groupBlur2.connectInput(0, groupRGBToYPbPr7091)
    groupMedian1.connectInput(0, groupRGBToYUV7091)
    groupSwitch1.connectInput(0, groupBlur1)
    groupSwitch1.connectInput(1, groupMedian1)
    groupswitch_cspace.connectInput(0, groupYUVToRGB7091)
    groupswitch_cspace.connectInput(1, groupYPbPrToRGB7091)
    groupswitch_cspace.connectInput(2, groupYCbCrToRGB7091)
    groupswitch_cspace.connectInput(3, groupRGBToHSV2)
    groupswitch_cspace.connectInput(4, groupDot10)
    groupOutput1.connectInput(0, groupMerge1)
    groupYUVToRGB7091.connectInput(0, groupSwitch1)
    groupInvert1.connectInput(0, groupGrade1)
    groupGrade1.connectInput(0, groupmask)
    groupBlur3.connectInput(0, groupRGBToYCbCr7091)
    groupMedian2.connectInput(0, groupRGBToYPbPr7091)
    groupBlur4.connectInput(0, groupRGBToHSV1)
    groupMedian3.connectInput(0, groupRGBToYCbCr7091)
    groupMedian4.connectInput(0, groupRGBToHSV1)
    groupSwitch2.connectInput(0, groupBlur2)
    groupSwitch2.connectInput(1, groupMedian2)
    groupSwitch3.connectInput(0, groupBlur3)
    groupSwitch3.connectInput(1, groupMedian3)
    groupSwitch4.connectInput(0, groupBlur4)
    groupSwitch4.connectInput(1, groupMedian4)
    groupYPbPrToRGB7091.connectInput(0, groupSwitch2)
    groupYCbCrToRGB7091.connectInput(0, groupSwitch3)
    groupRGBToHSV2.connectInput(0, groupSwitch4)
    groupMerge1.connectInput(0, groupswitch_cspace)
    groupMerge1.connectInput(1, groupDot5)
    groupMerge1.connectInput(2, groupDot7)
    groupDot5.connectInput(0, groupDot6)
    groupDot6.connectInput(0, groupDot1)
    groupDot7.connectInput(0, groupInvert1)
    groupBlur5.connectInput(0, groupDot9)
    groupMedian5.connectInput(0, groupDot9)
    groupDot8.connectInput(0, groupDot4)
    groupDot9.connectInput(0, groupDot8)
    groupSwitch5.connectInput(0, groupBlur5)
    groupSwitch5.connectInput(1, groupMedian5)
    groupDot10.connectInput(0, groupSwitch5)

    param = groupBlur1.getParam("NatronOfxParamProcessR")
    group.getParam("Blur1NatronOfxParamProcessR").setAsAlias(param)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessG")
    group.getParam("Blur1NatronOfxParamProcessG").setAsAlias(param)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessB")
    group.getParam("Blur1NatronOfxParamProcessB").setAsAlias(param)
    del param
    param = groupBlur1.getParam("size")
    group.getParam("Blur1size").setAsAlias(param)
    del param
    param = groupBlur1.getParam("filter")
    group.getParam("Blur1filter").setAsAlias(param)
    del param
    param = groupBlur2.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupBlur2.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupBlur2.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupBlur2.getParam("size")
    param.slaveTo(groupBlur1.getParam("size"), 0, 0)
    param.slaveTo(groupBlur1.getParam("size"), 1, 1)
    del param
    param = groupBlur2.getParam("filter")
    param.slaveTo(groupBlur1.getParam("filter"), 0, 0)
    del param
    param = groupMedian1.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupMedian1.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupMedian1.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupMedian1.getParam("size")
    param.setExpression("thisGroup.Blur1.size.get()[dimension]", False, 0)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.c_operation.get()", False, 0)
    del param
    param = groupInvert1.getParam("disableNode")
    param.setExpression("1-thisGroup.invmask.get()", False, 0)
    del param
    param = groupBlur3.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupBlur3.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupBlur3.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupBlur3.getParam("size")
    param.slaveTo(groupBlur1.getParam("size"), 0, 0)
    param.slaveTo(groupBlur1.getParam("size"), 1, 1)
    del param
    param = groupBlur3.getParam("filter")
    param.slaveTo(groupBlur1.getParam("filter"), 0, 0)
    del param
    param = groupMedian2.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupMedian2.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupMedian2.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupMedian2.getParam("size")
    param.setExpression("thisGroup.Blur1.size.get()[dimension]", False, 0)
    del param
    param = groupBlur4.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupBlur4.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupBlur4.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupBlur4.getParam("size")
    param.slaveTo(groupBlur1.getParam("size"), 0, 0)
    param.slaveTo(groupBlur1.getParam("size"), 1, 1)
    del param
    param = groupBlur4.getParam("filter")
    param.slaveTo(groupBlur1.getParam("filter"), 0, 0)
    del param
    param = groupMedian3.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupMedian3.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupMedian3.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupMedian3.getParam("size")
    param.setExpression("thisGroup.Blur1.size.get()[dimension]", False, 0)
    del param
    param = groupMedian4.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupMedian4.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupMedian4.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupMedian4.getParam("size")
    param.setExpression("thisGroup.Blur1.size.get()[dimension]", False, 0)
    del param
    param = groupSwitch2.getParam("which")
    param.setExpression("thisGroup.c_operation.get()", False, 0)
    del param
    param = groupSwitch3.getParam("which")
    param.setExpression("thisGroup.c_operation.get()", False, 0)
    del param
    param = groupSwitch4.getParam("which")
    param.setExpression("thisGroup.c_operation.get()", False, 0)
    del param
    param = groupBlur5.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupBlur5.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupBlur5.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupBlur5.getParam("size")
    param.slaveTo(groupBlur1.getParam("size"), 0, 0)
    param.slaveTo(groupBlur1.getParam("size"), 1, 1)
    del param
    param = groupMedian5.getParam("NatronOfxParamProcessR")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessR"), 0, 0)
    del param
    param = groupMedian5.getParam("NatronOfxParamProcessG")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessG"), 0, 0)
    del param
    param = groupMedian5.getParam("NatronOfxParamProcessB")
    param.slaveTo(groupBlur1.getParam("NatronOfxParamProcessB"), 0, 0)
    del param
    param = groupMedian5.getParam("size")
    param.setExpression("thisGroup.Blur1.size.get()[dimension]", False, 0)
    del param
    param = groupSwitch5.getParam("which")
    param.setExpression("thisGroup.c_operation.get()", False, 0)
    del param

    try:
        extModule = sys.modules["lp_ColourCleanExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
