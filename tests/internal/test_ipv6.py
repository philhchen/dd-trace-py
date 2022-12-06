import pytest

from ddtrace.internal.ipv6 import is_ipv6_hostname


@pytest.mark.parametrize(
    "hostname,expected",
    [
        (None, False),
        ("10.0.0.1", False),
        ("192.168.1.1", False),
        ("https://www.datadog.com", False),
        ("2001:db8:3333:4444:5555:6666:7777:8888", True),
        ("2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF", True),
        ("[2001:db8:3333:4444:5555:6666:7777:8888]", False),
        ("::", True),
    ],
)
def test_is_ipv6_hostname(hostname, expected):
    assert is_ipv6_hostname(hostname) == expected
