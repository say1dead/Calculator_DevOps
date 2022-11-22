import os
import sys
import shutil
import subprocess


def cmd_launch(cmd):
    """A clean way to launch commands."""
    rc = subprocess.run(cmd, shell=True).returncode
    if rc != 0:
        print(f"Failed to launch command: {cmd}")
        sys.exit(1)


# launch the builds
dir_src = ["main.py"]
dir_test = "test"
dir_build = "build"
shutil.rmtree(dir_build, ignore_errors=True)
# build each .py script into .exe binary
for i in dir_src:
    # generate .spec file in an isolated Docker container
    cmd_launch('docker run --rm -v $(pwd):/src/ -w /src python:slim /bin/bash -c "'
               'python3 -m pip install pyinstaller==3.6 && '
               'rm -rf {0} && '
               'mkdir {0} && '
               'chmod -R 777 {0} && '
               'cp {1} {0}/{1} && '
               'cd {0} && '
               'pyi-makespec --noupx --onefile {1}"'
               .format(dir_test, i))
    os.chdir(dir_test)
    # build an .exe file and place it into "build" directory
    cmd_launch(f'docker run --rm -v $(pwd):/src/ cdrx/pyinstaller-windows')
    binary = i.replace('.py', '.exe', 1)
    os.chdir("..")
    if not os.path.isdir(dir_build):
        os.mkdir(dir_build)
    shutil.copy(os.path.join(dir_test,
                             "dist",
                             "windows",
                             binary),
                os.path.join(dir_build,
                             binary))
# clean environment
cmd_launch(f'docker run --rm -v $(pwd):/src/ -w /src python:slim /bin/bash -c "rm -rf {dir_test}"')
docker_images = ["python:slim", "cdrx/pyinstaller-windows"]
# remove Docker images
for img in docker_images:
    cmd_launch(f"docker rmi {img}")