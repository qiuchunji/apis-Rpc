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
test_file = os.path.join(Conf.get_data_path(), "./ApisUnified/getDefiRates.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("getDefiRates")
class Test_getDefiRates():

    @pytest.mark.parametrize("getDefiRates", test_data)
    def test_getDefiRates(self, getDefiRates):
        url = ConfigYaml().get_conf_url() + getDefiRates["url"]
        # data = json.dumps(createWallet["data"])
        data = getDefiRates["data"]
        # headers = createWallet["headers"]
        case_name = getDefiRates["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.get(url=url, params=data)
        print(url)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], getDefiRates["except"]["code"])
        assert_res.assert_in_body(res["body"], getDefiRates["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_getDefiRates.py"])
