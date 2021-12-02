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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/RetrievingUncles/bscgetUncleCountByBlockNumber.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscgetUncleCountByBlockNumber")
class Test_bscgetUncleCountByBlockNumber():

    @pytest.mark.parametrize("bscgetUncleCountByBlockNumber", test_data)
    def test_bscgetUncleCountByBlockNumber(self, bscgetUncleCountByBlockNumber):
        url = ConfigYaml().get_conf_url() + bscgetUncleCountByBlockNumber["url"]
        data = json.dumps(bscgetUncleCountByBlockNumber["data"])
        # data = bscgetUncleCountByBlockNumber["data"]
        headers = bscgetUncleCountByBlockNumber["headers"]
        case_name = bscgetUncleCountByBlockNumber["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscgetUncleCountByBlockNumber["except"]["code"])
        assert_res.assert_in_body(res["body"], bscgetUncleCountByBlockNumber["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscgetUncleCountByBlockNumber.py"])
