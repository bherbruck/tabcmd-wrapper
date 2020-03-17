import pytest

from tabcmd import Session


# TODO: write some tests

def test_Session():
    sess = Session()
    assert sess.tabcmd_path == 'tabcmd'
    assert sess.certcheck == False
    assert sess.is_logged_in == False