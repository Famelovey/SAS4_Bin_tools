# Important stuff

import os       # Used for folder
import binascii # Used for HEX reading
import csv      # Used for writing down numbers in .csv file
import struct   # Used for HEX float processing
from itertools import zip_longest # Used for writing down numbers in .csv file

# ---------------

# Prompt

if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\') == 0:
    os.makedirs(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\')

print('Availble commands:')
print('')
print('1. Weapons.bin')
print('2. Ammo.bin')
print('3. Equipment.bin')
print("4. Enemies.bin")
print("5. Augments.bin")
print('')
print("6. [WIP, doesn't work] All .bin files")
print('')
print('0. Exit the app')
print('')
SelectedBIN = int(input('Select the .bin you want to decode: '))

if SelectedBIN == 0:
    exit()
elif SelectedBIN > 6 or SelectedBIN < 0:
    raise ValueError('The selected number is invalid. Try again.')

# Reads HEX from file

if SelectedBIN == 1 or SelectedBIN == 6:
    BinaryFile = 'weapons.bin'
elif SelectedBIN == 2:
    BinaryFile = 'ammo.bin'
elif SelectedBIN == 3:
    BinaryFile = 'equipment.bin'
elif SelectedBIN == 4:
    BinaryFile = 'enemies.bin'
elif SelectedBIN == 5:
    BinaryFile = 'augments.bin'
with open(BinaryFile, 'rb') as f:
    Numbers = f.read()
BinaryRaw = str(binascii.hexlify(Numbers))
# print(BinaryRaw) - Debug

# -------------------

# Main code

if SelectedBIN == 1 or SelectedBIN == 6:
    BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'weapons.csv', "w", newline="")
elif SelectedBIN == 2:
    BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'ammo.csv', "w", newline="")
elif SelectedBIN == 3:
    BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'equipment.csv', "w", newline="")
elif SelectedBIN == 4:
    BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'enemies.csv', "w", newline="")
elif SelectedBIN == 5:
    BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'augments.csv', "w", newline="")

## DO NOT CHANGE
## -------------

## ES - Enemy stats
if SelectedBIN == 4:
    t1 = 4
    t2 = 12
else:
    t1 = 2
    t2 = 6
# Order of bytes (in what order they should be decoded)
ByteOrder1 = [4, 4, 4, 2, 2, 4, 4, 4, 8, 8, 8, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 4, 2, 4, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 8, 8, 4, 4, 4, 8, 4, 4, 4, 2, 4, 'null']
ByteOrder2 = [4, 2, 8, 2, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 2]
ByteOrder3 = [4, 4, 4, 2, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 4, 4]
ByteOrder4 = [8, 'text', 4, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 8, 1]
ByteOrder4ES = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
ByteOrder5 = [4, 2, 2, 2, 8, 4, 8, 4, 2]
ByteOrder5A = [4, 2, 2, 2, 2, 2, 2, 2, 2, 8, 4, 8, 4, 2]
# Text order (for better understandment of decoded values)
TextOrder1 = ['ID', 'Name', 'Description', 'Manufacturer', 'Category', 'Rating', 'Max Grade', 'Rarity', 'Cost', 'Range', 'Accuracy', 'Cone', 'unknown', 'Rate of fire', 'Clip size', 'Reload time', 'Movement speed', 'Projectile speed', 'Trigger type', 'Ammo ID', 'Display', 'Profile', 'Eject', 'ContiniousEjectC', 'ReloadC', 'PoseC', 'EjectXOffsetC', 'EjectYOffsetC', 'PremiumEjectC', 'PremiumEjectXOffsetC', 'PremiiumEjectYOffsetC', 'GibAmountC', 'AppearsInStoreC', 'WeaponSoundC', 'DestroyedTurretC', 'WeaponVersionC', 'IsEnemyWeaponC', 'IsSeekingC', 'ExplosionC', 'AppearsInStoreAtPlayerLevelC', 'TurretBaseC', 'TurretTopC', 'DeployTurretBaseC', 'DeployTurretTopC', 'IsTurretC', 'TurretTargetAngleC', 'BurstSpeed', 'BurstCount', 'ChildrenTurretC', 'ChildTurrtIndexC', 'ReloadSoundGroupID', 'ConsumableType', 'ConsumableOrderC', 'MinGradeDropC', 'IsObtainable']
TextOrder2 = ['ID', 'Projectile count', 'Damage', 'Damage type', 'Radius', 'Pierce', 'DoT', 'DoT length', 'Arc range', 'Seeking angle', 'Stun length', 'Speed scale', 'Speed scale duration', 'Ammo display', 'Trail', 'Trail eject instance', 'Wall hit', 'Enemy hit', 'AmmoDisplay2C', 'AmooDisplay3C', 'AmmoDisplay1MinLength', 'AmmoDisplay1MaxLength', 'AmmoDisplay1MinSpacing', 'AmmoDisplay1MaxSpacing', 'AmmoDisplay2MinLength', 'AmmoDisplay2MaxLength', 'AmmoDisplay2MinSpacing', 'AmmoDisplay2MaxSpacing', 'AmmoDisplay3MinLength', 'AmmoDisplay3MaxLength', 'AmmoDisplay3MinSpacing', 'AmmoDisplay3MaxSpacing', 'Impact Type']
TextOrder3 = ['ID', 'Manufacturer', 'Name', 'Slot ID', 'Description', 'Rating', 'Rarity', 'Cost', 'Physical Resist', 'Thermal Resist', 'Chemical Resist', 'Movement speed', 'Spread', 'Damage', 'Energy boost', 'Health boost', 'Health regen', 'Energy regen', 'Recovery speed', 'Reload speed', 'Contact damage', 'Contact damage type', 'Display1', 'Display2', 'Display3', 'Display4', 'Profile1', 'Profile2', 'Profile3', 'Profile4', 'Equipped profile1', 'Equipped profile2', 'Equipped profile3', 'Equipped profile4', 'Max Grade', 'Appears in store', 'Equipment version', 'Appears in store at player level', 'Minimum grade drop', 'IsObtainable']
TextOrder4 = ['ID', 'Enemy name', 'Grade count', 'Body diameter', 'Stun threshold', 'Can gib?', 'Gib amount', 'Mass', 'Melee range', 'Turn speed', 'Blood on floor asset', 'Blood on death asset', 'Blood on hit asset', 'Drop class', 'Melee damage type', 'Ranged damage type']
TextOrder4ES = ['Version', 'Drop chance', 'Health', 'Melee attack cooldown', 'Melee damage', 'Move speed', 'Ranged attack cooldown', 'Ranged damage', 'Ranged projectile speed', 'Ranged range', 'Chemical resistance', 'Energy resistance', 'Physical resistance', 'Thermal resistance', 'XP per kill', 'Death asset', 'Ranged asset', 'Walking asset', 'Hit animation 0 asset', 'Hit animation 1 asset', 'Hit animation 2 asset', 'Melee animation 0 asset', 'Melee animation 1 asset', 'Flame death asset']
TextOrder5 = ['ID', 'Slot', 'Type', 'Grade', 'Cost', 'Message', 'Effect']
TextOrder5A = ['ID', 'Armor Pieces', 'Armor slot ID 1', 'Armor slot ID 2', 'Armor slot ID 3', 'Armor slot ID 4', 'Armor slot ID 5', 'Type', 'Grade', 'Cost', 'Message', 'Effect']
# Order for decoding values with size of 8:
# 0 - int;
# 1 - float
IntOrFloat1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
IntOrFloat2 = [1]
IntOrFloat3 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
IntOrFloat4 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
IntOrFloat4ES = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
IntOrFloat5 = [0, 1]
IntOrFloat5A = [0, 1]
# Rows where values and text is stored
Row1 = []
Row2 = []
# Enemy related stuff
EnemyName = ["Shambler", "Stalker", "Spitter", "Runner", "Bloater", "Shielder", "Zombdroid Servant", "Zombdroid Soldier", "Worm", "Puke Worm", "Regurgitator", "Necrosis", "Necrosis Spawn", "Zombie Mech", "Wicker", "Devastator", "Loaderbot", "Mercenary", "aaa"]
EnemyNameSize = [18, 18, 18, 16, 18, 20, 38, 38, 12, 22, 28, 20, 32, 26, 16, 24, 22, 22, 18]
EnemyNameOrder = 0
EnemyGrades = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 2, 2, 6, 2, 2, 2, 2, 4, 4, 4]
EnemyGradeOrder = 0
EnemyGradeOrder1 = 0
EnemyGradeOrderES = 0
ByteOrderES = ByteOrder4ES
IntOrFloatES = IntOrFloat4ES
TextOrderES = TextOrder4ES
ByteOrderA = ByteOrder5A
IntOrFloatA = IntOrFloat5A
TextOrderA = TextOrder5A
if SelectedBIN == 1 or SelectedBIN == 6:
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
    IntOrFloat = IntOrFloat4
    TextOrder = TextOrder4
elif SelectedBIN == 5:
    ByteOrder = ByteOrder5
    IntOrFloat = IntOrFloat5
    TextOrder = TextOrder5
Order = 0
IOFOrder = 0
DecryptMode = 0
if SelectedBIN == 5:
    DecryptMode = 2
AugmentCounter = 0
HEXString = 0
ArmorSlotCount = 5;
ArmorCurrent = 0;
ArmorBIN = 0;
DecodedBINFiles = 0;

def writeNonFloat(BinRaw, TxtOrder, Odr, b1, b2):
    HEXStr = BinRaw[b1:b2]
    NrmStr = str(int("0x" + HEXStr, 0))
    Row1.append(TxtOrder[Odr])
    Row2.append(NrmStr)
    return 0;

def writeFloat(BinRaw, TxtOrder, Odr, b1, b2, IOF, IOFOdr):
    if IOF[IOFOdr] == 0:
        HEXStr = BinRaw[b1:b2]
        NrmStr = str(int("0x" + HEXStr, 0))
        Row1.append(TxtOrder[Odr])
        Row2.append(NrmStr)
    else:
        HEXStr = BinRaw[b1:b2]
        NrmStr = struct.unpack('>f', bytes.fromhex(HEXStr))[0]
        NrmStr = format(NrmStr, '.3f')
        Row1.append(TxtOrder[Odr])
        Row2.append(NrmStr)
    return 0;
    
def writeEmptyArmorSlot(TxtOrder, Odr):
    Row1.append(TxtOrder[Odr])
    Row2.append(0)
    return 0;
    
def calcNonFloat(BinRaw, TxtOrder, Odr, b1, b2):
    HEXStr = BinRaw[b1:b2]
    calc123 = int("0x" + HEXStr, 0)
    return calc123;
    
def writeNonFloatEnd(BinRaw, TxtOrder, Odr, b1, b2):
    HEXStr = BinRaw[b1:b2]
    NrmStr = str(int("0x" + HEXStr, 0))
    Row1.append(TxtOrder[Odr])
    Row1.append('')
    Row2.append(NrmStr)
    Row2.append('')
    return 0;

def writeFloatEnd(BinRaw, TxtOrder, Odr, b1, b2, IOF, IOFOdr):
    if IOF[IOFOdr] == 0:
        HEXStr = BinRaw[b1:b2]
        NrmStr = str(int("0x" + HEXStr, 0))
        Row1.append(TxtOrder[Odr])
        Row1.append('')
        Row2.append(NrmStr)
        Row2.append('')
    else:
        HEXStr = BinRaw[b1:b2]
        NrmStr = struct.unpack('>f', bytes.fromhex(HEXStr))[0]
        NrmStr = format(NrmStr, '.3f')
        Row1.append(TxtOrder[Odr])
        Row1.append('')
        Row2.append(NrmStr)
        Row2.append('')
    return 0;
    
def writeZombieText(EN, ENO, TxtOrder, Odr):
    NrmStr = EN[ENO]
    Row1.append(TxtOrder[Odr])
    Row2.append(NrmStr)
    return 0;

def OrderOfBytes(b1, b2, Odr, ByteOdr):
    b1 = b2
    b2 = b2 + ByteOdr[Odr + 1]
    Odr = Odr + 1
    return b1, b2, Odr;
    
def OrderOfBytesENS(b1, b2, Odr, ByteOdr, ENS, ENO):
    b1 = b2
    b2 = b2 + ENS[ENO]
    Odr = Odr + 1
    return b1, b2, Odr;
    
def OrderOfBytesENO(b1, b2, Odr, ENO):
    b1 = b2
    b2 = b2 + 4
    Odr = Odr + 1
    ENO = ENO + 1
    return b1, b2, Odr, ENO;

## -------------
## Decryption modes:
## 0 - normal
## 1 - zombie grades
## 2 - weapon augments
while t2 <= len(BinaryRaw) or DecodedBINFiles < 5:
    if t2 >= len(BinaryRaw) and SelectedBIN == 6:
        DecodedBINFiles = DecodedBINFiles + 1
        if DecodedBINFiles == 3:
            t1 = 4
            t2 = 12
        else:
            t1 = 2
            t2 = 6
        Rows = zip(Row1, Row2)
        Writer = csv.writer(BinaryDecoded)
        for row in Rows:
            Writer.writerow(row)
        BinaryDecoded.close()
        Row1 = []
        Row2 = []
        Order = 0
        IOFOrder = 0
        HEXString = 0
        EnemyGradeOrder1 = 0
        if DecodedBINFiles == 1:
            BinaryFile = 'ammo.bin'
        elif DecodedBINFiles == 2:
            BinaryFile = 'equipment.bin'
        elif DecodedBINFiles == 3:
            BinaryFile = 'enemies.bin'
        elif DecodedBINFiles == 4:
            BinaryFile = 'augments.bin'
        with open(BinaryFile, 'rb') as f:
            Numbers = f.read()
        BinaryRaw = str(binascii.hexlify(Numbers))
        if DecodedBINFiles == 1:
            BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'ammo.csv', "w", newline="")
        elif DecodedBINFiles == 2:
            BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'equipment.csv', "w", newline="")
        elif DecodedBINFiles == 3:
            BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'enemies.csv', "w", newline="")
        elif DecodedBINFiles == 4:
            BinaryDecoded = open(os.path.dirname(os.path.abspath(__file__)) + '\\Decoded .bin files\\' + 'augments.csv', "w", newline="")
    if DecodedBINFiles == 1:
        ByteOrder = ByteOrder2
        IntOrFloat = IntOrFloat2
        TextOrder = TextOrder2
    elif DecodedBINFiles == 2:
        ByteOrder = ByteOrder3
        IntOrFloat = IntOrFloat3
        TextOrder = TextOrder3
    elif DecodedBINFiles == 3:
        ByteOrder = ByteOrder4
        IntOrFloat = IntOrFloat4
        TextOrder = TextOrder4
    elif DecodedBINFiles == 4:
        ByteOrder = ByteOrder5
        IntOrFloat = IntOrFloat5
        TextOrder = TextOrder5
        DecryptMode = 2
    if t2 >= len(BinaryRaw) and SelectedBIN != 6:
        break;
    if EnemyGradeOrderES == EnemyGrades[EnemyGradeOrder1]:
        EnemyGradeOrderES=0
        EnemyGradeOrder1=EnemyGradeOrder1+1
        DecryptMode=0
    if IOFOrder >= len(IntOrFloat) and DecryptMode == 0:
        IOFOrder = 0
    if Order<len(ByteOrder)-3 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        writeNonFloat(BinaryRaw, TextOrder, Order, t1, t2)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
    if DecryptMode==2 and AugmentCounter>=144:
        DecryptMode = 3
        AugmentCounter = 0
        Order = 0
        IOFOrder = 0
    if DecryptMode==3 and AugmentCounter>=156:
        t2 = len(BinaryRaw) + 1
    if Order<len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        writeFloat(BinaryRaw, TextOrder, Order, t1, t2, IntOrFloat, IOFOrder)
        IOFOrder = IOFOrder + 1
        if (SelectedBIN == 4 or SelectedBIN == 6) and str(ByteOrder[Order+1])=='text':
            t1, t2, Order = OrderOfBytesENS(t1, t2, Order, ByteOrder, EnemyNameSize, EnemyNameOrder)
        else:
            t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        writeNonFloatEnd(BinaryRaw, TextOrder, Order, t1, t2)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
        if SelectedBIN == 4 or (SelectedBIN == 6 and DecodedBINFiles == 3):
            DecryptMode = 1
        Order = 0
        IOFOrder = 0
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==0:
        writeFloatEnd(BinaryRaw, TextOrder, Order, t1, t2, IntOrFloat, IOFOrder)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
        if SelectedBIN == 4 or (SelectedBIN == 6 and DecodedBINFiles == 3):
            DecryptMode = 1
        Order = 0
        IOFOrder = 0
    elif Order<len(ByteOrder)-3 and str(ByteOrder[Order])=='text' and DecryptMode == 0:
        writeZombieText(EnemyName, EnemyNameOrder, TextOrder, Order)
        t1, t2, Order, EnemyNameOrder = OrderOfBytesENO(t1, t2, Order, EnemyNameOrder)
    elif Order<len(ByteOrderES)-3 and ByteOrderES[Order]!=8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        writeNonFloat(BinaryRaw, TextOrderES, Order, t1, t2)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderES)
    elif Order<len(ByteOrderES)-3 and ByteOrderES[Order]==8 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        writeFloat(BinaryRaw, TextOrderES, Order, t1, t2, IntOrFloatES, IOFOrder)
        IOFOrder = IOFOrder + 1
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderES)
    elif Order==len(ByteOrderES)-3 and str(ByteOrderES[Order])!='text' and DecryptMode == 1:
        writeFloatEnd(BinaryRaw, TextOrderES, Order, t1, t2, IntOrFloatES, IOFOrder)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderES)
        if DecryptMode == 1:
            if EnemyGradeOrderES < EnemyGrades[EnemyGradeOrder1]:
                EnemyGradeOrderES=EnemyGradeOrderES+1
        Order = 0
        IOFOrder = 0
    elif Order<len(ByteOrder)-3 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and DecryptMode==2 and AugmentCounter<144:
        writeNonFloat(BinaryRaw, TextOrder, Order, t1, t2)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
    elif Order<len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==2 and AugmentCounter<144:
        writeFloat(BinaryRaw, TextOrder, Order, t1, t2, IntOrFloat, IOFOrder)
        IOFOrder = IOFOrder + 1
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
    elif Order==len(ByteOrder)-3 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and DecryptMode==2 and AugmentCounter<144:
        writeFloatEnd(BinaryRaw, TextOrder, Order, t1, t2, IntOrFloat, IOFOrder)
        t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrder)
        Order = 0
        IOFOrder = 0
        AugmentCounter = AugmentCounter + 1
    elif DecryptMode==3:
        if (Order==0 or Order==1 or Order>6) and ByteOrderA[Order]!=8 and AugmentCounter<156:
            writeNonFloat(BinaryRaw, TextOrderA, Order, t1, t2)
            if Order==1:
                ArmorBIN = calcNonFloat(BinaryRaw, TextOrderA, Order, t1, t2)
            t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderA)
        elif Order>=2 and Order<=6 and ByteOrderA[Order]!=8 and AugmentCounter<156:
            while ArmorCurrent < ArmorSlotCount:
                if ArmorCurrent < ArmorBIN:
                    writeNonFloat(BinaryRaw, TextOrderA, Order, t1, t2)
                    t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderA)
                else:
                    writeEmptyArmorSlot(TextOrderA, Order)
                    Order = Order + 1
                ArmorCurrent = ArmorCurrent + 1;  
        elif Order<len(ByteOrderA)-3 and ByteOrderA[Order]==8 and AugmentCounter<156:
            writeFloat(BinaryRaw, TextOrderA, Order, t1, t2, IntOrFloatA, IOFOrder)
            IOFOrder = IOFOrder + 1
            t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderA)
        elif Order==len(ByteOrderA)-3 and ByteOrderA[Order]==8 and AugmentCounter<156:
            writeFloatEnd(BinaryRaw, TextOrderA, Order, t1, t2, IntOrFloatA, IOFOrder)
            t1, t2, Order = OrderOfBytes(t1, t2, Order, ByteOrderA)
            Order = 0
            IOFOrder = 0
            ArmorCurrent = 0
            AugmentCounter = AugmentCounter + 1
if SelectedBIN != 6:
    Rows = zip(Row1, Row2)
    Writer = csv.writer(BinaryDecoded)
    for row in Rows:
        Writer.writerow(row)
    BinaryDecoded.close()
# End