# Important stuff

import binascii # Used for HEX reading
import csv      # Used for writing down numbers in .txt file
import struct   # Used for HEX float processing
from collections import defaultdict

# ---------------

# Prompt

print('Availble commands:')
print('')
print('1. Weapons.csv')
print('2. Ammo.csv')
print('3. Equipment.csv')
print('')
print('0. Exit the app')
print('')
SelectedCSV = int(input('Select the .csv you want to decode: '))

if SelectedCSV == 0:
    exit()
elif SelectedCSV > 3 or SelectedCSV < 0:
    raise ValueError('The selected number is invalid. Try again.')

# Main code

if SelectedCSV == 1:
    CSVFile = 'weapons.csv'
    BinaryEncoded = open('Output\weapons.bin', "wb")
elif SelectedCSV == 2:
    CSVFile = 'ammo.csv'
    BinaryEncoded = open('ammoencode.bin', "wb")
elif SelectedCSV == 3:
    CSVFile = 'equipment.csv'
    BinaryEncoded = open('Output\equipment.bin', "wb")

## DO NOT CHANGE
## -------------
ByteOrder1 = [4, 4, 4, 2, 2, 4, 4, 4, 8, 8, 8, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 4, 2, 4, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 8, 8, 4, 4, 4, 8, 4, 4, 4, 2, 4]
ByteOrder2 = [4, 2, 8, 2, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4]
ByteOrder3 = [4, 4, 4, 2, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 4]
IntOrFloat1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
IntOrFloat2 = [1]
IntOrFloat3 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 0 - int;
# 1 - float
if SelectedCSV == 1:
    ByteOrder = ByteOrder1
    IntOrFloat = IntOrFloat1
elif SelectedCSV == 2:
    ByteOrder = ByteOrder2
    IntOrFloat = IntOrFloat2
elif SelectedCSV == 3:
    ByteOrder = ByteOrder3
    IntOrFloat = IntOrFloat3
Order = 0
IOFOrder = 0
Numbers = []
RowCleaner = 0
RowsConverted = 0
## -------------

# Reads stuff and cleans empty rows

columns = defaultdict(list)

with open(CSVFile) as Decodedfile:
    Reader = csv.reader(Decodedfile)
    for row in Reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
Numbers = columns[1]
while RowCleaner < len(Numbers):
    if Numbers[RowCleaner] == '':
        Numbers.pop(RowCleaner)
        RowCleaner = RowCleaner + 1
    else:
        RowCleaner = RowCleaner + 1

RowCleaner = 0
while RowCleaner < len(Numbers):
    if Numbers[RowCleaner] == '':
        Numbers.pop(RowCleaner)
        RowCleaner = RowCleaner + 1
    else:
        RowCleaner = RowCleaner + 1
        
# ----------------------------------
# Fun stuff begins

while RowsConverted < len(Numbers):
    if IOFOrder >= len(IntOrFloat):
        IOFOrder = 0
    if Order<len(ByteOrder)-2 and ByteOrder[Order]!=8:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrder[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order<len(ByteOrder)-2 and ByteOrder[Order]==8:
        NormalString = Numbers[RowsConverted]
        if IntOrFloat[IOFOrder] == 0:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrder[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrder)-2 and ByteOrder[Order]!=8:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrder[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=0
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrder)-2 and ByteOrder[Order]==8:
        NormalString = int(Numbers[RowsConverted])
        if IntOrFloat[IOFOrder] == 0 and CSVFile != 2:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrder[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1 or CSVFile == 2:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        Order=0
        RowsConverted=RowsConverted+1
BinaryEncoded.close()

