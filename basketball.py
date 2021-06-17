from pprint import pprint
from typing import KeysView
player_card = {
    "Leon Porc":[1.97],
    "Sandro Gard":[1.89],
    "Pedro Coppello":[1.92],
    "Marc Sukini":[1.86],
    "Gordon Rasini":[1.95]
}
pprint(player_card)

#Add
print("========Add============================")
new_player_card1 = {"Olesia Ayieko":[1.6]}
player_card.update(new_player_card1)
pprint(player_card)

#Del
pprint("======Del=============================")
del player_card ["Olesia Ayieko"]
pprint(player_card)

#Serch
pprint("=======Serch============================")
key = "Gordon Rasini"
if key in player_card:
    player = player_card[key]
    print("Player", player)
else:
   pprint("Игрок не найден")
pprint("=======or Serch=========================")
player = player_card.get(key)
pprint(player)

#Zamena
pprint("=======Change======================")
pprint(player_card)
print("Leon Porc takes a break,\n instead him will Robert Villian")
del player_card["Leon Porc"]
new_player_card2 = {"Robert Villian":[1.90]}
player_card.update(new_player_card2)
pprint(player_card)