"""
this script is modifying the contents of the PATH environment variable by adding a directory to it.
We then call the myapp command with that modified variable.
Doing it this way, the command will run in the modified environment with the updated value of path.
DETAILED:
we start by calling the copy method of the OS environ dictionary that contains the current environment variables.
This creates a new dictionary that we can change as needed without modifying the original environment.

The change that we're doing in this script is adding one extra directory to the path variable.
(Remember, the path variable indicates where the operating system will look for the executable programs.)
By adding one entry to the path, we're telling the OS to look for programs in an additional location.

To create the new value, we're calling the 'join' method on the OS path substring.
This joins elements of the list that we're passing with a path separator corresponding to the current operating system.
So here, we're joining /opt/myapp and the old value of the path variable to the path separator.

Finally, we call the myapp command, setting the end parameter to the new environment that we've just prepared.
"""

import os
import subprocess


my_env = os.environ.copy()
# print(my_env)
my_env['PATH'] = os.pathsep.join(['/opt/myapp', my_env['PATH']])  # * read below

result = subprocess.run(['myapp'], env=my_env)  # ** read below

# * This line modifies the PATH environment variable in the my_env dictionary.
# The PATH variable specifies a list of directories where the operating system looks for executable files.
# Here, the code adds the directory /opt/myapp to the beginning of the PATH variable, separating it with
# the appropriate separator (os.pathsep). This ensures that when a command is executed, the operating system will
# search for it in /opt/myapp before checking other directories in the PATH.
# The os.pathsep.join() function concatenates the directories using the path separator appropriate for the current OS.

# ** This line executes the command myapp as a subprocess using the modified environment my_env.
# The subprocess.run() function runs the specified command and waits for it to complete. The env parameter is used
# to specify the environment variables to be used by the subprocess.

# In this case, the modified my_env dictionary is passed to the env parameter, so the subprocess will use the updated PATH environment variable with /opt/myapp added at the beginning.

# Content of my_env variable:
# {
#   'ALLUSERSPROFILE': 'C:\\ProgramData',
#   'APPDATA': 'C:\\Users\\i_yaroshenko\\AppData\\Roaming',
#   'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
#   'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#   'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
#   'COMPUTERNAME': 'DM-NB-108',
#   'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
#   'DB_PASS': 'magnum4opus',
#   'DB_USER': 'postgres',
#   'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
#   'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
#   'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
#   'GDAL_DATA': 'C:\\Program Files\\PostgreSQL\\15\\gdal-data',
#   'HOMEDRIVE': 'C:',
#   'HOMEPATH': '\\Users\\i_yaroshenko',
#   'IDEA_INITIAL_DIRECTORY': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin',
#   'JETBRAINS RIDER': 'C:\\Program Files\\JetBrains\\JetBrains Rider 2022.2\\bin;',
#   'LOCALAPPDATA': 'C:\\Users\\i_yaroshenko\\AppData\\Local',
#   'LOGONSERVER': '\\\\AD1',
#   'NUMBER_OF_PROCESSORS': '16',
#   'ONEDRIVE': 'C:\\Users\\i_yaroshenko\\OneDrive',
#   'OPENSSL_CONF': 'C:\\Program Files\\PostgreSQL\\psqlODBC\\etc\\openssl.cnf',
#   'OS': 'Windows_NT',
#   'PATH': 'C:\\pythonProject\\venv\\Scripts;C:\\Program Files\\Python311\\Scripts\\;C:\\Program Files\\Python311\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\TortoiseSVN\\bin;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files\\dotnet\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\TortoiseSVN\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\i_yaroshenko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\JetBrains Rider 2022.2\\bin;;C:\\Users\\i_yaroshenko\\.dotnet\\tools;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin;;C:\\Users\\i_yaroshenko\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe;C:\\Program Files\\Python311;C:\\Program Files\\Python311\\Scripts;',
#   'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
#   'POSTGIS_ENABLE_OUTDB_RASTERS': '1',
#   'POSTGIS_GDAL_ENABLED_DRIVERS': 'GTiff PNG JPEG GIF XYZ DTED USGSDEM AAIGrid',
#   'PROCESSOR_ARCHITECTURE': 'AMD64',
#   'PROCESSOR_IDENTIFIER': 'AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD',
#   'PROCESSOR_LEVEL': '25',
#   'PROCESSOR_REVISION': '5000',
#   'PROGRAMDATA': 'C:\\ProgramData',
#   'PROGRAMFILES': 'C:\\Program Files',
#   'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
#   'PROGRAMW6432': 'C:\\Program Files',
#   'PROJ_LIB': 'C:\\Program Files\\PostgreSQL\\15\\share\\contrib\\postgis-3.3\\proj',
#   'PROMPT': '(venv) $P$G',
#   'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
#   'PUBLIC': 'C:\\Users\\Public',
#   'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin;',
#   'PYCHARM_HOSTED': '1',
#   'PYTHONIOENCODING': 'UTF-8',
#   'PYTHONPATH': 'C:\\pythonProject',
#   'PYTHONUNBUFFERED': '1',
#   'SESSIONNAME': 'Console',
#   'SYSTEMDRIVE': 'C:',
#   'SYSTEMROOT': 'C:\\Windows',
#   'TEMP': 'C:\\Users\\I_YARO~1\\AppData\\Local\\Temp',
#   'TMP': 'C:\\Users\\I_YARO~1\\AppData\\Local\\Temp',
#   'USERDNSDOMAIN': 'DREAMATE.LOCAL',
#   'USERDOMAIN': 'DREAMATE',
#   'USERDOMAIN_ROAMINGPROFILE': 'DREAMATE',
#   'USERNAME': 'i_yaroshenko',
#   'USERPROFILE': 'C:\\Users\\i_yaroshenko',
#   'VIRTUAL_ENV': 'C:\\pythonProject\\venv',
#   'WINDIR': 'C:\\Windows',
#   '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Python311\\Scripts\\;C:\\Program Files\\Python311\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\TortoiseSVN\\bin;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files\\dotnet\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\TortoiseSVN\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\i_yaroshenko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\JetBrains Rider 2022.2\\bin;;C:\\Users\\i_yaroshenko\\.dotnet\\tools;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin;;C:\\Users\\i_yaroshenko\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe;C:\\Program Files\\Python311;C:\\Program Files\\Python311\\Scripts;',
#   '_OLD_VIRTUAL_PROMPT': '$P$G'
# }