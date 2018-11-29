import sys
sys.path.append('../uospy')

import uospy.cluos
import requests
from nose.tools import raises

class TestCluos :

    def setup(self) :
        self.ce = uospy.cluos.Cluos()#'https://api.pennstation.uosnewyork.io:7101'
        self.json_to_bin = {u'to': u'uosio', u'memo': u'test', u'from': u'uosio', u'quantity': u'1.0000 UOS'}

        # ss= self.test_json_to_bin()

        self.bin_to_json = '0000000000ea30d50000000000ea30d5102700000000000004554f53000000000474657374'#'0000000000ea30550000000000ea3055102700000000000004454f53000000000474657374'

    def test_get_info(self) :
        output = self.ce.get_info()
        # test output is valid
        assert "server_version" in output
        assert "chain_id" in output
        assert "head_block_num" in output
        assert "last_irreversible_block_num" in output
        assert "head_block_id" in output
        assert "head_block_producer" in output
        assert "virtual_block_cpu_limit" in output
        assert "virtual_block_net_limit" in output
        assert "block_cpu_limit" in output
        assert "block_net_limit" in output

    def test_get_block(self) :
        block = self.ce.get_block(1)
        assert block['block_num'] == 1

    @raises(requests.exceptions.HTTPError)
    def test_get_block_invalid(self) :
        block = self.ce.get_block(-1)
        return block
        
    def test_get_account(self) :
        acct = self.ce.get_account('qupengcheng3')
        assert acct['account_name'] == 'uosio'

    @raises(requests.exceptions.HTTPError)
    def test_get_account_invalid(self) :
        acct = self.ce.get_account('uoserd')
        return acct

    def test_get_abi(self) :
        abi = self.ce.get_abi('uosio')
        return abi

    def test_get_code(self) :
        code = self.ce.get_code('uosio')
        return code

    def test_get_code_bad(self) :
        code = self.ce.get_code('uosio.ram')
        assert code['code_hash'] == u'0000000000000000000000000000000000000000000000000000000000000000'

    def test_get_table(self):
        # table = self.ce.get_table('uosio','uosio', 'producers', lower_bound='uosnewyorkio')
        table = self.ce.get_table('ulorduosudfs', 'qupengcheng3', 'udfsuserac', lower_bound='uosnewyorkio')

        table = self.ce.get_table('ulorduosudfs', 'qupengcheng3', 'udfsuserrd', lower_bound='uosnewyorkio')
        return table

    @raises(requests.exceptions.HTTPError)
    def test_get_table_bad(self):
        table = self.ce.get_table('uosio', 'uosio', 'producer')
        return table

    def test_get_currency_balance(self) :
        bal = self.ce.get_currency_balance('qupengcheng3', 'uosio.token', 'SYS')
        return bal

    @raises(requests.exceptions.HTTPError)
    def test_get_currency_balance_fail(self) :
        bal = self.ce.get_currency_balance('uosio', 'uosio', 'SYS')
        return bal

    def test_json_to_bin(self) :
        bin = self.ce.abi_json_to_bin('uosio.token', 'transfer', self.json_to_bin)
        assert bin['binargs'] == self.bin_to_json

    def test_json_to_bin_bad(self) :
        bin = self.ce.abi_json_to_bin('uosio.token', 'transfer', '')
        assert bin['binargs'] == ''

    def test_bin_to_json(self) :
        bin = self.ce.abi_bin_to_json('uosio.token', 'transfer', self.bin_to_json)
        assert bin['args'] == self.json_to_bin

    @raises(requests.exceptions.HTTPError)
    def test_bin_to_json_fail(self) :
        bin = self.ce.abi_bin_to_json('uosio.token', 'transfer', '00')
        return b

    def test_get_currency_stats(self) :
        return self.ce.get_currency_stats('uosio.token', 'UOS')

    def test_get_currency_stats_bad(self) :
        stats = self.ce.get_currency_stats('uosio.token', 'SYS')
        assert stats == {}

    def test_get_producers(self) :
        return self.ce.get_producers()

    
if __name__ == '__main__':
    t = TestCluos()
    t.setup()
    n = t.test_get_table()
    j =t.test_get_currency_balance()
    c = t.test_get_account()

    a = t.test_bin_to_json()
    b= t.test_get_account_invalid()

    d = t.test_bin_to_json_fail()
    e = t.test_get_abi()
    f = t.test_get_block()
    g = t.test_get_block_invalid()
    h = t.test_get_code()

    i = t.test_get_code_bad()

    k = t.test_get_currency_balance_fail()
    l = t.test_get_info()
    m = t.test_get_producers()

    o = t.test_get_table_bad()
    p = t.test_json_to_bin()
    # r = t.test_json_to_bin_bad()
