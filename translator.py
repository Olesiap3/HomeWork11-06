from pprint import PrettyPrinter
from pprint import pprint
from typing import KeysView
translate = {
    "hallo": "bonjour",
    "how are you": "comment allez-vous",
    "are you at home": "es tu à la maison",
    "thanks":"merci",
    "bon appetit":"bon appétit" 
}
pprint(translate)
kay = (input([]))
if kay in translate:
    text = translate[kay]
    pprint(text)
#{'are you at home': 'es tu à la maison',
#'bon appetit': 'bon appétit',
#'hallo': 'bonjour',
#'how are you': 'comment allez-vous',
#'thanks': 'merci'}
#how are you
#'comment allez-vous'