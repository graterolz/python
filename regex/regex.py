# importando el modulo de regex de python
# import re
# compilando la regex
# patron = re.compile(r'\bfoo\b')  # busca la palabra foo
# print(patron)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)