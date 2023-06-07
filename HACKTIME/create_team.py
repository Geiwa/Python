import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai",
         "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek",
         "Dastan", "Maksat"]



team_1 = names[:len(names)//4]
team_2 = names[len(names)//4:len(names)//2]
team_3 = names[len(names)//2:3*len(names)//4]
team_4 = names[3*len(names)//4:]

print("Команда 1:", team_1)
print("Команда 2:", team_2)
print("Команда 3:", team_3)
print("Команда 4:", team_4)
