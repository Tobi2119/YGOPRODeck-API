# Classe einer YuGiOh Karte mit der ID, Namen, Art und in welchen Set es diese zu welcher Seltenheit gibt
class Karte:
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