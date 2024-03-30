import random
import asyncio

server_pet = None

def adopt_pet(pet_name, species):
    global server_pet
    if server_pet is None:
        pet_name = pet_name.capitalize()  
        species = species.capitalize()  
        server_pet = {
            'name': pet_name,
            'species': species,
            'hunger': 50,
            'max_hunger': 100,  
            'happiness': 50,
            'max_happiness': 100,  
            'level': 1,
            'experience': 0
        }
        return f'{pet_name} isimli bir {server_pet["species"]} sahiplendin!'
    else:
        return "Zaten sunucuda bir hayvan var!"





def feed_pet():
    global server_pet
    if server_pet is not None:
        if server_pet['hunger'] >= server_pet['max_hunger']:
            return f"{server_pet['name']} tok, şuan yemek yemek istemiyor!"
        else:
            server_pet['hunger'] = min(server_pet['hunger'] + 10, server_pet['max_hunger'])
            server_pet['happiness'] = min(server_pet['happiness'] + 5, server_pet['max_happiness'])
            server_pet['experience'] += 10
            if server_pet['experience'] % 100 == 0:  
                level_up()
                return f"{server_pet['name']} seviye {server_pet['level']}'e yükseldi!"
            else:
                return f"{server_pet['name']}'yi besledin Açlık 10 arttı!"






def play_with_pet():
    global server_pet
    if server_pet is not None:
        if server_pet['happiness'] >= server_pet['max_happiness']:
            return f"{server_pet['name']} yorgun, şuan oynamak istemiyor"
        else:
            server_pet['hunger'] = max(server_pet['hunger'] - 5, 0)
            server_pet['happiness'] = min(server_pet['happiness'] + 10, server_pet['max_happiness'])
            server_pet['experience'] += 10
            if server_pet['experience'] % 100 == 0:  
                level_up()
                return f"{server_pet['name']} seviye {server_pet['level']}'e yükseldi!"
            else:
                return f'{server_pet["name"]} ile oynadın! Mutluluk 10 arttı!'





def level_up():
    global server_pet
    server_pet['level'] += 1
    server_pet['max_hunger'] += 10  
    server_pet['max_happiness'] += 10  





def new_pet(species, pet_name=None):
    global server_pet
    if server_pet is None:
        server_pet = {
            'name': pet_name,
            'species': species,
            'hunger': 50,
            'max_hunger': 100,  
            'happiness': 50,
            'max_happiness': 100,  
            'level': 1,
            'experience': 0
        }
        return f'Evcil hayvanı {pet_name} adlı bir {server_pet["species"]} ile değiştirdiniz!'
    else:
        server_pet = None
        return new_pet(species, pet_name)





def get_pet_info():
    global server_pet
    if server_pet is not None:
        pet_info = server_pet
        return f'''
        **{pet_info['name']}'nın bilgisi:**
        Tür: {pet_info['species']}
        Açlık: {pet_info['hunger']} / {pet_info['max_hunger']}
        Mutluluk: {pet_info['happiness']} / {pet_info['max_happiness']}
        Level: {pet_info['level']}
        Deneyim: {pet_info['experience']}
        '''
    else:
        return "Sunucu için evcil hayvan bulunmamaktadır. Önce bir tane sahiplen!"





def get_random_pet_name():
    names = ['Boncuk', 'Karabaş', 'Pamuk', 'Zeytin', 'Fındık', 'Karamel', 'Çikolata', 'Sultan', 
             'Şans', 'Prens', 'Prenses', 'Minnoş', 'Cici', 'Fıstık', 'Zuzu', 'Lola', 'Şanslı', 'Kuki', 'Kızıl', 'Kuyruk']
    return random.choice(names)





async def decrease_hunger():
    global server_pet
    while True:
        await asyncio.sleep(240)
        if server_pet is not None:
            decrease_amount = random.randint(1, 10)
            server_pet['hunger'] = max(server_pet['hunger'] - decrease_amount, 0)
            if server_pet['hunger'] <= 0:
                print(f"{server_pet['name']} açlıktan öldü. Yeni bir hayvan sahiplen!")
                server_pet = None





async def decrease_happiness():
    global server_pet
    while True:
        await asyncio.sleep(240)
        if server_pet is not None:
            decrease_amount = random.randint(1, 10)
            server_pet['happiness'] = max(server_pet['happiness'] - decrease_amount, 0)
            if server_pet['happiness'] <= 0:
                escape_chance = abs(server_pet['happiness'])
                if random.randint(1, 100) <= escape_chance:
                    print(f"{server_pet['name']} mutsuz olduğu için kaçtı. Yeni bir hayvan sahiplen!")
                    server_pet = None
