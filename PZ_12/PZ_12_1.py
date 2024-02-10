# Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

import random

boys = [random.randint(150, 210) for _ in range(20)]
basketball = list(filter(lambda x: x >= 190, boys))
football = list(filter(lambda x: x < 190, boys))

print(f'Все юноши: {boys}\n'
      f'Направлены в баскетбольную команду:{len(basketball)}\n'
      f'Направлены в футбольную команду: {len(football)}')
