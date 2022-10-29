import click 
import os
import subprocess
from tkinter import Tk,filedialog



@click.command()
def pull():
    """Dowloads the swagger editor docker image"""
    click.secho("Downloading editor",fg="white",bg="green")
    result=subprocess.Popen(
        ["docker","images","-q","swaggerapi/swagger-editor"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout,stderr=result.communicate()
    
    if stdout == None or stdout=="":
        os.system("docker pull swaggerapi/swagger-editor")
    else:
        click.secho("This images already exists",fg="yellow")
        result=input("Do you want to reinstall this image? y/n: ")
        if result=="y" or result=="Y":
            os.system("docker rmi swaggerapi/swagger-editor:latest")
            os.system("docker pull swaggerapi/swagger-editor")
            os.system("docker images")

@click.command()
@click.option("--build",is_flag=True,help="Forces to build a new container always on localhost:8000")
@click.option("--url",default="localhost",type=str,help="Specify the url where the editor will be launched")
@click.option("--port",default=8000,type=str,help="Specify the port to be used")
def launch(build,url,port):
    """Launch the editor on localhost:8000"""
    if build:
        os.system(f"docker run -d -p 8000:8080 --name editor swaggerapi/swagger-editor")
        click.secho(f"Swagger editor running on locahost:8000/",fg="green")
        os.system("google-chrome http://localhost:8000/")
    else:
        if url != "localhost" or port != 8000:
            result=os.system(f"docker run -d -p {port}:8080 -e URL='{url}' --name editor swaggerapi/swagger-editor")
            if result==0:
                click.secho(f"Swagger editor running on {url}:{port}/",fg="green")
                os.system(f"google-chrome http://{url}:{port}/")
        else:
            result=os.system("docker start editor")
            if result==0:
                click.secho("Swagger editor running on :\n",fg="green")
                os.system("docker ps")
            else:
                click.secho("Container editor does not seem to exists.",fg="yellow")
                result=input("Do you wish to build a new editor ? y/n : ")
                options=["y","Y","Yes","yes"]
                if result in options:
                    click.secho("Creating container editor on locahost:8000",bg="green")
                    os.system("docker run -d -p 8000:8080 --name editor swaggerapi/swagger-editor")
                    click.secho("Swagger editor running on localhost:8000/",fg="green")
                    os.system("google-chrome http://localhost:8000/")
                else:
                    os.system("clear")
                    click.secho("Aborting",bg="yellow")

@click.command()
def remove():
    """Removes the editor container if exists"""
    result=os.system("docker rm editor")
    if result==0:
        click.secho("Swagge editor removed.",fg="red")
    else:
        click.secho("Cannot find container editor. Nothing to remove",fg="yellow")

@click.command()
@click.option("--interactive",is_flag=True,help="Allows to select the file from a browser")
@click.option("--path",default="",help="template .json/yml path")
def template(interactive,path):
    """Launch the editor on localhost:8000 using a template """
    if path !="":
        click.secho(f"Launching using template : {path}",fg="white",bg="green")
        os.system(f"docker run -d -p 8000:8080 -v $(pwd):/tmp -e SWAGGER_FILE={path} swaggerapi/swagger-editor")
        os.system("google-chrome http://localhost:8000/")
        return
    if interactive:
        root=Tk()
        root.withdraw()
        root.update()
        file_path=filedialog.askopenfilename()
        root.destroy()
        print(type(file_path))
        if len(file_path)==0:
            os.system("clear")
            click.secho("Aborting",fg="white",bg="yellow")
            click.secho("No path given",fg="yellow")
            return
        click.secho(f"Launching using template : {file_path} on localhost:8000 with container name : editor",fg="white",bg="green")
        os.system(f"docker run -d -p 8000:8080 -v $(pwd):/tmp -e SWAGGER_FILE={file_path} --name editor swaggerapi/swagger-editor")
        os.system("google-chrome http://localhost:8000/")
        return
    click.secho("You must at least provide an option : --path | --interactive",fg="yellow")


