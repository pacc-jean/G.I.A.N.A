from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from app.models import Session, Message

main_bp = Blueprint("main", __name__)

@main_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "🟢 G.I.A.N.A is online and operational."})


@main_bp.route("/session", methods=["POST"])
def create_or_resume_session():
    from app.core.extensions import db

    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Missing 'username' in request."}), 400

    username = data["username"].strip().lower()
    session = Session.query.filter_by(username=username).first()

    if session:
        return jsonify({
            "session_id": session.id,
            "username": session.username,
            "created_at": session.created_at.isoformat(),
            "message": "🔁 Session resumed."
        })

    new_session = Session(username=username)
    db.session.add(new_session)
    db.session.commit()

    return jsonify({
        "session_id": new_session.id,
        "username": new_session.username,
        "created_at": new_session.created_at.isoformat(),
        "message": "🆕 New session created."
    })


@main_bp.route("/message", methods=["POST", "GET"])
def handle_messages():
    from app.core.extensions import db

    if request.method == "POST":
        data = request.get_json()

        if not data or "session_id" not in data or "role" not in data or "content" not in data:
            return jsonify({"error": "Missing required fields: session_id, role, content"}), 400

        session = Session.query.get(data["session_id"])
        if not session:
            return jsonify({"error": "Session not found."}), 404

        message = Message(
            session_id=session.id,
            role=data["role"].strip().lower(),
            content=data["content"].strip()
        )
        db.session.add(message)
        db.session.commit()

        return jsonify({
            "message_id": message.id,
            "session_id": message.session_id,
            "role": message.role,
            "content": message.content,
            "timestamp": message.timestamp.isoformat(),
            "status": "✅ Message stored."
        }), 201

    # GET: Fetch all messages for a session
    session_id = request.args.get("session_id")
    if not session_id:
        return jsonify({"error": "Missing session_id in query params."}), 400

    messages = Message.query.filter_by(session_id=session_id).order_by(Message.timestamp.asc()).all()

    return jsonify([
        {
            "message_id": m.id,
            "role": m.role,
            "content": m.content,
            "timestamp": m.timestamp.isoformat()
        }
        for m in messages
    ])
