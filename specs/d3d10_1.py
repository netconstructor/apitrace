##########################################################################
#
# Copyright 2008-2012 VMware, Inc.
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

"""d3d10_1.h"""

from winapi import *
from d3d10sdklayers import *
from d3d10 import *

ID3D10Blob = Interface("ID3D10Blob", IUnknown)
LPD3D10BLOB = ObjPointer(ID3D10Blob)

ID3D10Blob.methods += [
    Method(LPVOID, "GetBufferPointer", []),
    Method(SIZE_T, "GetBufferSize", []),
]

D3D10_DRIVER_TYPE = Enum("D3D10_DRIVER_TYPE", [
    "D3D10_DRIVER_TYPE_HARDWARE",
    "D3D10_DRIVER_TYPE_REFERENCE",
    "D3D10_DRIVER_TYPE_NULL",
    "D3D10_DRIVER_TYPE_SOFTWARE",
    "D3D10_DRIVER_TYPE_WARP",
])

D3D10_FEATURE_LEVEL1 = Enum("D3D10_FEATURE_LEVEL1", [
    "D3D10_FEATURE_LEVEL_10_0",
    "D3D10_FEATURE_LEVEL_10_1",
	"D3D10_FEATURE_LEVEL_9_1",
	"D3D10_FEATURE_LEVEL_9_2",
	"D3D10_FEATURE_LEVEL_9_3",
])

D3D10_RENDER_TARGET_BLEND_DESC1 = Struct("D3D10_RENDER_TARGET_BLEND_DESC1", [
    (BOOL, "BlendEnable"),
    (D3D10_BLEND, "SrcBlend"),
    (D3D10_BLEND, "DestBlend"),
    (D3D10_BLEND_OP, "BlendOp"),
    (D3D10_BLEND, "SrcBlendAlpha"),
    (D3D10_BLEND, "DestBlendAlpha"),
    (D3D10_BLEND_OP, "BlendOpAlpha"),
    (UINT8, "RenderTargetWriteMask"),
])

D3D10_BLEND_DESC1 = Struct("D3D10_BLEND_DESC1", [
    (BOOL, "AlphaToCoverageEnable"),
    (BOOL, "IndependentBlendEnable"),
    (Array(D3D10_RENDER_TARGET_BLEND_DESC1, "D3D10_SIMULTANEOUS_RENDER_TARGET_COUNT"), "RenderTarget"),
])

ID3D10BlendState1 = Interface("ID3D10BlendState1", ID3D10BlendState)
ID3D10BlendState1.methods += [
    Method(Void, "GetDesc1", [Out(Pointer(D3D10_BLEND_DESC1), "pDesc")]),
]

D3D10_TEXCUBE_ARRAY_SRV1 = Struct("D3D10_TEXCUBE_ARRAY_SRV1", [
    (UINT, "MostDetailedMip"),
    (UINT, "MipLevels"),
    (UINT, "First2DArrayFace"),
    (UINT, "NumCubes"),
])

D3D10_SHADER_RESOURCE_VIEW_DESC1 = Struct("D3D10_SHADER_RESOURCE_VIEW_DESC1", [
    (DXGI_FORMAT, "Format"),
    (D3D10_SRV_DIMENSION1, "ViewDimension"),
    (D3D10_BUFFER_SRV, "Buffer"),
    (D3D10_TEX1D_SRV, "Texture1D"),
    (D3D10_TEX1D_ARRAY_SRV, "Texture1DArray"),
    (D3D10_TEX2D_SRV, "Texture2D"),
    (D3D10_TEX2D_ARRAY_SRV, "Texture2DArray"),
    (D3D10_TEX2DMS_SRV, "Texture2DMS"),
    (D3D10_TEX2DMS_ARRAY_SRV, "Texture2DMSArray"),
    (D3D10_TEX3D_SRV, "Texture3D"),
    (D3D10_TEXCUBE_SRV, "TextureCube"),
    (D3D10_TEXCUBE_ARRAY_SRV1, "TextureCubeArray"),
])

ID3D10ShaderResourceView1 = Interface("ID3D10ShaderResourceView1", ID3D10ShaderResourceView)
ID3D10ShaderResourceView1.methods += [
    Method(Void, "GetDesc1", [Out(Pointer(D3D10_SHADER_RESOURCE_VIEW_DESC1), "pDesc")]),
]

ID3D10Device1 = Interface("ID3D10Device1", ID3D10Device)
ID3D10Device1.methods += [
    Method(HRESULT, "CreateShaderResourceView1", [(ObjPointer(ID3D10Resource), "pResource"), Out(Pointer(Const(D3D10_SHADER_RESOURCE_VIEW_DESC1)), "pDesc"), Out(Pointer(ObjPointer(ID3D10ShaderResourceView1)), "ppSRView")]),
    Method(HRESULT, "CreateBlendState1", [(Pointer(Const(D3D10_BLEND_DESC1)), "pBlendStateDesc"), Out(Pointer(ObjPointer(ID3D10BlendState1)), "ppBlendState")]),
    Method(D3D10_FEATURE_LEVEL1, "GetFeatureLevel", []),
]

d3d10_1 = API("d3d10_1")
d3d10_1.addFunctions([
    StdFunction(HRESULT, "D3D10CreateDevice1", [(ObjPointer(IDXGIAdapter), "pAdapter"), (D3D10_DRIVER_TYPE, "DriverType"), (HMODULE, "Software"), (D3D10_CREATE_DEVICE_FLAG, "Flags"), (D3D10_FEATURE_LEVEL1, "HardwareLevel"), (UINT, "SDKVersion"), Out(Pointer(ObjPointer(ID3D10Device1)), "ppDevice")]),
    StdFunction(HRESULT, "D3D10CreateDeviceAndSwapChain1", [(ObjPointer(IDXGIAdapter), "pAdapter"), (D3D10_DRIVER_TYPE, "DriverType"), (HMODULE, "Software"), (D3D10_CREATE_DEVICE_FLAG, "Flags"), (D3D10_FEATURE_LEVEL1, "HardwareLevel"), (UINT, "SDKVersion"), (Pointer(DXGI_SWAP_CHAIN_DESC), "pSwapChainDesc"), Out(Pointer(ObjPointer(IDXGISwapChain)), "ppSwapChain"), Out(Pointer(ObjPointer(ID3D10Device1)), "ppDevice")]),
    StdFunction(HRESULT, "D3D10CreateBlob", [(SIZE_T, "NumBytes"), Out(Pointer(LPD3D10BLOB), "ppBuffer")]),
])

d3d10_1.addInterfaces([
    IDXGIDevice,
    ID3D10Debug,
    ID3D10SwitchToRef,
    ID3D10InfoQueue,
    ID3D10DeviceChild,
    ID3D10Resource,
    ID3D10Buffer,
    ID3D10Texture1D,
    ID3D10Texture2D,
    ID3D10Texture3D,
    ID3D10View,
    ID3D10DepthStencilView,
    ID3D10RenderTargetView,
    ID3D10ShaderResourceView1,
    ID3D10BlendState1,
    ID3D10DepthStencilState,
    ID3D10GeometryShader,
    ID3D10InputLayout,
    ID3D10PixelShader,
    ID3D10RasterizerState,
    ID3D10SamplerState,
    ID3D10VertexShader,
    ID3D10Asynchronous,
    ID3D10Counter,
    ID3D10Query,
    ID3D10Predicate,
    ID3D10Device,
    ID3D10Multithread,
])
