; AutoHotKey script to map "ctrl + \" to run current line in VS Code
; Goes in windows startup folder (Win + R -> shell:startup)
#Hotif WinActive("ahk_exe Code.exe")
^\::
{
  Send("{Home}")
  Send("+{End}")}
  Sleep 20
  Send("+{Enter}")}
  Send("{Home}")
  Send("{Down}")
}
#HotIf
