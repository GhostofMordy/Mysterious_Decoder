
"""
╭━━━╮╱╱╱╱╱╱╱╭┳╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━╮╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱┃┃┃╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃╱╱╱╱╱╭╯╰╮
┃┃╱╰╋━━┳━╮╭━╯┃┃╭━━┫┃╭┳━━┳━━┳━━╮┃╭╮╭╮┣╮╱╭┳━┻╮╭╋━━┳━┳┳━━┳━━╮
┃┃╱╭┫╭╮┃╭╮┫╭╮┃┃┃┃━┫╰╯┫┃━┫┃━┫╭╮┃┃┃┃┃┃┃┃╱┃┃━━┫┃┃┃━┫╭╋┫┃━┫━━┫
┃╰━╯┃╭╮┃┃┃┃╰╯┃╰┫┃━┫╭╮┫┃━┫┃━┫╰╯┃┃┃┃┃┃┃╰━╯┣━━┃╰┫┃━┫┃┃┃┃━╋━━┃
╰━━━┻╯╰┻╯╰┻━━┻━┻━━┻╯╰┻━━┻━━┫╭━╯╰╯╰╯╰┻━╮╭┻━━┻━┻━━┻╯╰┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╰━━╯
"""

def Keys_of_Candlekeep(mystery):
    if mystery <= 1:
        return False
    if mystery <= 3:
        return True
    if mystery % 2 == 0 or mystery % 3 == 0:
        return False
    fenrir = 5
    while fenrir * fenrir <= mystery:
        if mystery % fenrir == 0 or mystery % (fenrir + 2) == 0:
            return False
        fenrir += 6
    return True

def Trickery_of_Mordenkainen(deez, nuts):
    Vault = []
    for goblin in range(deez, nuts):
        if Keys_of_Candlekeep(goblin):
            Vault.append(goblin)
    return Vault

Ernst_Larnak = 69420 + 1
Ned_Shakeshaft = "Mysterious_Code.txt"

with open(Ned_Shakeshaft, "r") as Sword_of_Souls:
    Emilio_the_Great = Sword_of_Souls.read()

Drakkar = ""

Barons_Son = Trickery_of_Mordenkainen(Ernst_Larnak, len(Emilio_the_Great))
for cleave in Barons_Son:
    Drakkar += Emilio_the_Great[cleave]
Drakkar = Drakkar[:226]

# Display the decoded message
print(Drakkar)
