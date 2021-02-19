@echo off
@echo Starting Script at %date% %time% >> %logfile%
"C:\Users\felix\AppData\Local\Microsoft\WindowsApps\python.exe" "C:\Users\Desktop\entregable\ExtraerDatos.py"
@echo finished at %date% %time% >> %logfile%