# core/config.py
# Configuration centralisée pour l'API Insider Trends - SÉCURISÉE

import os
from typing import Optional
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

class Settings:
    """Configuration centralisée de l'application - SÉCURISÉE"""
    
    def __init__(self):
        # =====================================================
        # CONFIGURATION SÉCURISÉE - PAS DE VALEURS PAR DÉFAUT
        # =====================================================
        
        # Base de données - OBLIGATOIRE
        self.DATABASE_URL: str = os.getenv("DATABASE_URL")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL must be set in environment variables")
        
        # Clé secrète JWT - OBLIGATOIRE
        self.SECRET_KEY: str = os.getenv("SECRET_KEY")
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY must be set in environment variables")
        
        # Configuration JWT
        self.ALGORITHM: str = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
        
        # Configuration Instagram Business API - OBLIGATOIRE
        self.IG_ACCESS_TOKEN: Optional[str] = os.getenv("IG_ACCESS_TOKEN")
        self.IG_USER_ID: Optional[str] = os.getenv("IG_USER_ID")
        self.IG_APP_ID: Optional[str] = os.getenv("IG_APP_ID")
        self.IG_APP_SECRET: Optional[str] = os.getenv("IG_APP_SECRET")
        self.IG_REDIRECT_URI: str = os.getenv("IG_REDIRECT_URI", "https://www.insidr.dev/auth/callback")
        
        # Configuration Facebook API - OBLIGATOIRE
        self.FB_APP_ID: Optional[str] = os.getenv("FB_APP_ID")
        self.FB_APP_SECRET: Optional[str] = os.getenv("FB_APP_SECRET")
        self.FB_REDIRECT_URI: str = os.getenv("FB_REDIRECT_URI", "https://www.insidr.dev/auth/facebook/callback")
        
        # Configuration OAuth - OBLIGATOIRE
        self.OAUTH_STATE_SECRET: str = os.getenv("OAUTH_STATE_SECRET")
        if not self.OAUTH_STATE_SECRET:
            raise ValueError("OAUTH_STATE_SECRET must be set in environment variables")
        
        # Configuration Webhook - OBLIGATOIRE
        self.WEBHOOK_VERIFY_TOKEN: str = os.getenv("WEBHOOK_VERIFY_TOKEN")
        if not self.WEBHOOK_VERIFY_TOKEN:
            raise ValueError("WEBHOOK_VERIFY_TOKEN must be set in environment variables")
        
        # Configuration MeiliSearch (optionnel)
        self.MEILI_HOST: str = os.getenv("MEILI_HOST", "http://localhost:7700")
        self.MEILI_INDEX: str = os.getenv("MEILI_INDEX", "posts")
        self.MEILI_MASTER_KEY: Optional[str] = os.getenv("MEILI_MASTER_KEY")
        
        # Configuration Google OAuth - OBLIGATOIRE
        self.GOOGLE_CLIENT_ID: Optional[str] = os.getenv("GOOGLE_CLIENT_ID")
        self.GOOGLE_CLIENT_SECRET: Optional[str] = os.getenv("GOOGLE_CLIENT_SECRET")
        
        # Configuration redirect URI selon l'environnement
        if os.getenv("ENVIRONMENT") == "production":
            self.GOOGLE_REDIRECT_URI: str = os.getenv("GOOGLE_REDIRECT_URI_PROD", "https://www.insidr.dev/api/v1/auth/google/callback")
        else:
            self.GOOGLE_REDIRECT_URI: str = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/api/v1/auth/google/callback")
        
        # Configuration Redis (optionnel)
        self.REDIS_URL: str = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

# Instance globale
settings = Settings()