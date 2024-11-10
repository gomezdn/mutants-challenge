from flask import Flask, request, jsonify
from utils.mutant import is_mutant
from repository.mutant import get_stats, upsert_dna, get_dna


api = Flask(__name__)

@api.post("/mutant")
def handle_mutant_post():
    dna = request.json["dna"]
    is_human = not is_mutant(dna)

    upsert_dna(dna, is_human)

    if (is_human):
        return jsonify(False), 403
    else:
        return jsonify(True), 200

@api.get("/stats")
def handle_stats_get():
    stats = get_stats()
  
    return jsonify(stats), 200