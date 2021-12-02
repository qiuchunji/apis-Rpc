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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/RealTimeEvents/bscsyncing.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("bscsyncing")
class Test_bscsyncing():

    @pytest.mark.parametrize("bscsyncing", test_data)
    def test_bscsyncing(self, bscsyncing):
        url = ConfigYaml().get_conf_url() + bscsyncing["url"]
        data = json.dumps(bscsyncing["data"])
        # data = bscsyncing["data"]
        headers = bscsyncing["headers"]
        case_name = bscsyncing["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscsyncing["except"]["code"])
        assert_res.assert_in_body(res["body"], bscsyncing["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscsyncing.py"])
