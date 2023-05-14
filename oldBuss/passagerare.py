import random

class Passagerare:
    def __init__(self, namn, ålder, kön):
        self.namn = namn
        self.ålder = int(ålder)
        self.kön = kön


    villStigaAv = False
    arg = False
    
    def slumpmässigtViljaStigaAv(self):
        if random.randint(1, 5) == 1:
            self.villStigaAv = True

    def åk(self):
        if self.villStigaAv:
            self.arg = True

    def argFras(self):
        return self.ageSwitch(
            "waah! waah!", 
            "Åhh nej! Var är vi?",
            "Är du dum i huvudet? Stanna bussen!",
            "Ursäkta, busschaufför..? Du passade min plats!"
            )
        
    def petaFras(self):
        match self.kön:
            case "m":
                return self.ageSwitch(
                    "goo goo ga ga",
                    "Jag vill inte gå till skolan.",
                    "Jag blir åksjuk från att titta på mobilen",
                    "Jag är så upptagen"
                )
            case "f":
                return self.ageSwitch(
                    "babababaa",
                    "Vädret är skönt i dag",
                    "Jag har för mycket läxor..",
                    "Busschauffören kör jättebra"
                )
            case _:
                return self.ageSwitch(
                    "zzz",
                    "Jag är hungrig",
                    "Hejsan",
                    "Jag är trött"
                )

    def ageSwitch(self, bebisFras, barnFras, tonårigFras, vuxenFras):
        if self.ålder < 3:
            return bebisFras
        elif self.ålder < 13:
            return barnFras
        elif self.ålder < 20:
            return tonårigFras
        else:
            return vuxenFras