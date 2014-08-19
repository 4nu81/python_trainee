###WARNING: Do not change anything in this file.
###To change a setting, go to Options in the Main Menu.
##
###Keys:
##L 276
##R 275
##T 273
##F 32
##
###Effects:
##PSD 4
##Light True
##ThO 0
##TuO 0
##ExO 0
##BuO False
##
###Sound:
##M 1.0
##E 1.0

def LoadSettings():
    file = open("Data/Settings.txt","r")
    data = file.readlines()
    file.close()
    data2 = []
    for line in data:
        if (not line.startswith("#")) and (not line.startswith("\n")):
            if line.endswith("\n"):
                data2.append(line[:-1])
            else:
                data2.append(line)
    for setting in data2:
        if   setting.startswith("L ")         : LEFTTURN       = int(setting[2:])
        elif setting.startswith("R")          : RIGHTTURN      = int(setting[2:])
        elif setting.startswith("T ")         : THRUST         = int(setting[2:])
        elif setting.startswith("F")          : FIRE           = int(setting[2:])
        elif setting.startswith("PSD")        : PSDDENSITY     = int(setting[4:])
        elif setting.startswith("Light True") : LIGHT          = True
        elif setting.startswith("Light False"): LIGHT          = False
        elif setting.startswith("ThO")        : THRUSTOCCLUDE  = int(setting[4:])
        elif setting.startswith("TuO")        : TURNOCCLUDE    = int(setting[4:])
        elif setting.startswith("ExO")        : EXPLODEOCCLUDE = int(setting[4:])
        elif setting.startswith("BuO True")   : BULLETOCCLUDE  = True
        elif setting.startswith("BuO False")  : BULLETOCCLUDE  = False
        elif setting.startswith("M")          : MUSICVOLUME    = float(setting[2:])
        elif setting.startswith("E")          : FXVOLUME       = float(setting[2:])
    return LEFTTURN,RIGHTTURN,FIRE,THRUST,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME
def WriteSettings(LEFTTURN,RIGHTTURN,FIRE,THRUST,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME):
    file = open("Data/Settings.txt","w")
    line1  = "#WARNING: Do not change anything in this file."
    line2  = "#To change a setting, go to Options in the Main Menu."
    line3  = ""
    line4  = "#Keys:"
    line5  = "L "+str(LEFTTURN)
    line6  = "R "+str(RIGHTTURN)
    line7  = "T "+str(THRUST)
    line8  = "F "+str(FIRE)
    line9  = ""
    line10 = "#Effects:"
    line11 = "PSD "+str(PSDDENSITY)
    if LIGHT: line12 = "Light True"
    else:     line12 = "Light False"
    line13 = "ThO "+str(THRUSTOCCLUDE)
    line14 = "TuO "+str(TURNOCCLUDE)
    line15 = "ExO "+str(EXPLODEOCCLUDE)
    if BULLETOCCLUDE: line16 = "BuO True"
    else:             line16 = "BuO False"
    line17 = ""
    line18 = "#Sound:"
    line19 = "M "+str(round(MUSICVOLUME,2))
    line20 = "E "+str(round(FXVOLUME,2))
    data = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20]
    data2 = []
    for line in data:
        data2.append(line+"\n")
    file.writelines(data2)
    file.close()
