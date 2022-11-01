#!/usr/bin/env python3

import cmd

''' Console for AirBnB Clone Project
'''


class HBNBCommand(cmd.Cmd):
    ''' Implement entry point of command interpreter
    '''

    prompt = "(hbnb) "

    def do_quit(self, args):
        ''' Quit command implementation
        '''
        return True

    def do_EOF(self, args):
        ''' EOF signal to exit
        '''
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
