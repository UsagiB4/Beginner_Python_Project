from termcolor import *
import sys
import os
import subprocess

os.system('color')
#______ Checking if the git initialization file exists_______
git_init_dir = os.getcwd() + "\.git\ "
if os.path.exists(git_init_dir):
    print(git_init_dir)
    cprint('Git init exists', 'green', attrs=['reverse', 'blink'])
else:
    cprint('Git init not exists.', 'red', attrs=['reverse', 'blink'])
    cprint('Please initialize your file to upload to github.', 'red', attrs=['reverse', 'blink'])






#_______________________________main function here_____________________________________________
def main():
    if len(sys.argv) == 1:
        cprint('No valid input found', 'red', attrs=['reverse', 'blink'])
        cprint('type --help or -h to get the instructions', 'blue', attrs=['reverse', 'blink'])

#______________________________instruction________________________________
    else:
        file_name = sys.argv[1]
        git_comment = sys.argv[2]

        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(sys.argv[1])
            help_text = """
            First of all thank you for using my Git Automation Tool.\n\n
            1. If you haven't initialized your file yet, please follow the instruction form your newly created git repository and setup your folder.\n
            2. If you have your setup done. the follow the command pattern below:\n
            git-automation.py <file name> <commit.massage.here>\n
            demo command: git-automation.py myfile.txt this.is.my.comment
            3. AND DONE. it's that easy.
            """
            help_text = colored(help_text, 'blue')
            print(help_text)

#____________________________________ handling git commands _________________________________________________

        elif file_name != '--help' or file_name != '-h' and len(sys.argv) == 2:
            current_wd = os.getcwd()
            file_path = f"{current_wd}\/{file_name}"

#_________________________________________ Checking for .gitignore ____________________________________________
            if os.path.exists('.gitignore'):
                with open('.gitignore', 'r') as ign:
                    ignore_lists = ign.readlines()
                    if file_name in ignore_lists:
                        print('This file is inside .gitignore file. You can not push it to the repository.')

#____________________________________ pushing file ____________________________________________________________
                    else:
                        if os.path.exists(file_path):
                            print('Yes! you can push')
                            com = git_comment.split('.')
                            print(com)
                        else:
                            cprint("The file doesn't exist.", 'magenta', attrs=['reverse', 'blink'])


if __name__ == '__main__':
    main()
