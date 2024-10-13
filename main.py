


import os, sys

# Get the current user's username
username = os.getlogin()


print(username)

if sys.stdout.isatty():
    # You're running in a real terminal
	print(os.get_terminal_size())
else:
    # You're being piped or redirected
	pass
print(os.getcwdb())## good
print(os.getlogin())
print(os.getpid())
print(os.getppid())
print(os.getcwd())

from pathlib import Path

# Get the home directory
home_folder = str(Path.home())
print(home_folder)

# TODO add externile input
folders_to_search = ["C:\Program Files",
					 "C:\Program Files (x86)"]
for p in folders_to_search:
	assert os.path.exists(p)


import ctypes, sys
import subprocess

_is_admin = None
def is_admin():
	global _is_admin
	if _is_admin is None:
		try:
			_is_admin = ctypes.windll.shell32.IsUserAnAdmin()
		except:
			_is_admin = False
	return _is_admin

if is_admin():
	print("You have admin privileges!")
	# Your admin-level code here
else:
	print("You don't have admin privileges!")
	# Re-run the script with admin privileges
	#print("Requesting admin privileges...")
	# TODO make this optional
	#ctypes.windll.shell32.ShellExecuteW(
	#	None, "runas", sys.executable, " ".join(sys.argv), None, 1) # returns the exit code of 42 or 5
	#exit()

	# Does not work
	#params = " ".join([sys.executable] + sys.argv)
	#proc = subprocess.run(
	#	['runas', '/user:Administrator', f'{params}'], shell=True)
	#proc.check_returncode()  # Will raise an error if the process fails


import winreg

#winreg

#\HKEY_LOCAL_MACHINE


def reqursive_registry_list(key,dept = 0):
	programs = []
	#if dept > 2:
	#	return
	num_subkeys,_num_values,_last_mod_time = winreg.QueryInfoKey(key)
	try:
		#print(num_subkeys,_num_values)
		app_name = winreg.QueryValueEx(key, "DisplayName")[0]
		app_location = winreg.QueryValueEx(key, "InstallLocation")[0]
		if app_location == '':
			return programs
		entry = (app_name,app_location)
		programs.append(entry)
		return programs
	except Exception as e:
		#print(e)
		pass 

	for i in range(num_subkeys):
		# Get the name of the subkey (application key)
		subkey_name = winreg.EnumKey(key, i)
		#print(subkey_name)
		# Open the subkey
		try:
			app_key = winreg.OpenKey(key, subkey_name)
			programs.extend(reqursive_registry_list(app_key,dept+1))
		except:
			pass
	return programs	



#registry_paths = [
#	r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",  # 64-bit system-wide apps
#	r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",  # 32-bit apps on 64-bit OS
#]

#for path in registry_paths:
#	registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
#	reqursive_registry_list(registry_key)


registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE")
l = reqursive_registry_list(registry_key)

print(len(l))
l = set(l)
print(len(l))

for name,path in l:
	#path = path.decode("utf-8") if type(path) != str else path
	if "D:" in str(path):
		print(f"{name}: {path}")

if is_admin():
	input("press eny key")

exit()


