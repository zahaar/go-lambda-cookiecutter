import os
import shutil
import stat
import subprocess

EVENTS_PATH = {
    "sns": "./events/sns_event.json",
    "s3": "./events/s3_event.json",
    "api_gw": "./events/api_gw_event.json",
}

def handleError(func, path, exc_info):
    print('Handling Error for file ' , path)
    print(exc_info)
    # If file has access issue...
    if not os.access(path, os.W_OK):
       # ...change the permission of the file
       os.chmod(path, stat.S_IWUSR)
       # ...and call the calling function again
       func(path)


def unlink_other_events(event_type):
    for key , path in EVENTS_PATH.items():
        if key == event_type:
            continue
        unlink_if_exists(path)
    subprocess.run(["mv", EVENTS_PATH[event_type], "./events/event.json"])

def unlink_other_go_files(event_type):
    for key, _ in EVENTS_PATH.items():
        if key == event_type:
            continue
        unlink_if_exists(f"{key}.go")

    # and rename to main.go 
    subprocess.run(["mv", f"{event_type}.go", "main.go"])



def unlink_if_exists(path):
    if os.path.exists(path):
        os.unlink(path)

def remove_tree(path):
    ## Try to remove tree; if failed show an error using try...except on screen
    try:
        shutil.rmtree(path)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))


if __name__ == "__main__":
    go_module_path = "{{cookiecutter.go_module_path}}"
    add_git = "{{cookiecutter.add_git}}"
    event_type = "{{cookiecutter.event_type}}".lower()

    #rm leftover events 
    unlink_other_events(event_type)

    #rm leftover LICENSES 
    remove_tree('./licenses')

    #rm leftover *.go 
    unlink_other_go_files(event_type)

    # tidy Go Packages 
    subprocess.run(["go", "mod", "init", go_module_path])
    subprocess.run(["go", "mod", "tidy"])

    # build SAM 
    subprocess.run(["make", "sam-build"])

    # create envs.json file
    subprocess.run(["cp", "envs.example.json", "envs.json"])

    if add_git:
        subprocess.run(["git", "init", "."])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m" "init"])
        subprocess.run(["ln", "-s", "pre-commit", ".git/hooks/pre-commit"])


    print("""
################################################################################
################################################################################
    You have succesfully created `{{ cookiecutter.lambda_name }}`.
################################################################################
    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}
################################################################################
    """)
