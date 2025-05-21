from flask import Blueprint, jsonify

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/analyze/<symbol>', methods=['GET'])
def analyze_symbol(symbol):
    return jsonify({"message": f"Analysis for {symbol} works"})

