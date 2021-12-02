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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/ReadingTransactions/ethGetTransactionByBlockHashAndIndex.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethGetTransactionByBlockHashAndIndex")
class Test_ethGetTransactionByBlockHashAndIndex():

    @pytest.mark.parametrize("ethGetTransactionByBlockHashAndIndex", test_data)
    def test_ethGetTransactionByBlockHashAndIndex(self, ethGetTransactionByBlockHashAndIndex):
        url = ConfigYaml().get_conf_url() + ethGetTransactionByBlockHashAndIndex["url"]
        data = json.dumps(ethGetTransactionByBlockHashAndIndex["data"])
        # data = ethGetTransactionByBlockHashAndIndex["data"]
        headers = ethGetTransactionByBlockHashAndIndex["headers"]
        case_name = ethGetTransactionByBlockHashAndIndex["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethGetTransactionByBlockHashAndIndex["except"]["code"])
        assert_res.assert_in_body(res["body"], ethGetTransactionByBlockHashAndIndex["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethGetTransactionByBlockHashAndIndex.py"])
