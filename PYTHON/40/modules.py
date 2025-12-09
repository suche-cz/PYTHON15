import sys, math, random, hashlib
import my_code1
import my_test
import new

"""
library (knihovna)
module = knihovna = 1 python soubor
package = balíček = sbírka více python souborů
"""

# dynamické přidání cesty kde má hledat zdrojáky
sys.path.insert(0, 'c:\\AKADEMIE\\PYTHON15\\PYTHON\\39')

import funkce_argumenty

print(sys.path) # toto obsahuje složky, kde hledá zdrojáky pro import
print(my_test.MY_NAME)
print(funkce_argumenty)