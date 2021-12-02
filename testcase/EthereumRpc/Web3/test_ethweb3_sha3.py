from config import Conf
import os
import json
from utils.yamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
import allure

# 获取测试用例内容list
# 获取testlogin.yml文件路径
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/Web3/ethweb3_sha3.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethweb3_sha3")
class Test_ethweb3_sha3():

    @pytest.mark.parametrize("ethweb3_sha3", test_data)
    def test_ethweb3_sha3(self, ethweb3_sha3):
        url = ConfigYaml().get_conf_url() + ethweb3_sha3["url"]
        data = json.dumps(ethweb3_sha3["data"])
        # data = ethweb3_sha3["data"]
        headers = ethweb3_sha3["headers"]
        case_name = ethweb3_sha3["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethweb3_sha3["except"]["code"])
        assert_res.assert_in_body(res["body"], ethweb3_sha3["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethweb3_sha3.py"])
