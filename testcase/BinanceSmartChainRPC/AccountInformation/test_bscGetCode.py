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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/AccountInformation/bscGetCode.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscGetCode")
class Test_bscGetCode():

    @pytest.mark.parametrize("bscGetCode", test_data)
    def test_bscGetCode(self, bscGetCode):
        url = ConfigYaml().get_conf_url() + bscGetCode["url"]
        data = json.dumps(bscGetCode["data"])
        # data = bscGetCode["data"]
        headers = bscGetCode["headers"]
        case_name = bscGetCode["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscGetCode["except"]["code"])
        assert_res.assert_in_body(res["body"], bscGetCode["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscGetCode.py"])
