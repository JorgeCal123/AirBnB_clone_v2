#!/usr/bin/python3
"""Fabric script hat distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import put, run, env
import os

env.hosts["54.226.20.179", "3.89.59.76"]
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")

        return True
    except:
        return False
