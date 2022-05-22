#!/usr/bin/python3
""" script that generates a .tgz archive
from the contents of the web_static """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ Generate .tgz file """
    try:
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        tgz_file_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        result = local("tar -cvzf {} web_static".format(tgz_file_name))
        return(result)
    except Exception:
        return(None)
