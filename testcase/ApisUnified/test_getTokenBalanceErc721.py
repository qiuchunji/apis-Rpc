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
test_file = os.path.join(Conf.get_data_path(), "./ApisUnified/tokenBalanceErc721.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("tokenBalanceErc721")
class Test_tokenBalanceErc721():

    @pytest.mark.parametrize("tokenBalanceErc721", test_data)
    def test_tokenBalanceErc721(self, tokenBalanceErc721):
        url = ConfigYaml().get_conf_url() + tokenBalanceErc721["url"]
        # data = json.dumps(createWallet["data"])
        data = tokenBalanceErc721["data"]
        headers = tokenBalanceErc721["headers"]
        case_name = tokenBalanceErc721["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.get(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], tokenBalanceErc721["except"]["code"])
        assert_res.assert_in_body(res["body"], tokenBalanceErc721["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_getTokenBalanceErc721.py"])
