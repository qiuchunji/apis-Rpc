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
test_file = os.path.join(Conf.get_data_path(), "./ApisUnified/createWallet.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("Create_wallet")
class Test_createWallet():

    @pytest.mark.parametrize("createWallet", test_data)
    def test_createWallet(self, createWallet):
        url = ConfigYaml().get_conf_url() + createWallet["url"]
        data = json.dumps(createWallet["data"])
        # data = createWallet["data"]
        headers = createWallet["headers"]
        case_name = createWallet["case_name"]
        allure.dynamic.title(case_name)
        print(url)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], createWallet["except"]["code"])
        assert_res.assert_in_body(res["body"], createWallet["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-vs", "test_createWallet.py"])
