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
test_file = os.path.join(Conf.get_data_path(), "./ApisUnified/tokenBalanceErc20.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("tokenBalanceErc20")
class Test_tokenBalanceErc20():

    @pytest.mark.parametrize("tokenBalanceErc20", test_data)
    def test_tokenBalanceErc20(self, tokenBalanceErc20):
        url = ConfigYaml().get_conf_url() + tokenBalanceErc20["url"]
        # data = json.dumps(createWallet["data"])
        data = tokenBalanceErc20["data"]
        headers = tokenBalanceErc20["headers"]
        case_name = tokenBalanceErc20["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.get(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], tokenBalanceErc20["except"]["code"])
        assert_res.assert_in_body(res["body"], tokenBalanceErc20["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_getTokenBalanceErc20.py"])
