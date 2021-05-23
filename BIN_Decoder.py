# Important stuff

import binascii # Used for HEX reading
import csv      # Used for writing down numbers in .csv file
import struct   # Used for HEX float processing
from itertools import zip_longest # Used for writing down numbers in .csv file

# ---------------

# Prompt

print('Availble commands:')
print('')
print('1. Weapons.bin')
print('2. Ammo.bin')
print('3. Equipment.bin')
print('')
print('0. Exit the app')
print('')
SelectedBIN = int(input('Select the .bin you want to decode: '))

if SelectedBIN == 0:
    exit()
elif SelectedBIN > 3 or SelectedBIN < 0:
    raise ValueError('The selected number is invalid. Try again.')

# Reads HEX from file

if SelectedBIN == 1:
    BinaryFile = 'weapons.bin'
elif SelectedBIN == 2:
    BinaryFile = 'ammo.bin'
elif SelectedBIN == 3:
    BinaryFile = 'equipment.bin'
with open(BinaryFile, 'rb') as f:
    Numbers = f.read()
BinaryRaw = str(binascii.hexlify(Numbers))
# print(BinaryRaw) - Debug

# -------------------

# Main code

if SelectedBIN == 1:
    BinaryDecoded = open("weapons.csv", "w")
elif SelectedBIN == 2:
    BinaryDecoded = open("ammo.csv", "w")
elif SelectedBIN == 3:
    BinaryDecoded = open("equipment.csv", "w")

## DO NOT CHANGE
## -------------
t1 = 2
t2 = 6
ByteOrder1 = [4, 4, 4, 2, 2, 4, 4, 4, 8, 8, 8, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 4, 2, 4, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 8, 8, 4, 4, 4, 8, 4, 4, 4, 2, 4, 'null']
ByteOrder2 = [4, 2, 8, 2, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 2]
ByteOrder3 = [4, 4, 4, 2, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 4, 4]
TextOrder1 = ['ID', 'Name', 'Description', 'Manufacturer', 'Category', 'Rating', 'Max Grade', 'Rarity', 'Cost', 'Range', 'Accuracy', 'Cone', 'Rate of fire', 'unknown', 'Clip size', 'Reload time', 'Movement speed', 'Projectile speed', 'Trigger type', 'Ammo ID', 'Display', 'Profile', 'Eject', 'ContiniousEjectC', 'ReloadC', 'PoseC', 'EjectXOffsetC', 'EjectYOffsetC', 'PremiumEjectC', 'PremiumEjectXOffsetC', 'PremiiumEjectYOffsetC', 'GibAmountC', 'AppearsInStoreC', 'WeaponSoundC', 'DestroyedTurretC', 'WeaponVersionC', 'IsEnemyWeaponC', 'IsSeekingC', 'ExplosionC', 'AppearsInStoreAtPlayerLevelC', 'TurretBaseC', 'TurretTopC', 'DeployTurretBaseC', 'DeployTurretTopC', 'IsTurretC', 'TurretTargetAngleC', 'BurstSpeed', 'BurstCount', 'ChildrenTurretC', 'ChildTurrtIndexC', 'ReloadSoundGroupID', 'ConsumableType', 'ConsumableOrderC', 'MinGradeDropC', 'unknown']
TextOrder2 = ['ID', 'Projectile count', 'Damage', 'Damage type', 'Radius', 'Pierce', 'DoT', 'DoT length', 'Arc range', 'Seeking angle', 'Stun length', 'Speed scale', 'Speed scale duration', 'Ammo display', 'Trail', 'Trail eject instance', 'Wall hit', 'Enemy hit', 'AmmoDisplay2C', 'AmooDisplay3C', 'AmmoDisplay1MinLength', 'AmmoDisplay1MaxLength', 'AmmoDisplay1MinSpacing', 'AmmoDisplay1MaxSpacing', 'AmmoDisplay2MinLength', 'AmmoDisplay2MaxLength', 'AmmoDisplay2MinSpacing', 'AmmoDisplay2MaxSpacing', 'AmmoDisplay3MinLength', 'AmmoDisplay3MaxLength', 'AmmoDisplay3MinSpacing', 'AmmoDisplay3MaxSpacing', 'Impact Type']
TextOrder3 = ['ID', 'Manufacturer', 'Name', 'Slot ID', 'Description', 'Rating', 'Rarity', 'Cost', 'Physical Resist', 'Thermal Resist', 'Chemical Resist', 'Movement speed', 'Spread', 'Damage', 'Energy boost', 'Health boost', 'Health regen', 'Energy regen', 'Recovery speed', 'Reload speed', 'Contact damage', 'Contact damage type', 'Display1', 'Display2', 'Display3', 'Display4', 'Profile1', 'Profile2', 'Profile3', 'Profile4', 'Equipped profile1', 'Equipped profile2', 'Equipped profile3', 'Equipped profile4', 'Max Grade', 'Appears in store', 'Equipment version', 'Appears in store at player level', 'Minimum grade drop', 'unknown']
IntOrFloat1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
IntOrFloat2 = [1]
IntOrFloat3 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Row1 = []
Row2 = []
# 0 - int;
# 1 - float
if SelectedBIN == 1:
    ByteOrder = ByteOrder1
    IntOrFloat = IntOrFloat1
    TextOrder = TextOrder1
elif SelectedBIN == 2:
    ByteOrder = ByteOrder2
    IntOrFloat = IntOrFloat2
    TextOrder = TextOrder2
elif SelectedBIN == 3:
    ByteOrder = ByteOrder3
    IntOrFloat = IntOrFloat3
    TextOrder = TextOrder3
Order = 0
IOFOrder = 0
## -------------

while t2 <= len(BinaryRaw):
    if IOFOrder >= len(IntOrFloat):
        IOFOrder = 0
    if Order<len(ByteOrder)-3 and ByteOrder[Order]!=8:
        HEXString = BinaryRaw[t1:t2]
        NormalString = str(int("0x" + HEXString, 0))
        Row1.append(TextOrder[Order])
        Row2.append(NormalString)
        if ByteOrder[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrder[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=Order+1
    elif Order<len(ByteOrder)-3 and ByteOrder[Order]==8:
        HEXString = BinaryRaw[t1:t2]
        if IntOrFloat[IOFOrder] == 0:
            NormalString = str(int("0x" + HEXString, 0))
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1:
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            IOFOrder = IOFOrder + 1
        Row1.append(TextOrder[Order])
        Row2.append(NormalString)
        if ByteOrder[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrder[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=Order+1
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]==8:
        HEXString = BinaryRaw[t1:t2]
        if IntOrFloat[IOFOrder] == 0:
            NormalString = str(int("0x" + HEXString, 0))
            IOFOrder = 0
        elif IntOrFloat[IOFOrder] == 1:
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            IOFOrder = 0
            print(t1, t2)
        Row1.append(TextOrder[Order])
        Row1.append('')
        Row2.append(NormalString)
        Row2.append('')
        if ByteOrder[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrder[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=0
        IOFOrder = 0
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]!=8:
        HEXString = BinaryRaw[t1:t2]
        NormalString = str(int("0x" + HEXString, 0))
        Row1.append(TextOrder[Order])
        Row1.append('')
        Row2.append(NormalString)
        Row2.append('')
        if ByteOrder[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrder[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=0
        IOFOrder = 0
Rows = zip(Row1, Row2)
Writer = csv.writer(BinaryDecoded)
for row in Rows:
    Writer.writerow(row)
BinaryDecoded.close()
# End
