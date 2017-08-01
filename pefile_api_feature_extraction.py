#coding:UTF-8
#pefileで.exe fileのAPIを抽出する


import pefile
pe = pefile.PE('path/to/your/file')

pe.parse_data_directories()
 
for entry in pe.DIRECTORY_ENTRY_IMPORT:
     print entry.dll
     for imp in entry.imports:
             print '\t', hex(imp.address), imp.name
             
             
             
#出力例
'''
DINPUT8.dll
	0x510494 DirectInput8Create
d3d8.dll
	0x5107a0 Direct3DCreate8
WINMM.dll
	0x510770 timeGetTime
KERNEL32.dll
	0x510524 MapViewOfFile
	0x510528 CreateFileMappingA
	0x51052c CreateFileA
	0x510530 CreateFileW
	0x510534 UnmapViewOfFile
	0x510538 HeapFree
	0x51053c GetProcessHeap
	0x510540 GetProcAddress
	0x510544 LoadLibraryA
	0x510548 GetModuleHandleA
	0x51054c LockResource
	0x510550 LoadResource
	0x510554 SizeofResource
	0x510558 FindResourceA
	0x51055c FindResourceW
	0x510560 WriteFile
	0x510564 CompareStringW
	0x510568 CompareStringA
	0x51056c GetLocaleInfoW
	0x510570 GetTimeZoneInformation
	0x510574 SetEndOfFile
	0x510578 ReadFile
	0x51057c LCMapStringW
	0x510580 LCMapStringA
	0x510584 GetStringTypeW
	0x510588 GetStringTypeA
	0x51058c IsBadCodePtr
	0x510590 SetUnhandledExceptionFilter
	0x510594 GetOEMCP
	0x510598 GetACP
	0x51059c FlushFileBuffers
	0x5105a0 SetStdHandle
	0x5105a4 SetFilePointer
	0x5105a8 SetConsoleCtrlHandler
	0x5105ac GetUserDefaultLCID
	0x5105b0 EnumSystemLocalesA
	0x5105b4 GetLocaleInfoA
	0x5105b8 IsValidCodePage
	0x5105bc IsValidLocale
	0x5105c0 GetFileSize
	0x5105c4 GetLastError
	0x5105c8 GetVersionExA
	0x5105cc IsProcessorFeaturePresent
	0x5105d0 WideCharToMultiByte
	0x5105d4 GetTempPathA
	0x5105d8 lstrcpyA
	0x5105dc CloseHandle
	0x5105e0 GetCurrentDirectoryA
	0x5105e4 MultiByteToWideChar
	0x5105e8 OutputDebugStringA
	0x5105ec Sleep
	0x5105f0 GetCPInfo
	0x5105f4 VirtualAlloc
	0x5105f8 HeapReAlloc
	0x5105fc HeapAlloc
	0x510600 RaiseException
	0x510604 SetEnvironmentVariableA
	0x510608 VirtualFree
	0x51060c GetStartupInfoA
	0x510610 GetCommandLineA
	0x510614 GetVersion
	0x510618 ExitProcess
	0x51061c RtlUnwind
	0x510620 IsBadWritePtr
	0x510624 IsBadReadPtr
	0x510628 HeapValidate
	0x51062c TerminateProcess
	0x510630 GetCurrentProcess
	0x510634 DebugBreak
	0x510638 GetStdHandle
	0x51063c InterlockedDecrement
	0x510640 InterlockedIncrement
	0x510644 GetModuleFileNameA
	0x510648 UnhandledExceptionFilter
	0x51064c FreeEnvironmentStringsA
	0x510650 FreeEnvironmentStringsW
	0x510654 GetEnvironmentStrings
	0x510658 GetEnvironmentStringsW
	0x51065c SetHandleCount
	0x510660 GetFileType
	0x510664 GetEnvironmentVariableA
	0x510668 HeapDestroy
	0x51066c HeapCreate
USER32.dll
	0x5106dc LoadIconA
	0x5106e0 TranslateMessage
	0x5106e4 GetMessageA
	0x5106e8 PeekMessageA
	0x5106ec DefWindowProcA
	0x5106f0 SetCursor
	0x5106f4 DrawTextW
	0x5106f8 DrawTextA
	0x5106fc SetRect
	0x510700 GetKeyboardState
	0x510704 MessageBoxA
	0x510708 DestroyWindow
	0x51070c GetDesktopWindow
	0x510710 GetWindowRect
	0x510714 PostQuitMessage
	0x510718 LoadCursorA
	0x51071c RegisterClassExA
	0x510720 CreateWindowExA
	0x510724 ShowWindow
	0x510728 UpdateWindow
	0x51072c PostMessageA
	0x510730 DispatchMessageA
GDI32.dll
	0x5104c4 CreateCompatibleDC
	0x5104c8 CreateDIBSection
	0x5104cc SetBkMode
	0x5104d0 SetBkColor
	0x5104d4 SetTextColor
	0x5104d8 SelectObject
	0x5104dc DeleteDC
	0x5104e0 CreateFontIndirectA
	0x5104e4 DeleteObject
	0x5104e8 GetObjectA
	0x5104ec GetStockObject
ADVAPI32.dll
	0x51045c RegQueryValueExA
	0x510460 RegOpenKeyA
	0x510464 RegCloseKey
ole32.dll
	0x5107d0 CoInitialize
	0x5107d4 CoCreateInstance
'''
