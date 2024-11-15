setlocal
REM
REM usage e.g.     make_mib.bat IF-MIB       will generate IF-MIB.py     
REM
REM Any specific vendor mibs can first be added to the src directory
REM

set "MIBS_TO_BUILD=IF-MIB DISMAN-EXPRESSION-MIB  IANAifType-MIB SNMPv2-MIB"

@echo Will check web and %~dp0src for MIB source
@echo Building mibs %MIBS_TO_BUILD%

set "MYDIR=%~dp0"

set "EPICS_MIBDIR=C:\Instrument\Apps\EPICS\support\NET-SNMP\master\vendor\mibs"
REM to also look at epics NETSNMP mibs uncomment this
REM set "EXTRA_ARGS=--mib-source file:///%EPICS_MIBDIR:\=/%"

REM having trouble with pysnmp site 
REM set "MIBS_WEB=https://mibs.pysnmp.com/asn1/@mib@"
set "MIBS_WEB=https://raw.githubusercontent.com/net-snmp/net-snmp/master/mibs/@mib@"

del %MYDIR%*.py
%~dp0..\..\scripts\mibdump.exe --mib-source file:///%MYDIR:\=/%src ^
                               --mib-source %MIBS_WEB% ^
                               --generate-mib-texts --keep-texts-layout --rebuild ^
                               %EXTRA_ARGS% ^
                               --destination-format pysnmp --no-python-compile --destination-directory . ^
                               %MIBS_TO_BUILD%
