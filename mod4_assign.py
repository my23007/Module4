import subprocess
import hashlib
from datetime import datetime
import getpass

class Database:
    def __init__(self):
        self.users = {('admin', 'admin123')}
        self.artifacts = {}

class MusicApp:
    def __init__(self, database):
        self.database = database
        self.authenticated_users = set()
    
    # Method to authenticate a user
    def authenticate_user(self, username, password):
        # Simplified authentication logic
        if (username, password) in self.database.users:
            self.authenticated_users.add(username)
            return True
        else:
            return False
    
    # Method to check if a user is authenticated
    def is_authenticated(self, username, password):
        return username in self.authenticated_users
    
    # Method to generate artifact ID
    def generate_artifact_id(self):
        # Simplified artifact ID generation (can be more complex)
        return len(self.database.artifacts) + 1
    
    # Method to encrypt content
    def encrypt_content(self, content):
        # Simplified encryption (can be more secure)
        return content[::-1]  # Reverse content as an example
    
    # Method to check if an artifact exists
    def artifact_exists(self, artifact_id):
        return artifact_id in self.database.artifacts
    
    # Method to store an artifact
    def store_artifact(self, artifact_id, title, artist, content, creation_date, modification_date, checksum):
        self.database.artifacts[artifact_id] = {
            'title': title,
            'artist': artist,
            'content': content,
            'creation_date': creation_date,
            'modification_date': modification_date,
            'checksum': checksum
        }
    
    # Method to update an artifact
    def update_artifact(self, artifact_id, title, artist, content, modification_date, checksum):
        self.database.artifacts[artifact_id].update({
            'title': title,
            'artist': artist,
            'content': content,
            'modification_date': modification_date,
            'checksum': checksum
        })
    
    # Method to delete an artifact
    def delete_artifact(self, artifact_id):
        del self.database.artifacts[artifact_id]

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # Method to add an artifact
    def addArtifact(self, music_app, title, artist, content):
        # Check if user is authenticated
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        # Generate artifact ID and timestamps
        artifact_id = music_app.generate_artifact_id()
        creation_date = modification_date = datetime.now()
        
        # Calculate checksum
        checksum = hashlib.sha256(content.encode()).hexdigest()
        
        # Encrypt content
        encrypted_content = music_app.encrypt_content(content)
        
        # Store artifact
        music_app.store_artifact(artifact_id, title, artist, encrypted_content, creation_date, modification_date, checksum)
        print("Artifact added successfully.")
    
    # Method to update an artifact
    def updateArtifact(self, music_app, artifact_id, title, artist, content):
        # Check if user is authenticated
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        # Check if artifact exists
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        
        # Generate modification timestamp
        modification_date = datetime.now()
        
        # Calculate checksum
        checksum = hashlib.sha256(content.encode()).hexdigest()
        
        # Encrypt content
        encrypted_content = music_app.encrypt_content(content)
        
        # Update artifact
        music_app.update_artifact(artifact_id, title, artist, encrypted_content, modification_date, checksum)
        print("Artifact updated successfully.")
    
    # Method to delete an artifact
    def deleteArtifact(self, music_app, artifact_id):
        # Check if user is authenticated
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        # Check if artifact exists
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        
        # Delete artifact
        music_app.delete_artifact(artifact_id)
        print("Artifact deleted successfully.")

class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    # Method to add an artifact (overriding User's method)
    def addArtifact(self, music_app, title, artist, content):
        # Administrator authentication check
        if self.username != 'admin':
            print("Only administrators can add artifacts.")
            return
        
        # Call the parent method to add artifact
        super().addArtifact(music_app, title, artist, content)
    
    # Method to delete an artifact (new method for Administrator)
    def deleteArtifact(self, music_app, artifact_id):
        # Administrator authentication check
        if self.username != 'admin':
            print("Only administrators can delete artifacts.")
            return
        
        # Call the parent method to delete artifact
        super().deleteArtifact(music_app, artifact_id)

# Automated testing tools and security testing
def run_tests():
    try:
        # Run Flake8
        print("Running Flake8:")
        flake8_process = subprocess.Popen(["flake8", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)  # Adjust timeout as needed
        print(flake8_stdout)
        if flake8_stderr:
            print(flake8_stderr)
        
        # Run Bandit
        print("\nRunning Bandit:")
        bandit_process = subprocess.Popen(["bandit", "-r", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)  # Adjust timeout as needed
        print(bandit_stdout)
        if bandit_stderr:
            print(bandit_stderr)
    
    except subprocess.TimeoutExpired:
        print("Timeout occurred while running tests.")

# Usage example
if __name__ == "__main__":
    run_tests()  # Run automated tests
    
    db = Database()
    music_app = MusicApp(db)
    
    username = input("Enter username: ")
    password = getpass.getpass("Enter a password: ")  # Securely get the password
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    
    admin = Administrator(username, password)  # Create a user or administrator
    
    # Add an artifact
    admin.addArtifact(music_app, title, artist, "Song Content")
    
    # Delete an artifact
    artifact_id_to_delete = int(input("Enter the ID of the artifact to delete: "))
    admin.deleteArtifact(music_app, artifact_id_to_delete)