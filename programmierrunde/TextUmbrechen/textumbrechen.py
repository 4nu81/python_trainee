class TextUmbrechen:
    def textUmwandeln(self, text, offset):
        worte = self.textZerlegen(text)
        text = self.textErstellen(worte, offset)
        return text

    def textZerlegen(self, text):
        text = text.replace('\n', ' ')
        return text.split()

    def textErstellen(self, worte, offset):
        zeilen = self.erzeugeZeilen(worte, offset)
        text = self.textBauen(zeilen)
        return text
        
    def erzeugeZeilen(self, worte, offset):
        zeilen = []
        while worte:
            nz = worte[0]
            del worte[0]
            while (len(nz) + len(worte[0]) + 1) <= offset:
                nz += ' ' + worte[0]
                del worte[0]
                if not worte:
                    break
            zeilen.append(nz)
        return zeilen
    
    def textBauen(self, zeilen):
        text = '\n'.join(zeilen)
        return text
