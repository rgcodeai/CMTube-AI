@echo off
rem Activa el entorno virtual existente
echo Activando entorno virtual...
call venv\Scripts\activate.bat
rem Comprueba si se ha activado correctamente el entorno virtual
if %errorlevel% neq 0 (
    echo Error al activar el entorno virtual.
    goto end
)

rem Actualiza pip a la última versión
echo Actualizando pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Error al actualizar pip.
    goto end
)

rem Actualiza todas las dependencias listadas en requirements.txt
echo Actualizando dependencias desde requirements.txt...
pip install --upgrade -r requirements.txt
if %errorlevel% neq 0 (
    echo Error al actualizar dependencias.
    goto end
)

rem Confirma que las dependencias se han actualizado correctamente
echo.
echo Dependencias actualizadas exitosamente.

:end
rem Etiqueta a la que se salta si hay un error en alguna de las operaciones anteriores o al finalizar el script
echo Presione cualquier tecla para cerrar...
pause > nul
