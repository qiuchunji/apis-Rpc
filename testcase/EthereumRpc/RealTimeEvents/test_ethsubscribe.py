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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/RealTimeEvents/ethsubscribe.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethsubscribe")
class Test_ethsubscribe():

    @pytest.mark.parametrize("ethsubscribe", test_data)
    def test_ethsubscribe(self, ethsubscribe):
        url = ConfigYaml().get_conf_url() + ethsubscribe["url"]
        data = json.dumps(ethsubscribe["data"])
        # data = ethsubscribe["data"]
        headers = ethsubscribe["headers"]
        case_name = ethsubscribe["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethsubscribe["except"]["code"])
        assert_res.assert_in_body(res["body"], ethsubscribe["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethsubscribe.py"])
