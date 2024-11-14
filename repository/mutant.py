from xxhash import xxh64
from db.db import dna_table

def get_stats():
  mutants = dna_table.select(count="exact").eq("is_mutant", "true").execute().count
  humans = dna_table.select(count="exact").eq("is_mutant", "false").execute().count
  ratio = max(mutants, 1) / max(humans, 1)

  return {
    "count_mutant_dna": mutants,
    "count_human_dna": humans,
    "ratio": round(ratio, 2)
  }

def upsert_dna(dna, mutant):
  dna_string = "".join(dna)
  hashed = xxh64(dna_string).hexdigest()

  response = dna_table.upsert(
    {
    "dna_hash": hashed,
    "dna": dna,
    "is_mutant": mutant
    }).execute()

  return response
