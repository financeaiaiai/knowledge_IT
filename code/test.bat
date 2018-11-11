echo test
rem ping -n 5 127.0.0.1>nul 2>nul
for /l %%i in (1,1,10) do (
ping -n 1 127.0.0.1>nul 2>nul
echo this is %%i
)
