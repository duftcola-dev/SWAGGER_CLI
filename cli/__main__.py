
from tkinter import filedialog,Tk 
import os
import pathlib


# Swagger codegen

ROOT_DIR=str(pathlib.Path(__file__).resolve().parent.parent)
SLASH="/"


def Install():
    os.system("git clone https://github.com/swagger-api/swagger-codegen")

def Build()->bool:
    temp=ROOT_DIR+SLASH+"swagger-codegen"+SLASH
    os.system(f"cd {temp} && .{SLASH}run-in-docker.sh mvn package")

def SearchFile()->str:
    root=Tk()
    root.withdraw()
    root.update()
    file_path=filedialog.askopenfilename()
    root.destroy()
    return str(file_path)

def SearchDir()->str:
    root=Tk()
    root.withdraw()
    root.update()
    dir_path=filedialog.askdirectory()
    root.destroy()
    return str(dir_path)


def Generate():
    input=SearchFile()
    output=SearchDir()
    if os.path.isfile(input) == False:
        print(f"{input} cannot be found")
        return
    if os.path.isdir(output) == False:
        print(f"{output} cannot be found")
        return
    temp=ROOT_DIR+SLASH+"swagger-codegen"+SLASH
    os.system(f"cd {temp} && .{SLASH}run-in-docker.sh generate -i {input} -l go -o {output}")
    

def  Help():
    os.system("clear")
    print("""
    0) CLONE --> Clones/downloads the code gen repository
    1) BUILD --> Build the code gen deppendencies. (it takes a while)
    2) GENERATE --> Genereates the actual server stubs using a json/yaml file as input
                    and a repository as output.

    3) help,h ---> Shown this instructions. Finishes the application. 
       quit, exit, q ,CRTL + C ---> Finishes the application.
    """)

# Swagger Editor

def Pull():
    """Dowloads the swagger editor docker image"""
    os.system("docker pull swaggerapi/swagger-editor")

def RunLocalhost():
    """Runs the image on locahost:80 by default NOT TESTED"""
    os.system("docker run -d -p 80:8080 swaggerapi/swagger-editor")

def RunOnUrl(url):
    """Runs on the defined URL NOT TESTED"""
    os.system(f"docker run -d -p 80:8080 -e URL='{url}' swaggerapi/swagger-editor")

def RunOnFile(file_path):
    """Runs the swagger editor on locahost using a file definition
    in json or yml
    
    NOT TESTED"""
    os.system(f"docker run -d -p 80:8080 -v $(pwd):/tmp -e SWAGGER_FILE={file_path} swaggerapi/swagger-editor")

def main():
    exit=False
    choice=None
    while(exit==False):
        os.system("clear")
        options=[Install,Build,Generate]
        print(ROOT_DIR)
        print("OPTIONS\n")
        print("0) CLONE\n")
        print("1) BUILD\n")
        print("2) GENERATE\n")
        print("3) HELP\n")
        print("3 , help, h ---> for display manual")
        print("quit, q, exit, crtl + C ---> to finish the cli\n")

        try:
            choice=(input("CHOICE (numbers only) : "))
        except KeyboardInterrupt as err:
            exit=True
            print("\n")
            break # ^C key


        if choice=="quit" or choice=="q" or choice=="exit":
            exit=True
            break
        if choice=="help" or choice=="h" or choice=="3":
            Help()
            exit=True
            break
        choice=int(choice)
        if choice < 0 or choice > len(options):
            print("Invalid choice number")
            return
        options[choice]()
    return

if __name__ == "__main__":

    main()
