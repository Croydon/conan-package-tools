
__version__ = '0.34.4'


def get_client_version():
    from conans.model.version import Version
    from conans import __version__ as client_version
    from os import getenv
    # It is a mess comparing dev versions, lets assume that the -dev is the further release
    return Version(client_version.replace("-dev", ""))
