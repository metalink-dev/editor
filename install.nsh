Function GetAfterChar
  Exch $0 ; chop char
  Exch
  Exch $1 ; input string
  Push $2
  Push $3
  StrCpy $2 0
  loop:
    IntOp $2 $2 - 1
    StrCpy $3 $1 1 $2
    StrCmp $3 "" 0 +3
      StrCpy $0 ""
      Goto exit2
    StrCmp $3 $0 exit1
    Goto loop
  exit1:
    IntOp $2 $2 + 1
    StrCpy $0 $1 "" $2
  exit2:
    Pop $3
    Pop $2
    Pop $1
    Exch $0 ; output
FunctionEnd

!macro install Name UUID URL Silent
    ; http://nsis.sourceforge.net/Tutorial:_Using_labels_in_macro%27s
    !define UniqueID ${__LINE__}
    ; check install of MS Redistributable
    ; HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{FF66E9F6-83E7-3A3E-AF14-8DE9A809A6A4}
    ; HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{FF66E9F6-83E7-3A3E-AF14-8DE9A809A6A4}
	
	Push ${URL}
    Push "/"
    Call GetAfterChar
	Pop $R1
    
    ReadRegStr $R0 HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${UUID}" "DisplayName"
  
    ${If} $R0 == ""
        DetailPrint "${Name} not detected."    
        MessageBox MB_YESNO|MB_ICONQUESTION "${Name} is required but not installed, would you like to download and install it?" /SD IDNO IDNO installend_${UniqueID} 

        DetailPrint "Attempting to download and install ${Name} from ${URL}..."
        NSISdl::download /TIMEOUT=30000 ${URL} $PLUGINSDIR\$R1

        IfSilent installsilent_${UniqueID}
        
        ExecWait "$PLUGINSDIR\$R1"
        Goto installend_${UniqueID}
        
        installsilent_${UniqueID}:
        ExecWait "$PLUGINSDIR\$R1 ${Silent}"
        Goto installend_${UniqueID}
    ${Else}
        DetailPrint "${Name} detected."
    ${EndIf}
    
    installend_${UniqueID}:
    !undef UniqueID
    
!macroend