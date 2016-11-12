
import sys
import os

def check_version():
    vi = sys.version_info.major
    if vi == 2:
        print("===Python 2===")
    else:
        print("Running under Py3")


def get_user_name():
    profile = os.getlogin()
    print("User name: " + profile)


def get_script_path():
    script_path = os.path.abspath(sys.argv[0])
    print("Script path: " + script_path)
    return script_path


def get_script_dir():
    script_path = get_script_path()
    dir_path = os.path.dirname(script_path)
    print(dir_path)


def get_os():
    os_name = os.name
    print("Operating system: " + os_name)


def get_cores():
    cores = os.cpu_count()
    print("Number of cores: " + str(cores))


def get_variables():
    variables = os.environ["PATH"]
    print("Folders in PATH system variable:")
    for variable in variables.split(sep=os.pathsep):
        print(variable)


if __name__ == "__main__":
    check_version()
    get_user_name()
    get_script_path()
    get_script_dir()
    get_os()
    get_cores()
    get_variables()
