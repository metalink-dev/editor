rem *** Used to create a Python exe 

call sample_setenv.bat

%PYTHON% setup.py clean

rem ***** create the exe
%PYTHON% -OO setup.py py2exe 

%PYTHON% setup.py zip

echo "done..."