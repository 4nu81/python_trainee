import setting

import ver1_1
import ver1_2

versions = {
    '1.1': ver1_1,
    '1.2': ver1_2
}

moduleversion = versions[setting.version]

m = moduleversion.module.Modul()

print m.pp()
