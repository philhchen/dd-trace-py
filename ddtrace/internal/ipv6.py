import socket
from typing import TypeVar
from typing import Union


T = TypeVar("T")


# Returns true if address is an IPv6 address
def is_ipv6_hostname(hostname):
    # type: (Union[T, str]) -> bool
    if not isinstance(hostname, str):
        return False
    try:
        socket.inet_pton(socket.AF_INET6, hostname)
        return True
    except socket.error:  # not a valid address
        return False
