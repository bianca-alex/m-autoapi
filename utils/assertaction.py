# -*- coding: utf-8 -*-
class Assert:

    # 断言code
    def assert_status_code(self, response, expected_status_code):
        assert response['code'] == expected_status_code, f"Expected status code {expected_status_code}, but got {response['code']}"

    # 断言请求时间
    def assert_response_time(self, response, max_response_time_ms):
        response_time_ms = response['time']
        assert response_time_ms <= max_response_time_ms, f"Response time exceeded {max_response_time_ms} ms, took {response_time_ms} ms"
    
    # 断言json
    def assert_json(self, response, expected_data):
        response_data = json.loads(response['body'])
        assert response_data == expected_data, f"Expected JSON data {expected_data}, but got {response_data}"
    
    def assert_header(self, response, header_name, expected_value):
        header_value = response['headers'].get(header_name)
        assert header_value == expected_value, f"Expected {header_name} header to be {expected_value}, but got {header_value}"
    
    def assert_contains(self, response, expected_text):
        response_text = response['body']
        assert expected_text in response_text, f"Expected text '{expected_text}' not found in response"


assert_tool = Assert()

if __name__ == "__main__":
    # 使用示例
    assert_tool = Assert()
    assert_tool.assert_status_code(response, 200)
