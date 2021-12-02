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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/ChainInformation/ethestimateGas.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethestimateGas")
class Test_ethestimateGas():

    @pytest.mark.parametrize("ethestimateGas", test_data)
    def test_ethestimateGas(self, ethestimateGas):
        url = ConfigYaml().get_conf_url() + ethestimateGas["url"]
        data = json.dumps(ethestimateGas["data"])
        # data = ethestimateGas["data"]
        headers = ethestimateGas["headers"]
        case_name = ethestimateGas["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethestimateGas["except"]["code"])
        assert_res.assert_in_body(res["body"], ethestimateGas["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethestimateGas.py"])
