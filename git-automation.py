from termcolor import *
import sys
import os
import subprocess
import shlex

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


    else:
        file_name = sys.argv[1]
        git_comment = sys.argv[2]
# ______________________________instruction________________________________
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(sys.argv[1])
            help_text = """
            First of all thank you for using my Git Automation Tool.\n\n
            1. If you haven't initialized your file yet, please follow the instruction form your newly created git repository and setup your folder.\n
            2. If you have your setup done. the follow the command pattern below:\n
            git-automation.py <file name> <commit.massage.here>\n
            demo command: git-automation.py myfile.txt "this is my comment"
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

#____________________________________ Executing the commands ____________________________________________________________
                    else:
                        if os.path.exists(file_path):
                            cprint('File found', 'magenta', attrs=['reverse', 'blink'])
                            com = git_comment.split('.')
                            com.reverse()
                            new_value = str()

                            for i in range(len(com)):
                                value = com[i]
                                new_value = value + " " + new_value
                                i += 1

                            git_add = f"git add {file_name}"
                            git_commit = f"git commit -m \"{new_value}\""
                            ga = shlex.split(git_add)

#_____________________________ Sub-processing the arguments______________________
                            sub_pro = subprocess.Popen(ga, shell=True)  # adding file to git
                            if sub_pro.wait() == 0:
                                sec_pro = subprocess.Popen(git_commit, shell=True)  # committing changes
                                if sec_pro.wait() == 0:
                                    subprocess.run(["git", "push"], shell=True)  # pushing file to repository

                        else:
                            cprint("The file doesn't exist.", 'magenta', attrs=['reverse', 'blink'])


if __name__ == '__main__':
    main()
