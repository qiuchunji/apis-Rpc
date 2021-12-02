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
test_file = os.path.join(Conf.get_data_path(), "./BinanceSmartChainRPC/WritingTransactions/bscsendRawTransaction.yml")
# 使用工具类来读取多个文档内容
test_data = YamlReader(test_file).data_all()
print(test_data)


@pytest.mark.skip
@allure.feature("bscsendRawTransaction")
class Test_bscsendRawTransaction():

    @pytest.mark.parametrize("bscsendRawTransaction", test_data)
    def test_bscsendRawTransaction(self, bscsendRawTransaction):
        url = ConfigYaml().get_conf_url() + bscsendRawTransaction["url"]
        data = json.dumps(bscsendRawTransaction["data"])
        # data = bscsendRawTransaction["data"]
        headers = bscsendRawTransaction["headers"]
        case_name = bscsendRawTransaction["case_name"]
        allure.dynamic.title(case_name)
        request = Request()
        res = request.post(url=url, params=data, headers=headers)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], bscsendRawTransaction["except"]["code"])
        assert_res.assert_in_body(res["body"], bscsendRawTransaction["except"]["errDsc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_bscsendRawTransaction.py"])
