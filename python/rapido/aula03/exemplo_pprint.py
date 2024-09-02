# https://docs.python.org/3/library/pprint.html
import pprint

coisas = ["sardinha", "ovos", "lenhador", "cavaleiros", "ni"]
coisas.insert(0, coisas)
pprint.pp(coisas)
