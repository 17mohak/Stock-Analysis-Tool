from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.analysis import StockAnalysisService

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/api/stock/<symbol>/analysis', methods=['GET'])
@jwt_required()
def get_stock_analysis(symbol):
    service = StockAnalysisService()
    try:
        return jsonify({
            'historical_data': service.get_technical_indicators(symbol),
            'recommendation': service.generate_recommendation(symbol)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400