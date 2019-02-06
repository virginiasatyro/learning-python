x = 11          # meu x: global apenas para esse arquivo

import moda     # obtem acesso aos nomes presentes em moda     
moda.f()        # configura moda.x e não meu x 
print (x)       # 11 
print (moda.x)  # 99