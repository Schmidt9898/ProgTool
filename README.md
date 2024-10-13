# ProgTool
Program location tool


## TODO

- find folders with .exe in them, (uninstall.exe,etc) collect folders, program name = folder name.

- 1. Windows Registry Entries

    Registry Keys for Installed Applications: Most applications create entries in the Windows Registry under specific keys. These can be checked to identify installed applications:
        32-bit applications on 64-bit systems:
            HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall
        64-bit applications:
            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
        Per-user installations:
            HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
    Inside these registry keys, you can find information such as:
        DisplayName: The name of the application.
        InstallLocation: The directory where the application is installed.
        DisplayVersion: The version of the installed application.
        Publisher: The application's publisher.

2. Installation Directory (Program Files)

    Applications are often installed in the following directories:
        C:\Program Files\ (for 64-bit applications).
        C:\Program Files (x86)\ (for 32-bit applications).
    By scanning these directories, your program can find folders related to installed applications.

3. Start Menu Entries

    Installed applications typically create shortcuts in the Start Menu:
        C:\ProgramData\Microsoft\Windows\Start Menu\Programs\
        C:\Users\<Username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\
    Scanning these locations can reveal installed applications via their shortcuts.

4. Desktop Shortcuts

    Applications might also create shortcuts on the Desktop:
        C:\Users\<Username>\Desktop\

5. AppData and Local AppData Folders

    Applications store user-specific data in the AppData folder. Common locations include:
        C:\Users\<Username>\AppData\Local\
        C:\Users\<Username>\AppData\Roaming\
    Although not directly indicating an installation, these folders often contain important configuration files for applications.

6. Services and Drivers

    Some applications (especially system tools) install Windows Services or drivers. These can be found in:
        Services: Control Panel > Administrative Tools > Services
        Drivers: C:\Windows\System32\drivers

7. System Environment Variables

    Some applications may modify system or user environment variables (e.g., adding paths to PATH).

8. Windows Installer Cache

    Windows Installer-based applications maintain a cache of .msi files in:
        C:\Windows\Installer\
    This is useful for detecting installations done via the Windows Installer.

9. Event Logs

    Some applications might log their installation in Windows Event Logs, particularly during large-scale or administrative installations.

10. Add/Remove Programs (Programs and Features)

    The Programs and Features section in the Control Panel displays a list of installed programs. This data can be programmatically accessed through the aforementioned registry keys.



