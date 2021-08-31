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
print("4. Enemies.bin")
print("5. Augments.bin (WIP, Works partially)")
print('')
print('0. Exit the app')
print('')
SelectedBIN = int(input('Select the .bin you want to decode: '))

if SelectedBIN == 0:
    exit()
elif SelectedBIN > 5 or SelectedBIN < 0:
    raise ValueError('The selected number is invalid. Try again.')

# Reads HEX from file

if SelectedBIN == 1:
    BinaryFile = 'weapons.bin'
elif SelectedBIN == 2:
    BinaryFile = 'ammo.bin'
elif SelectedBIN == 3:
    BinaryFile = 'equipment.bin'
elif SelectedBIN == 4:
    BinaryFile = 'enemies.bin'
elif SelectedBIN == 5:
    print('WARNING: This feature is still WIP')
    BinaryFile = 'augments.bin'
with open(BinaryFile, 'rb') as f:
    Numbers = f.read()
BinaryRaw = str(binascii.hexlify(Numbers))
# print(BinaryRaw) - Debug

# -------------------

# Main code

if SelectedBIN == 1:
    BinaryDecoded = open("weapons.csv", "w", newline="")
elif SelectedBIN == 2:
    BinaryDecoded = open("ammo.csv", "w", newline="")
elif SelectedBIN == 3:
    BinaryDecoded = open("equipment.csv", "w", newline="")
elif SelectedBIN == 4:
    BinaryDecoded = open("enemies.csv", "w", newline="")
elif SelectedBIN == 5:
    BinaryDecoded = open("augments.csv", "w", newline="")

## DO NOT CHANGE
## -------------

## ES - Enemy stats
if SelectedBIN == 4:
    t1 = 4
    t2 = 12
else:
    t1 = 2
    t2 = 6
ByteOrder1 = [4, 4, 4, 2, 2, 4, 4, 4, 8, 8, 8, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 4, 2, 4, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 8, 8, 4, 4, 4, 8, 4, 4, 4, 2, 4, 'null']
ByteOrder2 = [4, 2, 8, 2, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 2]
ByteOrder3 = [4, 4, 4, 2, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 4, 4]
ByteOrder4 = [8, 'text', 4, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 8, 1]
ByteOrder4ES = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
ByteOrder5 = [4, 2, 2, 2, 8, 4, 8, 4, 2]
TextOrder1 = ['ID', 'Name', 'Description', 'Manufacturer', 'Category', 'Rating', 'Max Grade', 'Rarity', 'Cost', 'Range', 'Accuracy', 'Cone', 'unknown', 'Rate of fire', 'Clip size', 'Reload time', 'Movement speed', 'Projectile speed', 'Trigger type', 'Ammo ID', 'Display', 'Profile', 'Eject', 'ContiniousEjectC', 'ReloadC', 'PoseC', 'EjectXOffsetC', 'EjectYOffsetC', 'PremiumEjectC', 'PremiumEjectXOffsetC', 'PremiiumEjectYOffsetC', 'GibAmountC', 'AppearsInStoreC', 'WeaponSoundC', 'DestroyedTurretC', 'WeaponVersionC', 'IsEnemyWeaponC', 'IsSeekingC', 'ExplosionC', 'AppearsInStoreAtPlayerLevelC', 'TurretBaseC', 'TurretTopC', 'DeployTurretBaseC', 'DeployTurretTopC', 'IsTurretC', 'TurretTargetAngleC', 'BurstSpeed', 'BurstCount', 'ChildrenTurretC', 'ChildTurrtIndexC', 'ReloadSoundGroupID', 'ConsumableType', 'ConsumableOrderC', 'MinGradeDropC', 'unknown']
TextOrder2 = ['ID', 'Projectile count', 'Damage', 'Damage type', 'Radius', 'Pierce', 'DoT', 'DoT length', 'Arc range', 'Seeking angle', 'Stun length', 'Speed scale', 'Speed scale duration', 'Ammo display', 'Trail', 'Trail eject instance', 'Wall hit', 'Enemy hit', 'AmmoDisplay2C', 'AmooDisplay3C', 'AmmoDisplay1MinLength', 'AmmoDisplay1MaxLength', 'AmmoDisplay1MinSpacing', 'AmmoDisplay1MaxSpacing', 'AmmoDisplay2MinLength', 'AmmoDisplay2MaxLength', 'AmmoDisplay2MinSpacing', 'AmmoDisplay2MaxSpacing', 'AmmoDisplay3MinLength', 'AmmoDisplay3MaxLength', 'AmmoDisplay3MinSpacing', 'AmmoDisplay3MaxSpacing', 'Impact Type']
TextOrder3 = ['ID', 'Manufacturer', 'Name', 'Slot ID', 'Description', 'Rating', 'Rarity', 'Cost', 'Physical Resist', 'Thermal Resist', 'Chemical Resist', 'Movement speed', 'Spread', 'Damage', 'Energy boost', 'Health boost', 'Health regen', 'Energy regen', 'Recovery speed', 'Reload speed', 'Contact damage', 'Contact damage type', 'Display1', 'Display2', 'Display3', 'Display4', 'Profile1', 'Profile2', 'Profile3', 'Profile4', 'Equipped profile1', 'Equipped profile2', 'Equipped profile3', 'Equipped profile4', 'Max Grade', 'Appears in store', 'Equipment version', 'Appears in store at player level', 'Minimum grade drop', 'unknown']
TextOrder4 = ['ID', 'Enemy name', 'Grade count', 'Body diameter', 'Stun threshold', 'Can gib?', 'Gib amount', 'Mass', 'Melee range', 'Turn speed', 'Blood on floor asset', 'Blood on death asset', 'Blood on hit asset', 'Drop class', 'Melee damage type', 'Ranged damage type']
TextOrder4ES = ['Version', 'Drop chance', 'Health', 'Melee attack cooldown', 'Melee damage', 'Move speed', 'Ranged attack cooldown', 'Ranged damage', 'Ranged projectile speed', 'Ranged range', 'Chemical resistance', 'Energy resistance', 'Physical resistance', 'Thermal resistance', 'XP per kill', 'Death asset', 'Ranged asset', 'Walking asset', 'Hit animation 0 asset', 'Hit animation 1 asset', 'Hit animation 2 asset', 'Melee animation 0 asset', 'Melee animation 1 asset', 'Flame death asset']
TextOrder5 = ['ID', 'Slot', 'Type', 'Grade', 'Cost', 'Message', 'Effect']
IntOrFloat1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
IntOrFloat2 = [1]
IntOrFloat3 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
IntOrFloat4 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
IntOrFloat4ES = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
IntOrFloat5 = [0, 1]
Row1 = []
Row2 = []
EnemyName = ["Shambler", "Stalker", "Spitter", "Runner", "Bloater", "Shielder", "Zombdroid Servant", "Zombdroid Soldier", "Worm", "Puke Worm", "Regurgitator", "Necrosis", "Necrosis Spawn", "Zombie Mech", "Wicker", "Devastator", "Loaderbot"]
# for i in range(len(EnemyName)):
#    print(len(EnemyName[i]))
EnemyNameSize = [18, 18, 18, 16, 18, 20, 38, 38, 12, 22, 28, 20, 32, 26, 16, 24, 22]
EnemyNameOrder = 0
EnemyGrades = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 2, 2, 6, 2, 2, 2, 2]
EnemyGradeOrder = 0
EnemyGradeOrder1 = 0
EnemyGradeOrderES = 0
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
elif SelectedBIN == 4:
    ByteOrder = ByteOrder4
    ByteOrderES = ByteOrder4ES
    IntOrFloat = IntOrFloat4
    IntOrFloatES = IntOrFloat4ES
    TextOrder = TextOrder4
    TextOrderES = TextOrder4ES
elif SelectedBIN == 5:
    ByteOrder = ByteOrder5
    IntOrFloat = IntOrFloat5
    TextOrder = TextOrder5
Order = 0
IOFOrder = 0
DecryptMode = 0
HEXString = 0
## -------------
while t2 <= len(BinaryRaw):
    if EnemyGradeOrderES == EnemyGrades[EnemyGradeOrder1]:
        EnemyGradeOrderES=0
        EnemyGradeOrder1=EnemyGradeOrder1+1
        DecryptMode=0
    if IOFOrder >= len(IntOrFloat) and DecryptMode == 0:
        IOFOrder = 0
    if Order<len(ByteOrder)-3 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        HEXString = BinaryRaw[t1:t2]
        NormalString = str(int("0x" + HEXString, 0))
        Row1.append(TextOrder[Order])
        Row2.append(NormalString)
        if ByteOrder[Order+1] == 'text':
            t1=t2
            t2=t2+EnemyNameSize[EnemyNameOrder]
        else:
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
    elif Order<len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        if IntOrFloat[IOFOrder] == 0:
            HEXString = BinaryRaw[t1:t2]
            NormalString = str(int("0x" + HEXString, 0))
            Row1.append(TextOrder[Order])
            Row2.append(NormalString)
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1:
            HEXString = BinaryRaw[t1:t2]
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            Row1.append(TextOrder[Order])
            Row2.append(NormalString)
            IOFOrder = IOFOrder + 1
        if ByteOrder[Order+1] == 'text':
            t1=t2
            t2=t2+EnemyNameSize[EnemyNameOrder]
        else:
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
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        if IntOrFloat[IOFOrder] == 0:
            HEXString = BinaryRaw[t1:t2]
            NormalString = str(int("0x" + HEXString, 0))
            Row1.append(TextOrder[Order])
            Row1.append('')
            Row2.append(NormalString)
        elif IntOrFloat[IOFOrder] == 1:
            HEXString = BinaryRaw[t1:t2]
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            Row1.append(TextOrder[Order])
            Row1.append('')
            Row2.append(NormalString)
            Row2.append('')
            IOFOrder = 0
        if ByteOrder[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrder[Order+1] == 2:
            t1=t2
            t2=t2+2
        if SelectedBIN == 4:
            DecryptMode=1
        Order=0
        IOFOrder = 0
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
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
        if SelectedBIN == 4:
            DecryptMode=1
        Order=0
        IOFOrder = 0
    elif Order<len(ByteOrder)-3 and str(ByteOrder[Order])=='text' and DecryptMode == 0:
        NormalString = EnemyName[EnemyNameOrder]
        Row1.append(TextOrder[Order])
        Row2.append(NormalString)
        if ByteOrder[Order+1] == 4:
            t1=t2
            t2=t2+4
        Order=Order+1
        EnemyNameOrder = EnemyNameOrder+1
    elif Order<len(ByteOrderES)-3 and ByteOrderES[Order]!=8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        HEXString = BinaryRaw[t1:t2]
        NormalString = str(int("0x" + HEXString, 0))
        Row1.append(TextOrderES[Order])
        Row2.append(NormalString)
        if ByteOrderES[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrderES[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrderES[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=Order+1
    elif Order<len(ByteOrderES)-3 and ByteOrderES[Order]==8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        if IntOrFloatES[IOFOrder] == 0:
            HEXString = BinaryRaw[t1:t2]
            NormalString = str(int("0x" + HEXString, 0))
            Row1.append(TextOrderES[Order])
            Row2.append(NormalString)
            IOFOrder = IOFOrder + 1
        elif IntOrFloatES[IOFOrder] == 1:
            HEXString = BinaryRaw[t1:t2]
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            Row1.append(TextOrderES[Order])
            Row2.append(NormalString)
            IOFOrder = IOFOrder + 1
        t1=t2
        t2=t2+8
        Order=Order+1
    elif Order==len(ByteOrderES)-3 and ByteOrderES[Order]==8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        if IntOrFloatES[IOFOrder] == 0:
            HEXString = BinaryRaw[t1:t2]
            NormalString = str(int("0x" + HEXString, 0))
            Row1.append(TextOrderES[Order])
            Row1.append('')
            Row2.append(NormalString)
            Row2.append('')
            IOFOrder = 0
        elif IntOrFloatES[IOFOrder] == 1:
            HEXString = BinaryRaw[t1:t2]
            NormalString = struct.unpack('>f', bytes.fromhex(HEXString))[0]
            NormalString = format(NormalString, '.3f')
            Row1.append(TextOrderES[Order])
            Row1.append('')
            Row2.append(NormalString)
            Row2.append('')
            IOFOrder = 0
        if ByteOrderES[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrderES[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrderES[Order+1] == 2:
            t1=t2
            t2=t2+2
        Order=0
        if DecryptMode == 1:
            if EnemyGradeOrderES < EnemyGrades[EnemyGradeOrder1]:
                EnemyGradeOrderES=EnemyGradeOrderES+1
        IOFOrder = 0
    elif Order==len(ByteOrderES)-3 and ByteOrderES[Order]!=8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        HEXString = BinaryRaw[t1:t2]
        NormalString = str(int("0x" + HEXString, 0))
        Row1.append(TextOrderES[Order])
        Row1.append('')
        Row2.append(NormalString)
        Row2.append('')
        if ByteOrderES[Order+1] == 8:
            t1=t2
            t2=t2+8
        elif ByteOrderES[Order+1] == 4:
            t1=t2
            t2=t2+4
        elif ByteOrderES[Order+1] == 2:
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
