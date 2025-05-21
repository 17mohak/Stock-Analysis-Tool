from flask import Blueprint, jsonify

watchlist_bp = Blueprint('watchlist', __name__)

@watchlist_bp.route('/mywatchlists', methods=['GET'])
def get_watchlists():
    return jsonify({"message": "Watchlists route works"})
