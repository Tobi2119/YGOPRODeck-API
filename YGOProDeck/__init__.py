import urllib.parse
import requests

# Classe einer YuGiOh Karte mit der ID, Namen, Art und in welchen Set es diese zu welcher Seltenheit gibt
class Card:
    def __init__(self, id:int, name:dict, set:list):
        # Orginale ID der Karte (unten links)
        self._id = id
        # Namen der Karte in mehreren Sprachen. z.B. {"en" : "Monster Reborn", "de" : "Wiedergeburt"}
        # Englisch wird immer angegeben zusätzlich können fr für French, de for German, it for Italian and pt for Portuguese
        self._name = name
        # Sets in welchen die Karte ist. z.B: [{"Set_Name" : }]
        self._set = set
    def Get_All_Names(self):
        return self._name
    def Get_Name(self, lang):
        if lang in self._name:
            return self._name[lang]
        return None
    def Get_ID(self):
        return self._id
    def Get_Set(self):
        return self._set

# Anfrage der API um eine Karte zu erhalten, der Englische Name wird immer abgefragt
def Get_Card(id:int = None, name:str = None, langs:list = ["en"]):
    # Kontrolle ob eine ID oder Name angegeben wurde
    if id == None and name == None:
        return None
    # Start URL der API
    API_URL = r"https://db.ygoprodeck.com/api/v7/cardinfo.php"
    # Hinzufügen der ID und oder des Namens
    URL = ""
    if id is not None and name is not None:
        URL = f"{API_URL}?id={urllib.parse.quote(str(id))}&name={urllib.parse.quote(name)}"
    if id is not None and name is None:
        URL = f"{API_URL}?id={urllib.parse.quote(str(id))}"
    if id is None and name is not None:
        URL = f"{API_URL}?name={urllib.parse.quote(name)}"
    # Anfrage mit der URL ohne Länderangebe für die Englische Version
    card_id = None
    card_names = {}
    card_sets = []
    response = requests.get(URL)
    data = response.json()
    card_id = data["data"][0]["id"]
    card_names["en"] = data["data"][0]["name"]
    for set in data["data"][0]["card_sets"]:
        card_set = {"set_name" : set["set_name"], "set_code" : set["set_code"], "set_rarity" : set["set_rarity"]}
        card_sets.append(card_set)
    # Erstelle für jede Sprache eine URL für die anfrage des Namens
    for lang in langs:
        if lang is not "en":
            try:
                Request_URL = f"{API_URL}?id={urllib.parse.quote(str(card_id))}&language={urllib.parse.quote(str(lang))}"
                response = requests.get(Request_URL)
                data = response.json()
                card_names[lang] = data["data"][0]["name"]
            except:
                pass
    #Rückgabe der Karte als Card Objekt
    return Card(id = card_id, name = card_names, set = card_sets)

if __name__ is "__main__":
    Monster_Reborn = Get_Card(name="Monster Reborn", langs=["de"])
    print(Monster_Reborn)