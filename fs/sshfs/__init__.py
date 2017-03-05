from __future__ import absolute_import
from __future__ import unicode_literals

from .sshfs import SSHFS
from ..opener import Opener, registry

__author__ = "Martin Larralde"
__author_email__ = "martin.larralde@ens-cachan.fr"
__version__ = "0.1.0"
__license__ = "LGPLv2.1"


@registry.install
class SSHOpener(Opener):
    protocols = ['ssh']

    @staticmethod
    def open_fs(fs_url, parse_result, writeable, create, cwd):
        #from .sshfs import SSHFS
        ssh_host, _, dir_path = parse_result.resource.partition('/')
        ssh_host, _, ftp_port = ssh_host.partition(':')
        ssh_port = int(ftp_port) if ftp_port.isdigit() else 22
        ssh_fs = SSHFS(
            ssh_host,
            port=ssh_port,
            user=parse_result.username,
            passwd=parse_result.password,
        )
        return ssh_fs.opendir(dir_path) if dir_path else ssh_fs
