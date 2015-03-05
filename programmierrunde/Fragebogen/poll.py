
import starten, antworten, auswerten
import cmdlnparser

commands = {
    'starten' : starten,
    'antworten' : antworten,
    'auswerten' : auswerten,
}

command = cmdlnparser.cmdln_poll()

commands[command].execute()
