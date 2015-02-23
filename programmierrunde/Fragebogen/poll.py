
import starten
import cmdlnparser

commands = {
    'starten' : starten,
    #'antworten' : antworten.Antworten,
}

command = cmdlnparser.cmdln_poll()

commands[command].execute()
