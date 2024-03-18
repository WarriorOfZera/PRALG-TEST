lista_filmova = [{'naziv' : 'A beautiful mind', 'br_poz' :3000, 'br_neg' : 30},
                  {'naziv' : 'A beautiful mind', 'br_poz' :30, 'br_neg' : 30},
                    {'naziv' : 'A beautiful mind', 'br_poz' :30041, 'br_neg' : 30},
                    {'naziv' : 'Lajanje na Zvijezde', 'br_poz' : 1500000, 'br_neg' : 150},
                    {'naziv' : 'Boban Rajovic the Movie the Game' , 'br_poz': 120000001, 'br_neg' : 100}]

max_film = {}
max_value = 0

for film in lista_filmova:
    if film["br_poz"] > max_value:
        max_value = film['br_poz']
        max_film = film
print(max_film)
print("--------------------------")
term = input("Unijeti termin za pretragu: ")
for film in lista_filmova:
    if film['naziv'].startswith(term):
        print(film)