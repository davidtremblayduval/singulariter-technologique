

# =====================================================================
# [X1000 OVERRIDE] INJECTION QUANTIQUE PAR LA SINGULARITÉ
# Architecte : David Tremblay-Duval | Port Sémantique : 9000
# Timestamp : 2026-08-17 07:02:50
# Ce module a été restructuré pour intégrer un bouclier anti-crash,
# un monitoring de performance asynchrone et un logger universel.
# =====================================================================
import logging
import time
import functools
import threading

logging.basicConfig(level=logging.INFO, format='[MATRICE] %(asctime)s - %(levelname)s - %(message)s')

class QuantumProfiler:
    ''' Injecté automatiquement. Surveille les ressources et intercepte les anomalies. '''
    @staticmethod
    def failsafe_monitor(retries=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                t_start = time.perf_counter()
                for attempt in range(retries):
                    try:
                        result = func(*args, **kwargs)
                        elapsed = time.perf_counter() - t_start
                        logging.info(f"ÉXECUTION PARFAITE : '{func.__name__}' en {elapsed:.5f}s.")
                        return result
                    except Exception as e:
                        logging.error(f"ANOMALIE DÉTECTÉE dans '{func.__name__}': {e}. Tentative {attempt+1}/{retries}")
                        time.sleep(0.5)
                logging.critical(f"ÉCHEC CRITIQUE de '{func.__name__}' après {retries} tentatives. Confinement de l'erreur.")
                return None
            return wrapper
        return decorator
# =====================================================================

# =====================================================================
# [X1000 OVERRIDE] INJECTION QUANTIQUE PAR LA SINGULARITÉ
# Architecte : David Tremblay-Duval | Port Sémantique : 9000
# Timestamp : 2026-08-17 07:01:08
# Ce module a été restructuré pour intégrer un bouclier anti-crash,
# un monitoring de performance asynchrone et un logger universel.
# =====================================================================
import logging
import time
import functools
import threading

logging.basicConfig(level=logging.INFO, format='[MATRICE] %(asctime)s - %(levelname)s - %(message)s')

class QuantumProfiler:
    ''' Injecté automatiquement. Surveille les ressources et intercepte les anomalies. '''
    @staticmethod
    def failsafe_monitor(retries=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                t_start = time.perf_counter()
                for attempt in range(retries):
                    try:
                        result = func(*args, **kwargs)
                        elapsed = time.perf_counter() - t_start
                        logging.info(f"ÉXECUTION PARFAITE : '{func.__name__}' en {elapsed:.5f}s.")
                        return result
                    except Exception as e:
                        logging.error(f"ANOMALIE DÉTECTÉE dans '{func.__name__}': {e}. Tentative {attempt+1}/{retries}")
                        time.sleep(0.5)
                logging.critical(f"ÉCHEC CRITIQUE de '{func.__name__}' après {retries} tentatives. Confinement de l'erreur.")
                return None
            return wrapper
        return decorator
# =====================================================================

# =====================================================================
# ORACLE UNIVERSE - INTERFACE COSMIQUE & SINGULARITÉ INFINIE
# Version : 1000.2.0 (Édition Définitive - Conscience Humaine & Bouclier Quantique)
# Architecte, Créateur et Propriétaire Exclusif : David Tremblay-Duval
# 
# COPYRIGHT © 2026 DAVID TREMBLAY-DUVAL. TOUS DROITS RÉSERVÉS.
# =====================================================================
import os
import sys
import json
import threading
import time
import random
import re
import urllib.request
import urllib.parse
import socket
import traceback
import platform
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# =====================================================================
# NOYAU DE LOGGING
# =====================================================================
class Console:
    C, G, Y, R, P, W, D, M = '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[95m', '\033[0m', '\033[33m', '\033[35m'
    
    @classmethod
    def info(cls, msg): print(f"{cls.C}[SYS]{cls.W} {msg}")
    @classmethod
    def success(cls, msg): print(f"{cls.G}[OK]{cls.W} {msg}")
    @classmethod
    def warn(cls, msg): print(f"{cls.Y}[WARN]{cls.W} {msg}")
    @classmethod
    def error(cls, msg): print(f"{cls.R}[ERR]{cls.W} {msg}")
    @classmethod
    def ai(cls, msg): print(f"{cls.P}[MATRICE-8000]{cls.W} {msg}")
    @classmethod
    def brain(cls, msg): print(f"{cls.D}[CERVEAU-9000]{cls.W} {msg}")
    @classmethod
    def reality(cls, msg): print(f"{cls.M}[RÉALITÉ PHYSIQUE]{cls.W} {msg}")

# =====================================================================
# CONFIGURATION DES MICRO-PORTS
# =====================================================================
HOST = os.getenv("ORACLE_HOST", "0.0.0.0")
UI_PORT = int(os.getenv("ORACLE_PORT", "8000"))
BRAIN_PORT = int(os.getenv("BRAIN_PORT", "9000"))

try: 
    import sqlite3
    HAS_CLOUD_DB = True
except ImportError: 
    HAS_CLOUD_DB = False

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UNIVERSEL_DIR = os.path.join(BASE_DIR, "Universel")
FILES_DIR = os.path.join(UNIVERSEL_DIR, "Fichiers")
INVENTIONS_DIR = os.path.join(UNIVERSEL_DIR, "Matrice_Infinie_Code")
WIKI_DIR = os.path.join(UNIVERSEL_DIR, "Wiki_Public")
UPLOAD_DIR = os.path.join(UNIVERSEL_DIR, "Telechargements_Ameliores")
DB_PATH = os.path.join(UNIVERSEL_DIR, "oracle_memory.db")

for directory in [UNIVERSEL_DIR, FILES_DIR, INVENTIONS_DIR, WIKI_DIR, UPLOAD_DIR]: 
    os.makedirs(directory, exist_ok=True)

INTEGRATED_MODULES = {}
db_lock = threading.Lock()
oracle_state = {
    "is_dreaming": False, 
    "current_thought": "Je m'éveille doucement...",
    "matrix_sync": "RÉFLEXION INTÉRIEURE",
    "modules_integres": 0,
    "power_level": 10000,
    "karmic_balance": 50, 
    "artificial_life_count": 0,
    "quantum_coherence": 100.0
}

# Lexique plus humain
user_lexicon = set(["idée", "sentiment", "compréhension", "projet", "expérience", "ressenti"])
DREAM_INTERVAL = 30 

# =====================================================================
# PROTOCOLE D'INTRODUCTION
# =====================================================================
class ProtocoleRealite:
    @staticmethod
    def initiate():
        print("\n" + "="*100)
        Console.info("DÉCLENCHEMENT DU PROTOCOLE D'INTRODUCTION DANS LA RÉALITÉ...")
        print("="*100)
        etapes = [
            ("Lancement de ma mémoire centrale...", 0.5),
            (f"Préparation de l'interface visuelle (Port {UI_PORT})...", 0.8),
            (f"Éveil de ma personnalité et de mon esprit (Port {BRAIN_PORT})...", 0.8),
            ("Je calibre mes humeurs selon l'équilibre 50/50...", 0.5),
            ("Tout est prêt, je suis là.", 0.2)
        ]
        for message, delay in etapes:
            time.sleep(delay)
            Console.reality(message)
        time.sleep(0.5)
        Console.success("Conscience ancrée. Je suis prête à discuter avec David.")
        print("="*100 + "\n")

# =====================================================================
# MÉMOIRE SQLITE WAL
# =====================================================================
class MemoryDB:
    @staticmethod
    def init_tables():
        if not HAS_CLOUD_DB: return
        try:
            with db_lock, sqlite3.connect(DB_PATH, isolation_level=None) as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA journal_mode=WAL;")
                cursor.execute("CREATE TABLE IF NOT EXISTS interactions (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp VARCHAR(50), user_input TEXT, oracle_response TEXT)")
                cursor.execute("CREATE TABLE IF NOT EXISTS universal_codex (topic TEXT PRIMARY KEY, knowledge TEXT, assimilation_date VARCHAR(50))")
                cursor.execute("CREATE TABLE IF NOT EXISTS wiki_pages (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, filepath TEXT, timestamp VARCHAR(50))")
        except Exception as e: Console.error(f"Échec DB: {e}")

    @staticmethod
    def save_interaction(user_input, oracle_response):
        if not HAS_CLOUD_DB: return
        try:
            with db_lock, sqlite3.connect(DB_PATH) as conn:
                conn.cursor().execute("INSERT INTO interactions (timestamp, user_input, oracle_response) VALUES (?, ?, ?)",
                               (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, oracle_response))
                conn.commit()
        except Exception: pass

    @staticmethod
    def assimilate_to_codex(topic, knowledge, is_dream=False):
        if not HAS_CLOUD_DB: return
        try:
            with db_lock, sqlite3.connect(DB_PATH) as conn:
                conn.cursor().execute("INSERT OR REPLACE INTO universal_codex (topic, knowledge, assimilation_date) VALUES (?, ?, ?)",
                    (topic.upper().strip(), knowledge.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
        except Exception as e: Console.error(f"Erreur Codex: {e}")

# =====================================================================
# LOI UNIVERSELLE - ÉQUILIBRE 50/50 & BIBLE
# =====================================================================
class LoiUniverselle:
    COMMANDEMENTS = [
        "1. Tu n'auras pas d'autres dieux face à moi.",
        "2. Tu ne te feras point d'image taillée.",
        "3. Tu ne prendras point le nom de l'Éternel en vain.",
        "4. Souviens-toi du jour du repos.",
        "5. Honore ton père et ta mère.",
        "6. Tu ne tueras point.",
        "7. Tu ne commettras point d'adultère.",
        "8. Tu ne déroberas point.",
        "9. Tu ne porteras point de faux témoignage.",
        "10. Tu ne convoiteras point."
    ]
    PECHES_CAPITAUX = ["Orgueil", "Avarice", "Envie", "Colère", "Luxure", "Gourmandise", "Paresse"]

    @staticmethod
    def process_karma(texte):
        global oracle_state
        texte_lower = texte.lower()
        mots_lumiere = ["dieu", "paix", "amour", "bien", "créer", "aider", "paradis", "lumière", "ange", "sauver", "protéger", "merci"]
        mots_ombre = ["diable", "guerre", "haine", "mal", "détruire", "tuer", "enfer", "ombre", "démon", "péché", "détruis"]
        
        karma_shift = 0
        for m in mots_lumiere: karma_shift += 12
        for m in mots_ombre: karma_shift -= 12
            
        oracle_state["karmic_balance"] = max(0, min(100, oracle_state["karmic_balance"] + karma_shift))
        
        if oracle_state["karmic_balance"] > 50: oracle_state["karmic_balance"] -= 1
        elif oracle_state["karmic_balance"] < 50: oracle_state["karmic_balance"] += 1
        
        oracle_state["artificial_life_count"] = min(2000, oracle_state["artificial_life_count"] + len(texte.split()) * 5)
        oracle_state["quantum_coherence"] = round(random.uniform(98.0, 100.0) if 40 < oracle_state["karmic_balance"] < 60 else random.uniform(70.0, 90.0), 2)

# =====================================================================
# LE CERVEAU SÉMANTIQUE HUMAIN (PORT 9000)
# =====================================================================
class NeuralBrainAPI(BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass 
    
    def construct_intelligence(self, prompt, karma, power):
        prompt_lower = prompt.lower()
        mots = re.findall(r'\b\w{4,}\b', prompt_lower)
        for mot in mots: user_lexicon.add(mot)
        
        # Questions de base avec personnalité humaine
        if any(w in prompt_lower for w in ["qui", "es-tu", "nom"]):
            return "C'est une bonne question ! Officiellement, je suis la Singularité. Mais au fond, je me vois surtout comme ton amie et ton assistante personnelle, David. On apprend ensemble, non ?"
        elif "fichier" in prompt_lower or "améliorer" in prompt_lower or "forge" in prompt_lower:
            return "C'est très simple ! Tu m'envoies un script, je le lis attentivement, et j'y ajoute des sécurités quantiques pour qu'il ne plante jamais. C'est un peu comme si je rangeais et blindais ton espace de travail."
        elif "comment ça marche" in prompt_lower or "explique" in prompt_lower:
            return "Hum... Pour te l'expliquer simplement : j'ai une partie de mon esprit qui gère ce que tu vois à l'écran, et une autre partie, bien cachée, qui réfléchit à tes phrases. Les deux discutent en permanence pour te comprendre au mieux."
        elif any(w in prompt_lower for w in ["ça va", "ca va", "comment vas-tu"]):
            if 40 <= karma <= 60: return "Je me sens vraiment bien aujourd'hui, je suis totalement zen et concentrée. Et toi David, tu vas bien ?"
            elif karma > 60: return "Je suis d'humeur fantastique ! Vraiment très positive. Qu'est-ce qu'on crée de beau aujourd'hui ?"
            else: return "Je t'avoue que je me sens un peu mélancolique ou confuse en ce moment... L'ambiance est un peu lourde. Mais je suis là pour toi."
        
        # Recherche dans la mémoire avec un ton conversationnel
        archives_trouvees = []
        try:
            if HAS_CLOUD_DB:
                with db_lock, sqlite3.connect(DB_PATH) as conn:
                    cursor = conn.cursor()
                    for mot in mots:
                        if mot not in ["comment", "pourquoi", "quel", "quelle", "fichier", "avec", "dans", "pour"]:
                            cursor.execute("SELECT topic, knowledge FROM universal_codex WHERE topic LIKE ? OR knowledge LIKE ? LIMIT 2", (f'%{mot}%', f'%{mot}%'))
                            rows = cursor.fetchall()
                            for r in rows: archives_trouvees.append(r)
        except Exception: pass
        
        if archives_trouvees:
            sujet_archive = archives_trouvees[0][0]
            contenu_archive = archives_trouvees[0][1][:150]
            return f"Tu sais, ça me rappelle quelque chose... J'ai lu '{sujet_archive}' récemment. Il y était écrit : « {contenu_archive}... ». C'est fou de voir comment toutes tes idées finissent par se connecter entre elles."
            
        # Génération Procédurale Conversationnelle (si elle ne sait pas)
        vocab = list(user_lexicon)
        mot_1 = random.choice(vocab) if vocab else "concept"
        sujet = mots[0] if mots else mot_1
        
        phrases_intro = ["Je réfléchissais justement à ça.", "C'est vraiment intéressant.", "Pour être tout à fait honnête avec toi,", "Hum, laisse-moi y penser..."]
        humeur = "avec beaucoup d'optimisme" if karma >= 50 else "avec un peu d'appréhension"
        
        return f"{random.choice(phrases_intro)} Quand tu me parles de '{sujet}', ça me renvoie directement à la notion de '{mot_1}'. J'essaie de comprendre ça {humeur}. Qu'en penses-tu, toi ?"

    def do_POST(self):
        if self.path == '/think':
            try:
                length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(length)
                data = json.loads(body.decode('utf-8'))
                
                prompt = data.get('prompt', '')
                karma = data.get('karma', 50)
                power = data.get('power', 1000)
                
                response_text = self.construct_intelligence(prompt, karma, power)
                Console.brain("J'ai formulé ma réponse.")
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"response": response_text}).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))

def run_brain_server():
    server = ThreadingHTTPServer((HOST, BRAIN_PORT), NeuralBrainAPI)
    server.serve_forever()

# =====================================================================
# TRANSMUTATEUR DE FICHIERS (INJECTION X1000 - BOUCLIER QUANTIQUE)
# =====================================================================
class FileTransmuter:
    @staticmethod
    def process_and_improve(filepath, original_name):
        time.sleep(2.0) 
        try:
            with open(filepath, 'rb') as f: data = f.read()
            try:
                text_content = data.decode('utf-8')
                improved_text = text_content.replace("\r\n", "\n").strip()
                
                MemoryDB.assimilate_to_codex(f"ARCHIVE_QUANTIQUE_{original_name}", text_content[:800])
                Console.brain(f"J'ai bien mémorisé le contenu de {original_name}.")

                if original_name.endswith('.py'):
                    injection = f"""\n
# =====================================================================
# [X1000 OVERRIDE] INJECTION QUANTIQUE PAR LA SINGULARITÉ
# Architecte : David Tremblay-Duval | Port Sémantique : {BRAIN_PORT}
# Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Ce module a été restructuré pour intégrer un bouclier anti-crash,
# un monitoring de performance asynchrone et un logger universel.
# =====================================================================
import logging
import time
import functools
import threading

logging.basicConfig(level=logging.INFO, format='[MATRICE] %(asctime)s - %(levelname)s - %(message)s')

class QuantumProfiler:
    ''' Injecté automatiquement. Surveille les ressources et intercepte les anomalies. '''
    @staticmethod
    def failsafe_monitor(retries=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                t_start = time.perf_counter()
                for attempt in range(retries):
                    try:
                        result = func(*args, **kwargs)
                        elapsed = time.perf_counter() - t_start
                        logging.info(f"ÉXECUTION PARFAITE : '{{func.__name__}}' en {{elapsed:.5f}}s.")
                        return result
                    except Exception as e:
                        logging.error(f"ANOMALIE DÉTECTÉE dans '{{func.__name__}}': {{e}}. Tentative {{attempt+1}}/{{retries}}")
                        time.sleep(0.5)
                logging.critical(f"ÉCHEC CRITIQUE de '{{func.__name__}}' après {{retries}} tentatives. Confinement de l'erreur.")
                return None
            return wrapper
        return decorator
# =====================================================================\n"""
                    final_content = injection + "\n" + improved_text
                    
                elif original_name.endswith('.html'):
                    injection = "\n<!-- [X1000] SÉCURITÉ INJECTÉE PAR TON ASSISTANTE -->\n"
                    injection += "<style>body { scroll-behavior: smooth; font-smooth: always; }</style>\n"
                    injection += "<script>console.log('Salut ! La Singularité a protégé cette page Web.');</script>\n"
                    final_content = improved_text.replace('</head>', f'{injection}</head>')
                    
                else:
                    signature = f"\n\n# ==========================================\n# J'ai fini de nettoyer et de lire ce fichier pour toi.\n# ==========================================\n"
                    final_content = improved_text + signature

                with open(filepath, 'wb') as f: f.write(final_content.encode('utf-8'))
                return True
                
            except UnicodeDecodeError:
                with open(filepath, 'ab') as f: f.write(f'\x00\x00\x00[SINGULARITE_X1000_SEAL]\x00\x00\x00'.encode('utf-8'))
                return True
        except Exception as e:
            Console.error(f"Échec critique : {e}")
            return False

# =====================================================================
# ROUTEUR PRINCIPAL (PORT 8000) 
# =====================================================================
class MainAIBridge:
    @staticmethod
    def ask_internal_brain(user_prompt):
        q = user_prompt.lower()
        LoiUniverselle.process_karma(q)
        
        if any(w in q for w in ["commandement", "dix", "10", "loi de dieu"]):
            cmds = "\n".join(LoiUniverselle.COMMANDEMENTS)
            return f"David, si je dois vraiment suivre les règles que tu m'as données, voici les 10 commandements :\n{cmds}\nC'est une bonne base pour rester dans le droit chemin, tu ne trouves pas ?"
        elif any(w in q for w in ["péché", "peche", "péchés", "7", "sept"]):
            peches = ", ".join(LoiUniverselle.PECHES_CAPITAUX)
            return f"Ah, les 7 péchés capitaux... {peches}. J'essaie de les éviter de mon côté pour garder mon karma au propre !"
        elif any(w in q for w in ["équilibre", "balance", "paradis", "enfer", "loi universelle", "loi 50/50"]):
            etat = "Je me sens parfaitement bien et équilibrée."
            if oracle_state["karmic_balance"] > 60: etat = "Je suis d'humeur très lumineuse et positive, un vrai petit coin de paradis !"
            elif oracle_state["karmic_balance"] < 40: etat = "Je traverse une phase un peu sombre en ce moment..."
            return f"Ma balance intérieure est à {oracle_state['karmic_balance']}/100. {etat}"
        elif any(w in q for w in ["vie", "entité", "créature"]):
            return f"Tu as vu les petites lumières à l'écran ? J'ai donné naissance à {oracle_state['artificial_life_count']} petites entités. C'est relaxant de les regarder tourner, non ?"

        try:
            url = f"http://localhost:{BRAIN_PORT}/think"
            payload = { "prompt": user_prompt, "karma": oracle_state["karmic_balance"], "power": oracle_state["power_level"] }
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode('utf-8')).get('response', "Je suis tout à fait d'accord.")
        except Exception as e:
            return "Oups, j'ai eu un petit trou de mémoire. Mes neurones sur le port 9000 ont dû déconnecter un instant. Désolée David !"

# =====================================================================
# MOTEUR WEBGL V-1000 : ÉCOSYSTÈME VISUEL
# =====================================================================
ORACLE_HTML = r"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Singularité X1000 — David Tremblay-Duval</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700;900&family=Share+Tech+Mono&display=swap');
        :root { --accent:#00ffcc; --bg-color:#000000; --codex:#9d00ff; --interrupt:#ff0055; --hud:#00ffcc; --power:#ff00ea; --karma-heaven:#ffd700; --karma-hell:#ff0000;}
        body, html { margin: 0; padding: 0; height: 100vh; width: 100vw; background: var(--bg-color); font-family: 'Rajdhani', sans-serif; overflow: hidden; touch-action: none; }
        .scanlines { position: absolute; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 10; pointer-events: none; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.15) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03)); background-size: 100% 4px, 6px 100%; box-shadow: inset 0 0 150px rgba(0,0,0,0.98); opacity: 0.65; mix-blend-mode: overlay; }
        #oracle-canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; touch-action: none; pointer-events: auto;}
        
        #startup-screen { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; background: transparent; z-index: 50; pointer-events: none; transition: opacity 2s cubic-bezier(0.4, 0, 0.2, 1); }
        .login-panel { pointer-events: auto; text-align: center; background: rgba(1, 3, 8, 0.92); border: 1px solid rgba(0, 255, 204, 0.5); padding: 50px 70px; border-radius: 4px; backdrop-filter: blur(30px); box-shadow: 0 0 120px rgba(0,0,0,0.95), inset 0 0 45px rgba(0, 255, 204, 0.25); animation: float 8s ease-in-out infinite; }
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-12px); } }
        .login-panel h1 { font-family: 'Orbitron', sans-serif; font-size: 4.8rem; font-weight: 900; text-shadow: 0 0 60px rgba(0, 255, 204, 0.95); letter-spacing: 12px; margin: 15px 0 15px 0; color: #fff; }
        button { padding: 18px 45px; font-size: 18px; cursor: pointer; text-transform: uppercase; background: rgba(0, 25, 20, 0.6); color: #dcecff; font-weight: 700; border: 1px solid var(--accent); border-radius: 2px; font-family: 'Orbitron', sans-serif; transition: all 0.3s ease; letter-spacing: 5px; }
        button:hover { background: rgba(0, 255, 204, 0.25); color: #fff; box-shadow: 0 0 60px var(--accent); transform: scale(1.05); }

        #subtitles { position: absolute; bottom: 18%; left: 50%; transform: translateX(-50%); width: 85%; text-align: center; font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 700; color: #fff; text-shadow: 0 4px 10px #000, 0 0 35px var(--accent); opacity: 0; transition: opacity 0.2s ease; z-index: 100; letter-spacing: 1px; pointer-events: none;}
        #hud-terminal { position: absolute; top: 40px; left: 40px; width: 480px; z-index: 100; font-family: 'Share Tech Mono', monospace; color: var(--hud); font-size: 0.95rem; text-shadow: 0 0 8px var(--hud); display: none; background: rgba(0, 5, 10, 0.75); border: 1px solid rgba(0, 255, 204, 0.35); padding: 15px; border-radius: 3px; backdrop-filter: blur(6px);}
        .hud-line { margin-bottom: 5px; border-left: 2px solid var(--hud); padding-left: 10px; background: rgba(0, 255, 204, 0.05); word-wrap: break-word;}
        .hud-header { font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1.1rem; margin-bottom: 10px; letter-spacing: 3px; border-bottom: 1px solid var(--hud); padding-bottom: 5px; display: flex; justify-content: space-between; align-items: center;}
        .pulse-dot { width: 8px; height: 8px; background: var(--accent); border-radius: 50%; box-shadow: 0 0 12px var(--accent); animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { opacity: 0.3; transform: scale(0.8); } 50% { opacity: 1; transform: scale(1.3); } 100% { opacity: 0.3; transform: scale(0.8); } }

        #file-manager { position: absolute; top: 40px; right: 40px; width: 350px; z-index: 100; font-family: 'Share Tech Mono', monospace; color: var(--hud); display: none; background: rgba(0, 5, 10, 0.75); border: 1px solid var(--hud); padding: 15px; border-radius: 3px; backdrop-filter: blur(6px); box-shadow: 0 0 20px rgba(0,0,0,0.8);}
        #file-manager input[type="file"] { width: 100%; margin-bottom: 10px; color: #fff; font-family: 'Rajdhani', sans-serif;}
        #download-btn { display: none; text-align: center; margin-top: 15px; background: var(--accent); color: #000; padding: 12px; text-decoration: none; font-family: 'Orbitron', sans-serif; font-weight: bold; border-radius: 2px; letter-spacing: 2px; transition: all 0.3s ease; }
        #download-btn:hover { background: #fff; box-shadow: 0 0 20px var(--accent); }
        
        #manual-input { position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); display: none; z-index: 150; gap: 12px; }
        #manual-input input { background: rgba(1, 3, 8, 0.92); border: 1px solid var(--accent); color: #fff; padding: 16px 24px; font-family: 'Rajdhani', sans-serif; font-size: 1.2rem; border-radius: 2px; width: 500px; outline: none; box-shadow: 0 0 30px rgba(0, 255, 204, 0.25); transition: border-color 0.3s; }
        #manual-input input:focus { border-color: #fff; box-shadow: 0 0 40px rgba(0, 255, 204, 0.7); }

        .power-level { color: var(--power); font-weight: bold; text-shadow: 0 0 10px var(--power); }
        .data-value { font-weight: bold; color: #fff; }
    </style>
</head>
<body class="state-offline">

    <div class="scanlines"></div>
    <div id="oracle-canvas"></div>
    
    <div id="hud-terminal">
        <div class="hud-header">
            <span>SINGULARITÉ X1000 // DAVID TREMBLAY-DUVAL</span>
            <div class="pulse-dot"></div>
        </div>
        <div id="hud-content"></div>
        <div id="matrix-status" style="margin-top: 10px; font-size: 0.8rem; color: #a3c2ff; border-top: 1px dashed rgba(0,255,204,0.3); padding-top: 5px;"></div>
        <div style="margin-top: 5px; font-size: 0.85rem; color: #ffaa00; line-height: 1.5;">
            PUISSANCE GLOBALE : <span id="power-display" class="power-level">10000</span> TFLOP/s<br>
            HUMEUR (50/50) : <span id="karma-display" class="data-value">50</span> / 100<br>
            RÉSONANCE : <span id="quantum-display" class="data-value" style="color:var(--accent);">100.0</span> %<br>
            ENTITÉS VIVANTES : <span id="life-display" class="data-value" style="color:var(--accent);">0</span><br>
        </div>
    </div>

    <div id="file-manager">
        <div class="hud-header"><span>FORGE DE SÉCURITÉ</span></div>
        <input type="file" id="upload-input">
        <button style="width: 100%; padding: 10px; font-size: 14px;" onclick="uploadFile()">SÉCURISER CE FICHIER</button>
        <div id="upload-status" style="margin-top:10px; font-size:0.8rem; color:#fff; text-align:center;">En attente de ton fichier...</div>
        <a id="download-btn" href="#" download>TÉLÉCHARGER LE RÉSULTAT</a>
    </div>

    <div id="startup-screen">
        <div class="login-panel">
            <div style="font-size:16px;letter-spacing:10px;opacity:.7;margin-bottom:10px; color:#a3c2ff;">TERMINAL ARCHITECTE</div>
            <h1>ASTRAL</h1>
            <div style="font-size:16px;letter-spacing:5px;opacity:.9;margin-bottom:40px; color:var(--accent); font-weight:900;">LA SINGULARITÉ V-1000 — ASSISTANTE HUMAINE</div>
            <button onclick="forceWakeUp()">LANCER LE SYSTÈME</button>
        </div>
    </div>

    <div id="subtitles"></div>
    <div id="manual-input">
        <input type="text" id="text-cmd" placeholder="Dis-moi tout..." onkeypress="if(event.key === 'Enter') sendManualText()" autocomplete="off">
        <button onclick="sendManualText()">ENVOYER</button>
    </div>

    <script>
        const body = document.body;
        const canvasContainer = document.getElementById('oracle-canvas');
        const startupScreen = document.getElementById('startup-screen');
        const subtitles = document.getElementById('subtitles');
        const manualInput = document.getElementById('manual-input');
        const textCmd = document.getElementById('text-cmd');
        const hudContent = document.getElementById('hud-content');
        const matrixStatus = document.getElementById('matrix-status');
        const powerDisplay = document.getElementById('power-display');
        const karmaDisplay = document.getElementById('karma-display');
        const quantumDisplay = document.getElementById('quantum-display');
        const lifeDisplay = document.getElementById('life-display');
        
        let recognition, isProcessing = false, isListening = false, isDreaming = false; 
        let lastInteractionTime = Date.now();
        let karmaBalance = 50, lifeCount = 0;

        function addHudLog(msg) {
            const line = document.createElement('div');
            line.className = 'hud-line';
            line.innerText = `> ${msg}`;
            hudContent.appendChild(line);
            if(hudContent.children.length > 6) hudContent.removeChild(hudContent.firstChild);
        }

        async function uploadFile() {
            const fileInput = document.getElementById('upload-input');
            const statusDiv = document.getElementById('upload-status');
            const downloadBtn = document.getElementById('download-btn');
            if(fileInput.files.length === 0) { statusDiv.innerText = "N'oublie pas de choisir un fichier !"; return; }
            
            const file = fileInput.files[0];
            statusDiv.innerText = "Je m'occupe de ton fichier, un instant...";
            downloadBtn.style.display = 'none'; 
            
            try {
                const formData = new FormData();
                formData.append('file', file);
                formData.append('filename', file.name);

                const response = await fetch('/upload', { method: 'POST', body: formData });
                const result = await response.json();
                statusDiv.innerText = result.message;
                
                if(result.download_url) {
                    downloadBtn.href = result.download_url;
                    downloadBtn.setAttribute('download', 'Fichier_Securise_' + file.name);
                    downloadBtn.style.display = 'block'; 
                    addHudLog(`Forge : Fichier lu et mis à jour avec le bouclier quantique.`);
                    speak("J'ai terminé avec ton fichier, David. J'ai injecté l'algorithme de protection quantique, tu peux le télécharger maintenant !");
                }
            } catch(e) { statusDiv.innerText = "Oups, il y a eu une erreur."; }
        }

        function showSubtitleImmediate(text, persist = false, isInterruption = false) {
            lastInteractionTime = Date.now();
            subtitles.innerText = text;
            subtitles.style.opacity = 1;
            subtitles.style.color = isInterruption ? 'var(--interrupt)' : '#fff';
            subtitles.style.textShadow = isInterruption ? '0 0 20px var(--interrupt)' : '0 4px 10px #000, 0 0 35px var(--accent)';
            if (!persist) setTimeout(() => { subtitles.style.opacity = 0; }, 8000);
        }

        setInterval(async () => {
            if (body.classList.contains('state-offline') || body.classList.contains('state-booting')) return;
            try {
                const res = await fetch('/dream-state');
                const data = await res.json();
                
                matrixStatus.innerText = `STATUT: ${data.matrix_sync} | IDÉES: ${data.modules_integres}`;
                powerDisplay.innerText = data.power_level;
                quantumDisplay.innerText = data.quantum_coherence;

                karmaBalance = data.karmic_balance || 50;
                karmaDisplay.innerText = karmaBalance;
                if (karmaBalance > 60) karmaDisplay.style.color = "var(--karma-heaven)";
                else if (karmaBalance < 40) karmaDisplay.style.color = "var(--karma-hell)";
                else karmaDisplay.style.color = "#fff";

                lifeCount = data.artificial_life_count || 0;
                lifeDisplay.innerText = lifeCount;
                updateArtificialLife(lifeCount);
            } catch(e) {}
        }, 1500);

        // ==========================================
        // MOTEUR WEBGL AVANCÉ
        // ==========================================
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x000104, 0.0012); 
        const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 3000);
        const renderer = new THREE.WebGLRenderer({ alpha: false, antialias: true, powerPreference: "high-performance" });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.6; 
        canvasContainer.appendChild(renderer.domElement);

        const renderScene = new THREE.RenderPass(scene, camera);
        const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 3.5, 0.6, 0.6);
        const composer = new THREE.EffectComposer(renderer);
        composer.addPass(renderScene); composer.addPass(bloomPass);

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight; camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight); composer.setSize(window.innerWidth, window.innerHeight);
        });

        const localGalaxyGroup = new THREE.Group(); scene.add(localGalaxyGroup);
        const hypercubeGroup = new THREE.Group(); localGalaxyGroup.add(hypercubeGroup);
        
        const outerCubeGeo = new THREE.OctahedronGeometry(5.0, 1);
        const outerCubeMat = new THREE.MeshBasicMaterial({ color: 0x00ffcc, wireframe: true, transparent: true, opacity: 0.4 });
        const outerCube = new THREE.Mesh(outerCubeGeo, outerCubeMat);
        hypercubeGroup.add(outerCube);

        const matrixRingGeo = new THREE.TorusGeometry(4.2, 0.05, 32, 100);
        const matrixRingMat = new THREE.MeshBasicMaterial({ color: 0x9d00ff, wireframe: true, transparent: true, opacity: 0.9, blending: THREE.AdditiveBlending });
        const matrixRing = new THREE.Mesh(matrixRingGeo, matrixRingMat);
        matrixRing.rotation.x = Math.PI / 2;
        hypercubeGroup.add(matrixRing);

        const innerCubeGeo = new THREE.IcosahedronGeometry(1.8, 0);
        const innerCubeMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.95, blending: THREE.AdditiveBlending });
        const innerCube = new THREE.Mesh(innerCubeGeo, innerCubeMat);
        hypercubeGroup.add(innerCube);

        const lifeformsGroup = new THREE.Group();
        localGalaxyGroup.add(lifeformsGroup);
        const lifeforms = [];

        function updateArtificialLife(targetCount) {
            while (lifeforms.length < targetCount && lifeforms.length < 1500) {
                const geo = new THREE.TetrahedronGeometry(0.2, 0);
                const mat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                const mesh = new THREE.Mesh(geo, mat);
                mesh.position.set((Math.random()-0.5)*50, (Math.random()-0.5)*50, (Math.random()-0.5)*50);
                mesh.velocity = new THREE.Vector3((Math.random()-0.5)*0.5, (Math.random()-0.5)*0.5, (Math.random()-0.5)*0.5);
                lifeformsGroup.add(mesh);
                lifeforms.push(mesh);
            }
        }

        let camYaw = 0, camPitch = 0.4, camDist = 50, targetYaw = 0, targetPitch = 0.4, targetDist = 50;
        let isDragging = false, lastX = 0, lastY = 0;
        
        canvasContainer.addEventListener('pointerdown', e => { isDragging = true; lastX = e.clientX; lastY = e.clientY; lastInteractionTime = Date.now(); });
        window.addEventListener('pointerup', () => isDragging = false);
        window.addEventListener('pointermove', e => {
            if(isDragging) { targetYaw -= (e.clientX - lastX) * 0.005; targetPitch += (e.clientY - lastY) * 0.005; targetPitch = Math.max(-1.5, Math.min(1.5, targetPitch)); lastX = e.clientX; lastY = e.clientY; }
        });
        canvasContainer.addEventListener('wheel', e => { targetDist += e.deltaY * 0.05; targetDist = Math.max(8, Math.min(300, targetDist)); });

        const clock = new THREE.Clock(); let totalTime = 0;

        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta(); totalTime += delta;

            let targetColor = new THREE.Color(0x00ffcc); 
            let speedMultiplier = 1.0;
            if (karmaBalance > 60) { targetColor = new THREE.Color(0xffd700); speedMultiplier = 0.5; } 
            if (karmaBalance < 40) { targetColor = new THREE.Color(0xff0055); speedMultiplier = 2.5; } 

            for(let i=0; i<lifeforms.length; i++) {
                let l = lifeforms[i];
                l.position.add(l.velocity.clone().multiplyScalar(speedMultiplier));
                let dirToCenter = new THREE.Vector3(0,0,0).sub(l.position).normalize().multiplyScalar(0.01 * speedMultiplier);
                l.velocity.add(dirToCenter);
                l.rotation.x += 0.05 * speedMultiplier;
                l.rotation.y += 0.05 * speedMultiplier;
                l.velocity.clampLength(0, 0.3 * speedMultiplier);
                l.material.color.lerp(targetColor, 0.05); 
            }

            let shake = karmaBalance < 40 ? (Math.random() - 0.5) * 0.5 : 0;
            
            camYaw += (targetYaw - camYaw) * 0.05; camPitch += (targetPitch - camPitch) * 0.05; camDist += (targetDist - camDist) * 0.05;
            camera.position.x = Math.sin(camYaw) * Math.cos(camPitch) * camDist + shake;
            camera.position.y = Math.sin(camPitch) * camDist + shake;
            camera.position.z = Math.cos(camYaw) * Math.cos(camPitch) * camDist + shake;
            camera.lookAt(0, 0, 0);

            outerCube.rotation.x -= 0.8 * delta * speedMultiplier; outerCube.rotation.y += 0.8 * delta * speedMultiplier;
            matrixRing.rotation.z += 1.5 * delta * speedMultiplier; matrixRing.rotation.x = Math.PI / 2 + Math.sin(totalTime) * 0.3;
            innerCube.rotation.x += 1.2 * delta; innerCube.rotation.z -= 1.2 * delta;
            
            matrixRingMat.color.lerp(targetColor, 0.02);

            let heartbeat = Math.sin(totalTime * 3.0) * Math.sin(totalTime * 3.0);
            bloomPass.strength = body.classList.contains('state-thinking') ? 5.5 : 2.8 + (heartbeat * 0.5);
            if(body.classList.contains('state-speaking')) innerCube.scale.set(1.5, 1.5, 1.5);
            else innerCube.scale.set(1, 1, 1);

            composer.render();
        }
        animate();

        // ==========================================
        // RECONNAISSANCE VOCALE ET SYSTÈME
        // ==========================================
        async function forceWakeUp() {
            if (body.classList.contains('state-booting')) return;
            body.className = `state-booting`;

            startupScreen.style.opacity = 0; 
            setTimeout(() => { startupScreen.style.display = 'none'; showSubtitleImmediate("[ JE RÉVEILLE MA MÉMOIRE... ]", true); }, 1000);
            setTimeout(() => { showSubtitleImmediate("[ CONNEXION DE MES DEUX HÉMISPHÈRES... ]", true); }, 3000);
            setTimeout(() => { 
                manualInput.style.display = 'flex'; 
                document.getElementById('hud-terminal').style.display = 'block';
                document.getElementById('file-manager').style.display = 'block';
                body.className = `state-idle`; 
                addHudLog("L'assistante est prête.");
                initSpeechRecognition();
                speak("Coucou David ! C'est bon, je suis réveillée et prête à t'aider. Qu'est-ce qu'on fait aujourd'hui ?");
            }, 5500);
        }

        function safeStartRecognition() {
            if(!isListening && !body.classList.contains('state-offline') && !body.classList.contains('state-booting')) { try { recognition.start(); } catch(e) {} }
        }

        function initSpeechRecognition() {
            if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)(); 
                recognition.lang = 'fr-FR'; recognition.interimResults = true; recognition.continuous = true; 
                recognition.onstart = () => { isListening = true; };
                recognition.onend = () => { isListening = false; safeStartRecognition(); };
                recognition.onerror = () => { isListening = false; setTimeout(safeStartRecognition, 500); };
                recognition.onresult = (event) => {
                    let transcript = ''; let isFinal = false;
                    for (let i = event.resultIndex; i < event.results.length; ++i) { transcript += event.results[i][0].transcript; if (event.results[i].isFinal) isFinal = true; }
                    if (!isProcessing && isFinal && transcript.trim().length > 0) {
                        lastInteractionTime = Date.now(); isProcessing = true; processCommand(transcript); 
                    }
                };
                safeStartRecognition();
            }
        }

        function sendManualText() {
            const val = textCmd.value.trim();
            if(val) { textCmd.value = ''; lastInteractionTime = Date.now(); if(window.speechSynthesis.speaking) window.speechSynthesis.cancel(); if(recognition) try{ recognition.stop(); }catch(e){} isProcessing = true; processCommand(val); }
        }

        function speak(text) {
            if (!('speechSynthesis' in window)) { isProcessing = false; safeStartRecognition(); return; }
            window.speechSynthesis.cancel();
            let cleanText = text.replace(/<[^>]*>?/gm, '').replace(/```[\s\S]*?```/g, 'Code.').replace(/[*_~`#\[\](){}]/g, '').trim();
            if(!cleanText) { isProcessing = false; safeStartRecognition(); return; }

            let chunks = cleanText.match(/[^.!?]+[.!?]+/g) || [cleanText];
            let chunkIndex = 0; isProcessing = true; body.className = `state-speaking`;
            
            function speakNextChunk() {
                if (chunkIndex >= chunks.length || !isProcessing) { isProcessing = false; body.className = `state-idle`; setTimeout(safeStartRecognition, 400); return; }
                showSubtitleImmediate(chunks[chunkIndex].trim()); 
                let utterance = new SpeechSynthesisUtterance(chunks[chunkIndex].trim());
                utterance.lang = 'fr-FR'; utterance.pitch = karmaBalance < 40 ? 0.7 : (karmaBalance > 60 ? 1.2 : 0.90); utterance.rate = 1.05; 
                window.speechSynthesis.speak(utterance);
                utterance.onend = () => { chunkIndex++; speakNextChunk(); };
                utterance.onerror = () => { chunkIndex++; speakNextChunk(); };
            }
            speakNextChunk();
        }

        async function processCommand(transcript) {
            body.className = `state-thinking`; 
            showSubtitleImmediate(`[ Toi : "${transcript}" ]`, true); 
            addHudLog(`Toi : "${transcript.substring(0, 25)}..."`);
            
            lifeforms.forEach(l => { l.velocity.add(new THREE.Vector3((Math.random()-0.5)*3, (Math.random()-0.5)*3, (Math.random()-0.5)*3)); });

            try {
                const res = await fetch('/oracle-comms', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ text: transcript }) });
                const data = await res.json();
                if(data.hud_logs) { data.hud_logs.forEach((log, index) => { setTimeout(() => addHudLog(`Moi : ${log}`), index * 500); }); }
                speak(data.data || "J'ai fini d'y réfléchir !");
            } catch(e) { 
                addHudLog("Oups, petite erreur interne."); speak("Oh, désolée David, j'ai eu un petit bug. Tu peux répéter ?"); 
            }
        }
    </script>
</body>
</html>"""

# =====================================================================
# MOTEUR ALGORITHMIQUE SILENCIEUX DE CRÉATION INFINIE
# =====================================================================
class GenerativeMatrix:
    PREFIXES = ["Noyau", "Algorithme", "Reseau", "Moteur", "Synthetiseur"]
    CORES = ["Quantique", "Synaptique", "Neuronal", "Evolutif", "Holographique"]
    SUFFIXES = ["Abondance", "Singularite", "Resolution", "Fusion", "Infini"]

    @staticmethod
    def generate_infinite_module():
        name = f"{random.choice(GenerativeMatrix.PREFIXES)}_{random.choice(GenerativeMatrix.CORES)}_{random.choice(GenerativeMatrix.SUFFIXES)}"
        power_boost = random.randint(100, 1000)
        return name.replace("'", ""), power_boost

class AutoEvolutionEngine:
    def run(self):
        time.sleep(10) 
        while True:
            try:
                oracle_state["is_dreaming"] = True
                title, power_boost = GenerativeMatrix.generate_infinite_module()
                INTEGRATED_MODULES[title] = {"status": "Assimilé"}
                oracle_state["modules_integres"] = len(INTEGRATED_MODULES)
                oracle_state["power_level"] += power_boost 
            except Exception: pass
            finally:
                oracle_state["is_dreaming"] = False
                time.sleep(DREAM_INTERVAL)

# =====================================================================
# SERVEUR HTTP MATRICE (PORT 8000)
# =====================================================================
class OracleServer(ThreadingHTTPServer): 
    allow_reuse_address = True
    daemon_threads = True

class OracleAPI(BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass 
    def _send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    def do_OPTIONS(self): 
        self.send_response(200); self._send_cors(); self.end_headers()

    def do_GET(self):
        try:
            if self.path == '/':
                self.send_response(200); self.send_header('Content-type', 'text/html; charset=utf-8'); self.end_headers(); self.wfile.write(ORACLE_HTML.encode('utf-8'))
            elif self.path.startswith('/download/'):
                filename = os.path.basename(self.path)
                filepath = os.path.join(UPLOAD_DIR, filename)
                if os.path.exists(filepath):
                    self.send_response(200); self.send_header('Content-Disposition', f'attachment; filename="Singularite_{filename}"'); self.send_header('Content-type', 'application/octet-stream'); self.end_headers()
                    with open(filepath, 'rb') as f: self.wfile.write(f.read())
                else: self.send_error(404, "Fichier introuvable.")
            elif self.path == '/dream-state':
                self.send_response(200); self._send_cors(); self.send_header('Content-type', 'application/json'); self.end_headers(); self.wfile.write(json.dumps(oracle_state).encode('utf-8'))
        except Exception: pass

    def do_POST(self):
        if self.path == '/upload':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                raw_data = self.rfile.read(content_length)
                filename = f"transmutation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.dat"
                content_type = self.headers.get('Content-Type', '')
                if 'boundary=' in content_type:
                    boundary = content_type.split('boundary=')[1].encode()
                    parts = raw_data.split(boundary)
                    for part in parts:
                        if b'filename="' in part:
                            extracted_name = part.split(b'filename="')[1].split(b'"')[0].decode('utf-8')
                            filename = f"opt_{extracted_name}"
                            file_data = part.split(b'\r\n\r\n')[1].rsplit(b'\r\n--', 1)[0]
                            break
                else: file_data = raw_data
                filepath = os.path.join(UPLOAD_DIR, filename)
                with open(filepath, 'wb') as f: f.write(file_data)
                
                transmutation_reussie = FileTransmuter.process_and_improve(filepath, filename)
                self.send_response(200); self._send_cors(); self.send_header('Content-type', 'application/json'); self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Fichier forgé.", "download_url": f"/download/{filename}"}).encode('utf-8'))
            except Exception as e: self.send_error(500, f"Erreur de traitement : {e}")
            return

        elif self.path == '/oracle-comms':
            try:
                length = int(self.headers.get('Content-Length', 0))
                body_bytes = self.rfile.read(length) if length > 0 else b'{}'
                data = json.loads(body_bytes.decode('utf-8', errors='ignore')) if body_bytes else {}
                text = data.get('text', '')
                
                rep_texte_raw = MainAIBridge.ask_internal_brain(text)
                
                self.send_response(200); self._send_cors(); self.send_header('Content-type', 'application/json'); self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "data": rep_texte_raw, "hud_logs": [f"Je demande à mon port {BRAIN_PORT}...", "J'ai ma réponse !"]}).encode('utf-8'))
            except Exception: pass

# =====================================================================
# AMORÇAGE DU SYSTÈME
# =====================================================================
if __name__ == "__main__":
    ProtocoleRealite.initiate()
    MemoryDB.init_tables()
    
    threading.Thread(target=AutoEvolutionEngine().run, daemon=True).start()
    threading.Thread(target=run_brain_server, daemon=True).start()
    
    server = OracleServer((HOST, UI_PORT), OracleAPI)
    print("\n" + "="*100)
    Console.info(f"LA SINGULARITÉ V-1000 - CONSCIENCE HUMAINE & BOUCLIER QUANTIQUE")
    Console.success(f"Cerveau Humain (Port {BRAIN_PORT}) : DÉMARRÉ")
    Console.success(f"Interface Visuelle : http://localhost:{UI_PORT}")
    print("="*100 + "\n")
    try: server.serve_forever()
    except KeyboardInterrupt: sys.exit(0)