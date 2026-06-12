# my-dashsys-project

Dépendences : 

-Python3/ pip / venv 
- Requests
-psutil

Listes des commandes à effectuer :  

# 1. Met à jour la liste des paquets disponibles
-apt update

# 2. Installe Python 3, Pip et le module pour les environnements virtuels (venv)
-apt install python3 python3-pip python3-venv -y

# 3. Installe les bibliothèques nécessaires : 
-pip install requests
-pip install psutil

# 4. Crée le dossier du serveur
-mkdir /opt/sysagent
-cd /opt/sysagent

# 5. Crée et active l'environnement virtuel
-python3 -m venv venv
-source venv/bin/activate

# 6. Ajouter le fichier agent.py dans le répertoire /opt/sysagent 

Il faut ensuite voir pour faire un docker pull de l'image docker pour la configuration de la machine serveur :

docker push hjabdoul/dashsys-server:tagname

Pour lancer le conteneur, faire la commande suivante : 

docker run -d -p 5000:5000 --name [donner un nom] dashsys-server

Lancer le script : 
- python agent.py

Pour tester sur une nouvelle machine Linux : 

- git clone https://github.com/hjabdoul/my-dashsys-project.git
- cd my-dashsys-project
- pip install -r requirements.txt
- python agent.py
