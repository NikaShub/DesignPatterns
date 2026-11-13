import json
import xml.etree.ElementTree as ET
from stock_analytics import StockAnalytics
from third_party_analytics import ThirdPartyJsonAnalytics


class XmlToJsonAdapter(StockAnalytics):
    def __init__(self, json_analytics: ThirdPartyJsonAnalytics) -> None:
        self._json_analytics = json_analytics

    def analyze_stock_data(self, xml_data: str) -> None:
        converted_json = self._convert_xml_to_json(xml_data)
        self._json_analytics.process_json(converted_json)

    def _convert_xml_to_json(self, xml_data: str) -> str:
        root = ET.fromstring(xml_data)
        data = {child.tag: child.text for child in root}
        if not data and root.text:
            data = {root.tag: root.text}
        return json.dumps(data)