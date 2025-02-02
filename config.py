# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21065691")

API_HASH = os.environ.get("API_HASH", "54e7c2bef4f5eb1815d07ce348327810")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "mongodb+srv://nexgengaming19:zXggN4MFRotLo5dA@cluster0.teahm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Crunchyroll_India_Official") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://nexgengaming19:zXggN4MFRotLo5dA@cluster0.teahm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6393499976').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
