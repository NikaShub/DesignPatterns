import json


class ThirdPartyJsonAnalytics:
    def process_json(self, json_data: str) -> None:
        parsed = json.loads(json_data)
        print(f"Processing JSON data: {parsed}")