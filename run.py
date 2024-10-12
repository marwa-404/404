import os
import platform
import subprocess
import time

subprocess.call('clear', shell=True)

print('Checking for updates...')

subprocess.call('git pull', shell=True)

permission = input('Do you want to allow permissions? (y/n): ')
if permission.lower() == 'y':
    subprocess.call('termux-setup-storage', shell=True)

try:
    import requests
except ImportError:
    subprocess.call('pip install requests', shell=True)

subprocess.call('git pull', shell=True)

bit = platform.architecture()[0]
print(f'Detected architecture: {bit}')  # Added print statement
if bit == '64bit':
    print("\n64 bit Congratulations! Your device supports this tool.")
    try:
        from DARK import menu___
        menu___()
    except Exception as e:
        print(f"Error occurred while importing menu___: {e}")  # Error handling
elif bit == '32bit':
    print("\n32 bit Congratulations! Your device supports this tool.")
    try:
        from DARK32 import menu___
        menu___()
    except Exception as e:
        print(f"Error occurred while importing menu___: {e}")  # Error handling
else:
    print("Just Leave:", bit)
