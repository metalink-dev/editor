@echo off

SET PSCPDIR=c:\programme\PSCP
SET SFUSER=sourceforgenetuser
SET BUILDS=..\builds
SET DIST=dist
SET PYTHON=python.exe
::SET PATH=%PATH%;..\..\dependencies\Portable_Python_2.7.6.1\App;..\..\dependencies\Portable_Python_2.7.6.1\App\scripts
SET PATH=%PATH%;%SYSTEMDRIVE%\python27;%SYSTEMDRIVE%\python27\scripts
::SET PATH=%PATH%;..\..\dependencies\Portable_Python_2.7.6.1\App\Lib\site-packages\PyQt4;%SYSTEMDRIVE%\python27\Lib\site-packages\PyQt4
SET PATH=%PATH%;..\..\dependencies\upx307w;%PROGRAMFILES%\upx
SET PATH=%PATH%;..\..\dependencies\NSISPortableANSI\App\NSIS;%PROGRAMFILES(X86)%\NSIS;%PROGRAMFILES%\NSIS
SET PATH=%PATH%;..\..\dependencies\PortableApps.comInstaller
SET PORTABLE=PortableApps.comInstaller.exe

FOR /F "TOKENS=1,2 DELIMS=/ " %%A IN ('DATE /T') DO SET mm=%%B
FOR /F "TOKENS=2,3 DELIMS=/ " %%A IN ('DATE /T') DO SET dd=%%B
FOR /F "TOKENS=3,4 DELIMS=/ " %%A IN ('DATE /T') DO SET yyyy=%%B

SET MYDATE=%yyyy%-%mm%-%dd%

IF NOT EXIST setenv.bat GOTO NOSETENV
   call setenv.bat
:NOSETENV