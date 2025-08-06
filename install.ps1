# Se Necesitan tener los permisos de seguridad configurados con Set-ExecutionPolicy RemoteSigned
# para ello abrir la consola de PowerShell como administrador y ejecutar:
# Set-ExecutionPolicy RemoteSigned

# Activar el entorno virtual
# Cambiar la ruta del entorno virtual si es necesario
& "$env:USERPROFILE\environments\gral_env\Scripts\Activate.ps1" #variable de entorno que apunta al usuario

pip3 install -r requirements.txt