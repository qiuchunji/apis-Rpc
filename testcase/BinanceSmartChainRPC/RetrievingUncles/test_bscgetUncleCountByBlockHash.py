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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/RetrievingUncles/bscgetUncleCountByBlockHash.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscgetUncleCountByBlockHash")
class Test_bscgetUncleCountByBlockHash():

    @pytest.mark.parametrize("bscgetUncleCountByBlockHash", test_data)
    def test_bscgetUncleCountByBlockHash(self, bscgetUncleCountByBlockHash):
        url = ConfigYaml().get_conf_url() + bscgetUncleCountByBlockHash["url"]
        data = json.dumps(bscgetUncleCountByBlockHash["data"])
        # data = bscgetUncleCountByBlockHash["data"]
        headers = bscgetUncleCountByBlockHash["headers"]
        case_name = bscgetUncleCountByBlockHash["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscgetUncleCountByBlockHash["except"]["code"])
        assert_res.assert_in_body(res["body"], bscgetUncleCountByBlockHash["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscgetUncleCountByBlockHash.py"])
