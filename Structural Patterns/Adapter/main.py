from third_party_analytics import ThirdPartyJsonAnalytics
from xml_to_json_adapter import XmlToJsonAdapter
from stock_analytics import StockAnalytics


def run_app(analytics: StockAnalytics, xml_payload: str) -> None:
    analytics.analyze_stock_data(xml_payload)


if __name__ == "__main__":
    xml_from_market = "<stock><symbol>AAPL</symbol><price>225.50</price></stock>"
    external_library = ThirdPartyJsonAnalytics()
    adapter = XmlToJsonAdapter(external_library)
    run_app(adapter, xml_from_market)