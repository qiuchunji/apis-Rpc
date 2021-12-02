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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/ChainInformation/ethnet_version.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethnet_version")
class Test_ethnet_version():

    @pytest.mark.parametrize("ethnet_version", test_data)
    def test_ethnet_version(self, ethnet_version):
        url = ConfigYaml().get_conf_url() + ethnet_version["url"]
        data = json.dumps(ethnet_version["data"])
        # data = ethnet_version["data"]
        headers = ethnet_version["headers"]
        case_name = ethnet_version["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethnet_version["except"]["code"])
        assert_res.assert_in_body(res["body"], ethnet_version["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethnet_version.py"])
