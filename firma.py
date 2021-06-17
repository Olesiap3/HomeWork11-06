from pprint import pprint
marks = {
    "Phone number": 0,
    "Email": 1,
    "Position": 2,
    "Room nuber": 3,
    "Skype": 4
}
firma = {
    "Sylvester Stalone":[41779648761, "stal.sylvester@gmx.com", "President", 1, "The_Boss" ],
    "Jennifer Aniston":[41779648762, "aniston@gmx.com", "Manager", 4, "Anisson"],
    "Nicole Kidman":[41779648763, "kidman@gmx.com", "Executive Director", 3, "NiKi" ],
    "Sharon Stone":[41779648764, "ssharon@gmx.com", "Consultant", 5, "Sharon" ],
    "Keanu Reeves":[41779648765, "matrix.forever@gmx.com", "Managing Direktor",6, "Neo"],
    "George Clooney":[41779648766, "the.boss@gmx.com", "Vice President", 2, "HeyDoro"]
}
pprint(firma)
pprint(firma["Keanu Reeves"][marks["Skype"]])

#==================add===========================
new_persone = input("Name :")
name = input("Phone Namber :")
email =input("Email :")
position = input("Position :") 
room_number = input("Room number :")
skype = input("Skype :")
data =[name, email, position, room_number, skype]
firma[new_persone] = data
pprint(firma)

#==========del==============
fire = input("Not more work hier :")
del firma [fire]
pprint(firma)

#===========serch==============
look_you = input("I‘m looking for :")
if look_you in firma.keys():
    person = firma.get(look_you)
    pprint(look_you)

