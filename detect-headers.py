import cmd
import re
dicts = {};
class shell(cmd.Cmd):
    def do_sherlock(self,line):
        args = line.split();
        for arg in args:
            if "vuln_scan:" in arg:
                comment = args[args.index("vuln_scan:")+1];
                headers = args[args.index(comment)+1];
                headers = headers.split(",");
                
                for i in headers:
                    i = i.replace("{", "");i = i.replace("}", "");
                    i = i.replace("'", ""); i = i.replace('"', "");
                    
                    i = i.split(":");
                    dicts[i[0]] = i[1];
                    print(i);
                arg = arg.replace("vuln_scan:", "");
                print(comment, dicts);
    def emptyline(self):
        pass;
    
shell().cmdloop();
