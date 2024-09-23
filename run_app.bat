@echo off
rem Activa el entorno virtual necesario para el proyecto
echo Activando entorno virtual...
call venv\Scripts\activate.bat
rem Comprueba si se ha activado correctamente el entorno virtual
if %errorlevel% neq 0 (
    echo Error al activar el entorno virtual.
    goto end
    rem Si hay un error, muestra un mensaje y salta a la etiqueta :end
)

rem Ejecuta la aplicación de Streamlit
echo Ejecutando aplicación de Streamlit...
streamlit run app.py
rem Comprobar si la aplicación de Streamlit se ha ejecutado correctamente
if %errorlevel% neq 0 (
    echo Error al ejecutar la aplicación de Streamlit.
    goto end
    rem Si hay un error, muestra un mensaje y salta a la etiqueta :end
)

rem Muestra un mensaje de éxito si la aplicación de Streamlit se ejecutó sin errores
echo.
echo Aplicación de Streamlit ejecutada exitosamente.

:end
rem Etiqueta a la que se salta si hay un error en alguna de las operaciones anteriores o al finalizar el script
echo Presione cualquier tecla para cerrar....
pause > nul