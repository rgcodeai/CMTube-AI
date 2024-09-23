@echo off
rem Crea un nuevo entorno virtual para este proyecto
echo Creando entorno virtual...
python -m venv venv
rem Comprobar si se creó correctamente el entorno virtual
if %errorlevel% neq 0 (
    echo Error al crear el entorno virtual.
    goto end
)

rem Activa el entorno virtual recién creado
echo Activando entorno virtual...
call venv/Scripts/activate.bat
rem Comprueba si las dependencias se instalaron correctamente
if %errorlevel% neq 0 (
    echo Error al activar el entorno virtual.
    goto end
)

rem Instala las dependencias necesarias para el proyecto desde requirements.txt
echo Instalando dependencias desde requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt
rem Comprueba si las dependencias se instalaron correctamente
if %errorlevel% neq 0 (
    echo Error al instalar dependencias.
    goto end
)

rem Confirma que el entorno está listo para ser usado
echo.
echo Entorno de desarrollo listo.

:end
rem Etiqueta a la que se salta si hay un error en alguna de las operaciones anteriores o al finalizar el script
echo Presione cualquier tecla para cerrar....
pause > nul