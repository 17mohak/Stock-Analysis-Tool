import pandas as pd
from nselib import price_volume_and_deliverable_position_data

class StockAnalysisService:
    def get_technical_indicators(self, symbol, period='6M'):
        data = price_volume_and_deliverable_position_data(symbol, period=period)
        data['MA50'] = data['Close'].rolling(window=50).mean()
        data['MA200'] = data['Close'].rolling(window=200).mean()
        data['RSI'] = self.calculate_rsi(data['Close'])
        return data.tail(30).to_dict(orient='records')

    # Add other methods from the original service class