call sample_setenv.bat

call py2exe.bat %1

makensis.exe setup.nsi

echo "done..."