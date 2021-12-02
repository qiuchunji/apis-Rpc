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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/RetrievingBlocks/bscGetBlockByHash.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscGetBlockByHash")
class Test_bscGetBlockByHash():

    @pytest.mark.parametrize("bscGetBlockByHash", test_data)
    def test_bscGetBlockByHash(self, bscGetBlockByHash):
        url = ConfigYaml().get_conf_url() + bscGetBlockByHash["url"]
        data = json.dumps(bscGetBlockByHash["data"])
        # data = bscGetBlockByHash["data"]
        headers = bscGetBlockByHash["headers"]
        case_name = bscGetBlockByHash["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscGetBlockByHash["except"]["code"])
        assert_res.assert_in_body(res["body"], bscGetBlockByHash["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscGetBlockByHash.py"])
