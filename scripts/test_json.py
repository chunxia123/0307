from base.read_json import read_json
from base.base_driver import initdriver
from page.page import Page
import pytest

class TestJson:
    @pytest.mark.parametrize("args", read_json())
    def test_json(self,args):
        print(args)






