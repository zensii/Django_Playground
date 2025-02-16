import os
import subprocess
import sys
'''
USAGE: python name_of_this_script.py project_name=your_project_name_here app_name=your_app_name_here

This script only works on WINDOWS you can tweak the dir names of the activation scripts 
and it should work on linux/mac aswell.

Be free to modify and change parameter names/anything you dont like

I made this for me and my VsCode brothers that don't have or don't want to use PyCharm Pro
'''


def create_venv():
    print(f"Creating venv")
    subprocess.run([sys.executable, "-m", "venv", "venv"])

def create_requirements():
    print("Creating requirements.txt")
    with open("requirements.txt", "w") as f:
        f.write("django\npsycopg2\n")

def install_dependencies():
    print("Installing dependencies")
    subprocess.run([r".\venv\Scripts\pip3.11.exe", "install", "-r", "requirements.txt"])

def start_django_project(project_name="base"):
    print(f"Starting Django project: {project_name}")
    subprocess.run(["django-admin", "startproject", project_name])

def create_templates_folder(project_name="base"):
    print("Creating templates folder and index.html")
    templates_path = os.path.join(project_name, "templates")
    os.makedirs(templates_path, exist_ok=True)
    with open(os.path.join(templates_path, "index.html"), "w") as f:
        f.write("<h1>Hello, Django!</h1>")

def start_django_app(project_name, app_name):
    print(f"Creating Django app: {app_name}")
    subprocess.run([r".\venv\Scripts\python.exe", f"{project_name}\manage.py", "startapp", app_name])

def move_folders_and_files_into_project_folder(project_name, app_name):
    print("Moving directories into the project folder....")
    subprocess.run(["move", app_name, project_name], shell=True, check=True)
    subprocess.run(["move", "requirements.txt", project_name], shell=True, check=True)
    subprocess.run(["move", "venv", project_name], shell=True, check=True)

def main():
    args = sys.argv[1:]
    project_name = ""
    app_name = ""

    for arg in args:
        if "project_name=" in arg:
            project_name = arg.split("=")[-1]
        elif "app_name=" in arg:
            app_name = arg.split("=")[-1]

    if not project_name or not app_name:
        print("Usage: python setup_script.py project_name=your_project_name app_name=your_app_name")
        sys.exit(1)

    create_venv()

    create_requirements()

    install_dependencies()

    start_django_project(project_name)

    create_templates_folder(project_name)

    start_django_app(project_name, app_name)

    move_folders_and_files_into_project_folder(project_name, app_name)

    print("Setup complete!")
    print("----------------------------------------------------------------")
    print("Dont forget to setup your templates, staticfiles and db setting in your settings.py file!")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    main()
