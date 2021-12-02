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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/Web3/bscsha3.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscsha3")
class Test_bscsha3():

    @pytest.mark.parametrize("bscsha3", test_data)
    def test_bscsha3(self, bscsha3):
        url = ConfigYaml().get_conf_url() + bscsha3["url"]
        data = json.dumps(bscsha3["data"])
        # data = bscsha3["data"]
        headers = bscsha3["headers"]
        case_name = bscsha3["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscsha3["except"]["code"])
        assert_res.assert_in_body(res["body"], bscsha3["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscsha3.py"])
