import os, sys

operations = ["--imp", "--exp", "--reserve", "--show", "--report"]
descriptions = ["--imp <json|url> <filename>            | Import specified file|URL into movie DB", 
                "--exp <json> <filename>                | Export from movie DB to a file", 
                "--reserve <movie> <amount>             | Reserve tickets", 
                "--show <movie|list>                    | Show ticket reservations", 
                "--report <report|list> [export-file]   | Print reports or export to a file"]
file_dir = "backup/"
separator = ';'

def print_help(cmd = None):
    if cmd is None:
        print("********************************************************************************")
        print("*                             Movie theater TroY®                              *")
        print("********************************************************************************")
        for desc in descriptions:
            print(desc)
        print("********************************************************************************")
    else:
        print("Wrong number of parameters.")
        print(descriptions[operations.index(cmd)])
        print("")

def operation(opp):
    return opp[2:]

def imp(args):     
    if len(args) != 4:
        print_help(args[1])
        return

    #TODO: call import with parameters
    raise NotImplementedError("imp(args)") 

def exp(args):     
    if len(args) != 4:
        print_help(args[1])
        return

    #TODO: call import with parameters
    raise NotImplementedError("exp(args)") 

def reserve(args):     
    if len(args) != 4:
        print_help(args[1])
        return

    #TODO: call import with parameters
    raise NotImplementedError("reserve(args)") 

def show(args):     
    if len(args) != 3:
        print_help(args[1])
        return

    #TODO: call import with parameters
    raise NotImplementedError("show(args)") 

def report(args):     
    if len(args) != 4:
        print_help(args[1])
        return

    #TODO: call import with parameters
    raise NotImplementedError("report(args)") 
    
def main(args):
    #Check for valid operations & print help
    if len(args) < 2 or args[1] not in operations:
        print("Wrong or non existing operation!" + os.linesep)
        print_help()
        return

    #create accounts dir if not exists
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    #Execute operation    
    getattr(sys.modules[__name__], operation(args[1]))(args)

if __name__ == '__main__':
    #Test parameters
    #sys.argv.append('--report')
    ################

    main(sys.argv)