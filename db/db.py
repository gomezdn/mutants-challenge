from supabase import create_client
from dotenv import load_dotenv
from os import getenv

load_dotenv()

URL = getenv("SUPABASE_URL")
API_KEY = getenv("SUPABASE_API_KEY")

db = create_client(URL, API_KEY)
dna_table = db.table("dna")
