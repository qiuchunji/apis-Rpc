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
test_file = os.path.join(Conf.get_data_path(), "./ApisUnified/createTokenErc20.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("createTokenErc20")
class Test_createTokenErc20():

    @pytest.mark.parametrize("createTokenErc20", test_data)
    def test_createTokenErc20(self, createTokenErc20):
        url = ConfigYaml().get_conf_url() + createTokenErc20["url"]
        data = json.dumps(createTokenErc20["data"])
        headers = createTokenErc20["headers"]
        case_name = createTokenErc20["case_name"]
        allure.dynamic.title(case_name)
        print(url)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], createTokenErc20["except"]["code"])
        assert_res.assert_in_body(res["body"], createTokenErc20["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-vs", "test_createTokenErc20.py"])
