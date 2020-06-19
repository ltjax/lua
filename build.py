import platform
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    command = None
    if platform.system() == "Linux":
        command = "sudo apt-get update -q && sudo apt-get install -y -q libreadline-dev libncurses5-dev"
    builder = ConanMultiPackager(docker_entry_script=command)
    builder.add_common_builds(shared_option_name="lua:shared")
    builder.run()
