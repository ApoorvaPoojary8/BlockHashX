from flask import request, jsonify
from app.services.blockchain_service import Blockchain
from app.services.hashing_service import sha256_hash

# Singleton blockchain instance
blockchain = Blockchain()


def create_block():
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "Data is required"}), 400

    block = blockchain.add_block(data)

    return jsonify({
        "message": "Block created",
        "block": block.to_dict()
    })


def get_chain():
    return jsonify(blockchain.get_chain())


def validate_chain():
    return jsonify({
        "valid": blockchain.is_chain_valid()
    })


def hash_data():
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "Data is required"}), 400

    return jsonify({
        "hash": sha256_hash(data)
    })