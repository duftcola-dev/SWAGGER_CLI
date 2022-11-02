import click 
import os 
import re
import pathlib
import subprocess
from tkinter import Tk,filedialog

ROOT_DIR=str(pathlib.Path(__file__).resolve().parent.parent.parent)
SLASH="/"

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

def __Clone():
    os.system("git clone https://github.com/swagger-api/swagger-codegen")

def __Build():
    temp=ROOT_DIR+SLASH+"swagger-codegen"+SLASH
    print(temp)
    os.system(f"cd {temp} && .{SLASH}run-in-docker.sh mvn package")

def __InstallTkinter():
    result=subprocess.Popen(
        ["python","--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout,stderr=result.communicate()
    stdout=stdout.decode()
    pattern=re.compile(r"\d.\d\d")
    result=pattern.search(stdout)
    version=result.group()
    os.system(f"sudo apt-get install python{version}-tk")

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

def Interactive():
    exit=False
    choice=None
    while(exit==False):
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


@click.command()
def clone():
    """Clones the deppendencies for the code generator."""
    click.secho("Cloning SWAGGER deppendencies",fg="white",bg="green")
    __Clone()

@click.command()
def build():
    """Builds the deppendenecies for the code generator."""
    click.secho("Building deppendencies",fg="white",bg="green")
    __Build()
    click.secho("Installing tkinter version for :\n",fg="white",bg="green")
    os.system("python --version")
    __InstallTkinter()

@click.command()
@click.option("--input",default="",type=str,help="name of the input file example : swagger.yaml")
@click.option("--output",default="",type=str,help="folder name of the output example : out-server")
def generate(input:str,output:str):
    """Generates code using .yml files. Input .yaml files must be stored at /in.
    Generated code will be placed at /out"""
    click.secho("Generating",fg="white",bg="green")
    if input.strip() == "" or input is None:
        os.system("clear")
        click.secho("Warning",fg="white",bg="yellow")
        click.secho("A .json/.yaml file is require as input parameter.",fg="yellow")
        click.secho("Example : python cli  generate --input file_path/path/template.json",fg="yellow")
    if output.strip() == "" or output is None:
        os.system("clear")
        click.secho("Warning",fg="white",bg="yellow")
        click.secho("An output path for the generated code is reuqired",fg="yellow")
        click.secho("'.' is a valid path",fg="yellow")
        click.secho("Example : python cli  generate --input file_path/path/template.json --output .",fg="yellow")

    temp=ROOT_DIR+SLASH+"swagger-codegen"+SLASH
    input_path=ROOT_DIR+SLASH+"in"+SLASH+input # moving from /in
    _input_path=temp+"in"+SLASH+input # to /swagger-codegen/in
    _output_path=temp+"out"+SLASH+output
    ouput_path=ROOT_DIR+SLASH+"out"

    click.secho(f"-->{input}",fg="green")
    click.secho(f"-->{output}",fg="blue")
    if os.path.isfile(input_path) == False:
        click.secho(f"{input_path} not found",fg="red")
        click.secho("Aborting",fg="white",bg="yellow")
        return
    os.system(f"mv {input_path} {_input_path} ")# moving from /in to /swagger-codegen/in
    
    os.system(f"cd {temp} && .{SLASH}run-in-docker.sh generate -i in/{input} -l go -o  ./out/{output}")
    os.system(f"mv {_input_path} {input_path} ")# /swagger-codegen/in to moving from /in
    os.system(f"mv {_output_path} {ouput_path}")# /swagger-codegen/out to moving from /out
    





