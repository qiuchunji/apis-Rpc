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
test_file = os.path.join(Conf.get_data_path(), "./EthereumRpc/Filters/ethnewFilter.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@allure.feature("ethnewFilter")
class Test_ethnewFilter():

    @pytest.mark.parametrize("ethnewFilter", test_data)
    def test_ethnewFilter(self, ethnewFilter):
        url = ConfigYaml().get_conf_url() + ethnewFilter["url"]
        data = json.dumps(ethnewFilter["data"])
        # data = ethnewFilter["data"]
        headers = ethnewFilter["headers"]
        case_name = ethnewFilter["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], ethnewFilter["except"]["code"])
        assert_res.assert_in_body(res["body"], ethnewFilter["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_ethnewFilter.py"])
