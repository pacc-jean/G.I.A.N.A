from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "🟢 G.I.A.N.A is online and operational."})
