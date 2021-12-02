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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/ChainInformation/ethnet_listening.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethnet_listening")
class Test_ethnet_listening():

    @pytest.mark.parametrize("ethnet_listening", test_data)
    def test_ethnet_listening(self, ethnet_listening):
        url = ConfigYaml().get_conf_url() + ethnet_listening["url"]
        data = json.dumps(ethnet_listening["data"])
        # data = ethnet_listening["data"]
        headers = ethnet_listening["headers"]
        case_name = ethnet_listening["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethnet_listening["except"]["code"])
        assert_res.assert_in_body(res["body"], ethnet_listening["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethnet_listening.py"])
