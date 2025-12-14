@echo off
echo Starting C code compilation...
echo.


gcc unitconverter.c -o converter_exe.exe


if %errorlevel% equ 0 (
    echo -------------------------------------------------------------------
    echo SUCCESS! C program compiled. Executable: converter_exe.exe is ready.
    echo -------------------------------------------------------------------
) else (
    echo -------------------------------------------------------------------
    echo ERROR: C program compilation failed.
    echo Please check 'unitconverter.c' for syntax errors.
    echo -------------------------------------------------------------------
)