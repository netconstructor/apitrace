##########################################################################
#
# Copyright 2011 Jose Fonseca
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

from dxgiformat import *

DXGI_RGB = Struct("DXGI_RGB", [
    (Float, "Red"),
    (Float, "Green"),
    (Float, "Blue"),
])

DXGI_GAMMA_CONTROL = Struct("DXGI_GAMMA_CONTROL", [
    (DXGI_RGB, "Scale"),
    (DXGI_RGB, "Offset"),
    (Array(DXGI_RGB, 1025), "GammaCurve"),
])

DXGI_GAMMA_CONTROL_CAPABILITIES = Struct("DXGI_GAMMA_CONTROL_CAPABILITIES", [
    (BOOL, "ScaleAndOffsetSupported"),
    (Float, "MaxConvertedValue"),
    (Float, "MinConvertedValue"),
    (UINT, "NumGammaControlPoints"),
    (Array(Float, 1025), "ControlPointPositions"),
])

DXGI_RATIONAL = Struct("DXGI_RATIONAL", [
    (UINT, "Numerator"),
    (UINT, "Denominator"),
])

DXGI_MODE_SCANLINE_ORDER = Enum("DXGI_MODE_SCANLINE_ORDER", [
    "DXGI_MODE_SCANLINE_ORDER_UNSPECIFIED",
    "DXGI_MODE_SCANLINE_ORDER_PROGRESSIVE",
    "DXGI_MODE_SCANLINE_ORDER_UPPER_FIELD_FIRST",
    "DXGI_MODE_SCANLINE_ORDER_LOWER_FIELD_FIRST",
])

DXGI_MODE_SCALING = Enum("DXGI_MODE_SCALING", [
    "DXGI_MODE_SCALING_UNSPECIFIED",
    "DXGI_MODE_SCALING_CENTERED",
    "DXGI_MODE_SCALING_STRETCHED",
])

DXGI_MODE_ROTATION = Enum("DXGI_MODE_ROTATION", [
    "DXGI_MODE_ROTATION_UNSPECIFIED",
    "DXGI_MODE_ROTATION_IDENTITY",
    "DXGI_MODE_ROTATION_ROTATE90",
    "DXGI_MODE_ROTATION_ROTATE180",
    "DXGI_MODE_ROTATION_ROTATE270",
])

DXGI_MODE_DESC = Struct("DXGI_MODE_DESC", [
    (UINT, "Width"),
    (UINT, "Height"),
    (DXGI_RATIONAL, "RefreshRate"),
    (DXGI_FORMAT, "Format"),
    (DXGI_MODE_SCANLINE_ORDER, "ScanlineOrdering"),
    (DXGI_MODE_SCALING, "Scaling"),
])

DXGI_SAMPLE_DESC = Struct("DXGI_SAMPLE_DESC", [
    (UINT, "Count"),
    (UINT, "Quality"),
])

