import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def check_admin():
   """ checks if the script is running with administrative rights.
   It uses the ctypes library to call the Windows API function IsUserAnAdmin(). """
   try:
       isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
   except AttributeError:
       isAdmin = False
   if not isAdmin:
       ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
"""opens the specified file with the specified verb, which in this case is "runas", which means "run as administrator"""

def add_rule(rule_name, file_path):
   """ Add rule to Windows Firewall """
   """This command adds a new rule to the Windows Firewall.
    The stdout and stderr parameters are set to DEVNULL to suppress the output and errors of the command."""
   subprocess.call(
       f"netsh advfirewall firewall add rule name={rule_name} dir=out action=block enable=no program={file_path}",
       shell=True,
       stdout=DEVNULL,
       stderr=DEVNULL
   )
   print(f"Rule {rule_name} for {file_path} added")

if __name__ == '__main__':
   check_admin()
   """ ensure the script has administrative rights."""
   add_rule("RULE_NAME", "PATH_TO_FILE")
   """ add the rule to the Windows Firewall."""
