import string
from mypackage.lib import try_me

def test_type():
    assert type(try_me()) == str
