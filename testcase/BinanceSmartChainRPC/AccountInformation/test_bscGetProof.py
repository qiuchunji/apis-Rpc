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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/AccountInformation/bscGetProof.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscGetProof")
class Test_bscGetProof():

    @pytest.mark.parametrize("bscGetProof", test_data)
    def test_bscGetProof(self, bscGetProof):
        url = ConfigYaml().get_conf_url() + bscGetProof["url"]
        data = json.dumps(bscGetProof["data"])
        # data = bscGetProof["data"]
        headers = bscGetProof["headers"]
        case_name = bscGetProof["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscGetProof["except"]["code"])
        assert_res.assert_in_body(res["body"], bscGetProof["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscGetProof.py"])
