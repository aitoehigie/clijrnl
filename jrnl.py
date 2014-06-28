from cmd import Cmd
from time import ctime

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print "Hello, %s" % name

    def do_writejournal(self, args):
    	"""This writes an entry into your journal"""
    	if len(args) == 0:
    		pass
    	else:
    		filename = str(ctime()) + ".md"
    		with open(filename, "w") as file:
    			file.write(ctime()+": "+args)
    		print "Success!"

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')

