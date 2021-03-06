# - try to find DirectX include dirs and libraries

if (${CMAKE_SYSTEM_NAME} STREQUAL "Windows")
	find_path (DirectX_ROOT_DIR
		Include/d3d9.h
		PATHS
			"$ENV{DXSDK_DIR}"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (June 2010)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (February 2010)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (March 2009)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (August 2008)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (June 2008)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (March 2008)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (November 2007)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK (August 2007)"
			"$ENV{ProgramFiles}/Microsoft DirectX SDK"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (June 2010)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (February 2010)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (March 2009)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (August 2008)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (June 2008)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (March 2008)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (November 2007)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK (August 2007)"
			"$ENV{ProgramFiles(x86)}/Microsoft DirectX SDK"
		DOC "DirectX SDK root directory")


	if (CMAKE_CL_64)
		set (DirectX_ARCHITECTURE x64)
	else ()
		set (DirectX_ARCHITECTURE x86)
	endif ()


	find_path (DirectX_D3D_INCLUDE_DIR d3d.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d.h resides")

	find_path (DirectX_D3DX_INCLUDE_DIR d3dx.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3dx.h resides")

	find_library (DirectX_DDRAW_LIBRARY ddraw
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where ddraw resides")

	find_library (DirectX_D3DX_LIBRARY d3dx
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3dx resides")

	if (DirectX_D3D_INCLUDE_DIR AND DirectX_DDRAW_LIBRARY)
		set (DirectX_D3D_FOUND 1)
		if (DirectX_D3DX_INCLUDE_DIR AND DirectX_D3DX_LIBRARY)
			set (DirectX_D3DX_FOUND 1)
		endif ()
	endif ()


	find_path (DirectX_D3D8_INCLUDE_DIR d3d8.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d8.h resides")

	find_path (DirectX_D3DX8_INCLUDE_DIR d3dx8.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3dx8.h resides")

	find_library (DirectX_D3D8_LIBRARY d3d8
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3d8 resides")

	find_library (DirectX_D3DX8_LIBRARY d3dx8
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3dx8 resides")

	if (DirectX_D3D8_INCLUDE_DIR AND DirectX_D3D8_LIBRARY)
		set (DirectX_D3D8_FOUND 1)
		if (DirectX_D3DX8_INCLUDE_DIR AND DirectX_D3DX8_LIBRARY)
			set (DirectX_D3DX8_FOUND 1)
		endif ()
	endif ()


	find_path (DirectX_D3D9_INCLUDE_DIR d3d9.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d9.h resides")

	find_path (DirectX_D3DX9_INCLUDE_DIR d3dx9.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3dx9.h resides")

	find_library (DirectX_D3D9_LIBRARY d3d9
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3d9 resides")

	find_library (DirectX_D3DX9_LIBRARY d3dx9
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3dx9 resides")

	if (DirectX_D3D9_INCLUDE_DIR AND DirectX_D3D9_LIBRARY)
		set (DirectX_D3D9_FOUND 1)
		if (DirectX_D3DX9_INCLUDE_DIR AND DirectX_D3DX9_LIBRARY)
			set (DirectX_D3DX9_FOUND 1)
		endif ()
	endif ()


	find_path (DirectX_D3D10_INCLUDE_DIR d3d10.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d10.h resides")

	find_path (DirectX_D3DX10_INCLUDE_DIR d3dx10.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3dx10.h resides")

	find_library (DirectX_D3D10_LIBRARY d3d10
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3d10 resides")

	find_library (DirectX_D3DX10_LIBRARY d3dx10
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3dx10 resides")

	if (DirectX_D3D10_INCLUDE_DIR AND DirectX_D3D10_LIBRARY)
		set (DirectX_D3D10_FOUND 1)
		if (DirectX_D3DX10_INCLUDE_DIR AND DirectX_D3DX10_LIBRARY)
			set (DirectX_D3DX10_FOUND 1)
		endif ()
	endif ()


	find_path (DirectX_D3D10_1_INCLUDE_DIR d3d10_1.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d10_1.h resides")

	find_library (DirectX_D3D10_1_LIBRARY d3d10_1
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3d10_1 resides")

	if (DirectX_D3D10_1_INCLUDE_DIR AND DirectX_D3D10_1_LIBRARY)
		set (DirectX_D3D10_1_FOUND 1)
	endif ()


	find_path (DirectX_D3D11_INCLUDE_DIR d3d11.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3d11.h resides")

	find_path (DirectX_D3DX11_INCLUDE_DIR d3dx11.h
		PATHS
			"${DirectX_ROOT_DIR}/Include"
		DOC "The directory where d3dx11.h resides")

	find_library (DirectX_D3D11_LIBRARY d3d11
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3d11 resides")

	find_library (DirectX_D3DX11_LIBRARY d3dx11
		PATHS
			"${DirectX_ROOT_DIR}/Lib/${DirectX_ARCHITECTURE}"
		DOC "The directory where d3dx11 resides")

	if (DirectX_D3D11_INCLUDE_DIR AND DirectX_D3D11_LIBRARY)
		set (DirectX_D3D11_FOUND 1)
		if (DirectX_D3DX11_INCLUDE_DIR AND DirectX_D3DX11_LIBRARY)
			set (DirectX_D3DX11_FOUND 1)
		endif ()
	endif ()


	mark_as_advanced(
		DirectX_D3D_INCLUDE_DIR
		DirectX_D3D_INCLUDE_DIR
		DirectX_DDRAW_LIBRARY
		DirectX_DDRAW_LIBRARY
		DirectX_D3DX_INCLUDE_DIR
		DirectX_D3DX_INCLUDE_DIR
		DirectX_D3DX_LIBRARY
		DirectX_D3DX_LIBRARY
		DirectX_D3D8_INCLUDE_DIR
		DirectX_D3D8_INCLUDE_DIR
		DirectX_D3D8_LIBRARY
		DirectX_D3D8_LIBRARY
		DirectX_D3DX8_INCLUDE_DIR
		DirectX_D3DX8_INCLUDE_DIR
		DirectX_D3DX8_LIBRARY
		DirectX_D3DX8_LIBRARY
		DirectX_D3D9_INCLUDE_DIR
		DirectX_D3D9_LIBRARY
		DirectX_D3DX9_INCLUDE_DIR
		DirectX_D3DX9_LIBRARY
		DirectX_D3D10_INCLUDE_DIR
		DirectX_D3D10_LIBRARY
		DirectX_D3DX10_INCLUDE_DIR
		DirectX_D3DX10_LIBRARY
		DirectX_D3D10_1_INCLUDE_DIR
		DirectX_D3D10_1_LIBRARY
		DirectX_D3D11_INCLUDE_DIR
		DirectX_D3D11_LIBRARY
		DirectX_D3DX11_INCLUDE_DIR
		DirectX_D3DX11_LIBRARY
	)

endif ()

mark_as_advanced (
	DirectX_D3D_FOUND
	DirectX_D3DX_FOUND
	DirectX_D3D8_FOUND
	DirectX_D3DX8_FOUND
	DirectX_D3D9_FOUND
	DirectX_D3DX9_FOUND
	DirectX_D3D10_FOUND
	DirectX_D3DX10_FOUND
	DirectX_D3D10_1_FOUND
	DirectX_D3D11_FOUND
	DirectX_D3DX11_FOUND
)
