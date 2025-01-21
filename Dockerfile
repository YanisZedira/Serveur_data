FROM python:3.9

# Définir la variable d'environnement pour le chemin de l'application
ENV APP_HOME /app

# Définir le répertoire de travail
WORKDIR $APP_HOME

# Mettre à jour le système et installer les dépendances
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev

# Copier les dépendances Python
COPY requirements .

# Installer les dépendances listées dans requirements.txt
RUN pip install -r requirements

# Copier tout le contenu du projet
COPY . .

# Définir la commande par défaut pour démarrer l'application
CMD ["python3", "app.py"]
