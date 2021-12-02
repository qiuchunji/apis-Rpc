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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/ChainInformation/bscchainId.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscchainId")
class Test_bscchainId():

    @pytest.mark.parametrize("bscchainId", test_data)
    def test_bscchainId(self, bscchainId):
        url = ConfigYaml().get_conf_url() + bscchainId["url"]
        data = json.dumps(bscchainId["data"])
        # data = bscchainId["data"]
        headers = bscchainId["headers"]
        case_name = bscchainId["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscchainId["except"]["code"])
        assert_res.assert_in_body(res["body"], bscchainId["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscchainId.py"])
