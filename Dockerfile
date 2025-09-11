# Utilise une image Python légère
FROM python:3.12-slim

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances système utiles
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie le fichier de dépendances
COPY requirements.txt .

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le projet dans le conteneur
COPY . .

# Expose le port (par défaut Django utilise 8000)
EXPOSE 8000

# Commande de lancement
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
