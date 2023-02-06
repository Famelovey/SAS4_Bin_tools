# Important stuff

import os     #
import shutil # For file operations

# ---------------

# Prompt

if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\') == 0:
    os.makedirs(os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\')

print('Availble commands:')
print('')
print('1. Backup .bin files')
print('2. Restore .bin files')
print('')
print('0. Exit the app')
print('')
SelectedOption = int(input('Select the option: '))

if SelectedOption == 0:
    exit()

print('Availble commands:')
print('')
print('1. Weapons.bin')
print('2. Ammo.bin')
print('3. Equipment.bin')
print("4. Enemies.bin")
print("5. Augments.bin")
print('')
print("6. All .bin files")
print('')
print('0. Exit the app')
print('')
SelectedBIN = int(input('Select the .bin file: '))

if SelectedBIN == 0:
    exit()
elif SelectedBIN > 6 or SelectedBIN < 0:
    raise ValueError('The selected number is invalid. Try again.')
    
BinaryFile = ['\\weapons.bin', '\\ammo.bin', '\\equipment.bin', '\\enemies.bin', '\\augments.bin']
counter = 0

if SelectedOption == 1:
    if SelectedBIN < 6:
        shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + BinaryFile[SelectedBIN - 1], os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\')
    else:
        while counter < 5:
            shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + BinaryFile[counter], os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\')
            counter = counter + 1
if SelectedOption == 2:
    if SelectedBIN < 6:
        shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\' + BinaryFile[SelectedBIN - 1], os.path.dirname(os.path.abspath(__file__)))
    else:
        while counter < 5:
            shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + '\\Backup\\' + BinaryFile[counter], os.path.dirname(os.path.abspath(__file__)))
            counter = counter + 1