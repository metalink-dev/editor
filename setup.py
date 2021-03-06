# setup.py
from distutils.core import setup
import sys
import zipfile
import os
import shutil

APP_NAME = 'Metalink Editor'
VERSION = '1.3.1'
LICENSE = 'GPL'
DESC = ''
AUTHOR_NAME = 'Neil McNab'
EMAIL = ''
URL = 'https://sourceforge.net/projects/metalinks/'

scripts = ["meditor.py"]
data = ["metalink_small.png", "metalink_small.ico", "metalink.png", "license.txt", "changelog.txt", "readme.txt"]

# Needed to keep Vista's UAC from popping up and missing DLL errors from happening at runtime
manifest = """<?xml version="1.0" encoding="utf-8"?>
<asmv1:assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv1="urn:schemas-microsoft-com:asm.v1" xmlns:asmv2="urn:schemas-microsoft-com:asm.v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<assemblyIdentity version="1.0.0.0" name="Metalink Editor"/>
<trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
<security>
<requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
<requestedExecutionLevel level="asInvoker" uiAccess="false" />
</requestedPrivileges>
</security>
</trustInfo>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="X86"
            publicKeyToken="1fc8b3b9a1e18e3b"
            language="*"
        />
    </dependentAssembly>
</dependency>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</asmv1:assembly>"""

def create_zip(rootpath, zipname, mode="w"):
    print zipname
    myzip = zipfile.ZipFile(zipname, mode, zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            filepath = os.path.join(root, filename)
            filehandle = open(filepath, "rb")
            filepath = filepath[len(rootpath):]
            text = filehandle.read()
            #print filepath, len(text)
            myzip.writestr(filepath, text)
            filehandle.close()
    myzip.close()
    
def clean():  
    filelist = ["MANIFEST"]
    filelist.extend(rec_search(".exe"))
    filelist.extend(rec_search(".zip"))
    filelist.extend(rec_search(".pyc"))
    filelist.extend(rec_search(".pyo"))
    
    try:
        shutil.rmtree("build")
    except WindowsError: pass
    try:
        shutil.rmtree("dist")
    except WindowsError: pass
    try:
        shutil.rmtree("files")
    except WindowsError: pass
    
    for filename in filelist:
        #if filename not in ignore:
            try:
                os.remove(filename)
            except WindowsError: pass

def rec_search(end, abspath = True):
    start = os.path.dirname(__file__)
    mylist = []
    for root, dirs, files in os.walk(start):
        for filename in files:
            if filename.endswith(end):
                if abspath:
                    mylist.append(os.path.join(root, filename))
                else:
                    mylist.append(os.path.join(root[len(start):], filename))
                    
    return mylist

if sys.argv[1] == 'py2exe':
    import py2exe
    
    # DLL files to exclude from distribution
    dlllist = [ "mswsock.dll", "powrprof.dll", "MSVCP90.dll", "w9xpopen.exe", "API-MS-Win-Core-LocalRegistry-L1-1-0.dll", "MPR.dll"]
    
    setup(
        windows = [
            {
                "script": "metalink_editor.py",
                "icon_resources": [(1, "metalink.ico")],
                "other_resources": [(24,1,manifest)]
            },
        ],
        console = ["meditor.py"],
        data_files=[('', ["metalink_small.png", "metalink_small.ico", "metalink.png", "license.txt", "changelog.txt", "readme.txt"])],
        options={"py2exe" : {'dll_excludes': dlllist}},
        name = APP_NAME,
        version = VERSION,
        license = LICENSE,
        description = DESC,
        author = AUTHOR_NAME,
        author_email = EMAIL,
        url = URL        
    )

elif sys.argv[1] == 'clean':
    clean()

elif sys.argv[1] == 'zip':
    #print "Zipping up..."
    create_zip("dist/", APP_NAME + "-" + VERSION + "-win32.zip")

elif sys.argv[1] == 'install':
    setup(scripts = scripts,
	#packages = packages,
        data_files=[('', data)],
      name = APP_NAME,
      version = VERSION,
      license = LICENSE,
      description = DESC,
      author = AUTHOR_NAME,
      author_email = EMAIL,
      url = URL
      )

    if os.name == 'posix':
        for filename in scripts:
            mypath = "/usr/bin/"
            try:
                os.symlink(mypath + filename, mypath + filename[:-3])
                print "linking " + mypath + filename + " -> " + mypath + filename[:-3]
            except OSError: pass
            
if sys.argv[1] == 'sdist':
    setup(scripts = scripts,
	#packages = packages,
      data_files = [('', data)],
      name = APP_NAME,
      version = VERSION,
      license = LICENSE,
      description = DESC,
      author = AUTHOR_NAME,
      author_email = EMAIL,
      url = URL
      )

