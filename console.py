#!/usr/bin/python3
import cmd
""" The console of our AirBNB"""


class HBNBCommand(cmd.Cmd):
    """ My HBNB COMMAND INTERPRETER """
    prompt = "(hbnb) "

    def emptyline(self):
        """ nothing """
        pass

    def do_quit(self, arg):
        """ Exit with quit ?"""
        return True

    def do_EOF(self, arg):
        """ EOF exit """
        print("")
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
