import kommandline
import textdatei
import textumbrechen
import ausgabe

cmd = kommandline.kommandline()
td = textdatei.textdatei()
tu = textumbrechen.TextUmbrechen()
ausg = ausgabe.ausgabe()

filename, max_length = cmd.readCmdln()
text = td.textLesen(filename)
text = tu.textUmwandeln(text, max_length)
filename = td.dateiSpeichern(filename, text, max_length)
ausg.feedbackAusgaben(filename)
