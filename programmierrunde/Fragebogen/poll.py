
import starten, antworten
import cmdlnparser

commands = {
    'starten' : starten,
    'antworten' : antworten,
}

command = cmdlnparser.cmdln_poll()

commands[command].execute()
