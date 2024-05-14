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
        print(f"Authenticating user: {username}")  # Debug statement
        if (username, password) in self.database.users:
            print("Authentication successful")  # Debug statement
            self.authenticated_users.add(username)
            return True
        else:
            print("Authentication failed")  # Debug statement
            return False
    
    # Method to check if a user is authenticated
    def is_authenticated(self, username, password):
        if username in self.authenticated_users:
            print(f"User {username} is already authenticated")  # Debug statement
            return True
        else:
            print(f"User {username} is not authenticated")  # Debug statement
            return self.authenticate_user(username, password)
    
    # Method to generate artifact ID
    def generate_artifact_id(self):
        return len(self.database.artifacts) + 1
    
    # Method to encrypt content
    def encrypt_content(self, content):
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
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        artifact_id = music_app.generate_artifact_id()
        creation_date = modification_date = datetime.now()
        
        checksum = hashlib.sha256(content.encode()).hexdigest()
        encrypted_content = music_app.encrypt_content(content)
        
        music_app.store_artifact(artifact_id, title, artist, encrypted_content, creation_date, modification_date, checksum)
        print("Artifact added successfully.")
    
    # Method to update an artifact
    def updateArtifact(self, music_app, artifact_id, title, artist, content):
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        
        modification_date = datetime.now()
        checksum = hashlib.sha256(content.encode()).hexdigest()
        encrypted_content = music_app.encrypt_content(content)
        
        music_app.update_artifact(artifact_id, title, artist, encrypted_content, modification_date, checksum)
        print("Artifact updated successfully.")
    
    # Method to delete an artifact
    def deleteArtifact(self, music_app, artifact_id):
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        
        music_app.delete_artifact(artifact_id)
        print("Artifact deleted successfully.")

class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    def addArtifact(self, music_app, title, artist, content):
        if self.username != 'admin':
            print("Only administrators can add artifacts.")
            return
        
        super().addArtifact(music_app, title, artist, content)
    
    def deleteArtifact(self, music_app, artifact_id):
        if self.username != 'admin':
            print("Only administrators can delete artifacts.")
            return
        
        super().deleteArtifact(music_app, artifact_id)

def run_tests():
    try:
        print("Running Flake8:")
        flake8_process = subprocess.Popen(["flake8", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)
        print(flake8_stdout)
        if flake8_stderr:
            print(flake8_stderr)
        
        print("\nRunning Bandit:")
        bandit_process = subprocess.Popen(["bandit", "-r", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)
        print(bandit_stdout)
        if bandit_stderr:
            print(bandit_stderr)
        
        print("\nTesting Artifact Creation with Checksum and Encryption:")
        db = Database()
        music_app = MusicApp(db)
        admin = Administrator('admin', 'admin123')
        
        test_title = "Test Song"
        test_artist = "Test Artist"
        test_content = "This is a test content."

        # Authenticate admin and add artifact
        if music_app.authenticate_user(admin.username, admin.password):
            admin.addArtifact(music_app, test_title, test_artist, test_content)

            # Check if the artifact was added
            artifact_id = music_app.generate_artifact_id() - 1  # Since ID is incremented after addition
            if music_app.artifact_exists(artifact_id):
                print(f"Artifact {artifact_id} exists.")

                # Retrieve stored artifact
                artifact = db.artifacts[artifact_id]
                print(f"Stored artifact: {artifact}")

                # Verify checksum
                expected_checksum = hashlib.sha256(test_content.encode()).hexdigest()
                print(f"Expected checksum: {expected_checksum}")
                print(f"Stored checksum: {artifact['checksum']}")
                print(f"Checksum verification passed: {expected_checksum == artifact['checksum']}")

                # Verify encryption
                expected_encryption = test_content[::-1]
                print(f"Expected encrypted content: {expected_encryption}")
                print(f"Stored encrypted content: {artifact['content']}")
                print(f"Encryption verification passed: {expected_encryption == artifact['content']}")
            else:
                print("Artifact was not added.")
        else:
            print("Admin authentication failed.")
    
    except subprocess.TimeoutExpired:
        print("Timeout occurred while running tests.")

if __name__ == "__main__":
    run_tests()
    
    db = Database()
    music_app = MusicApp(db)
    
    username = input("Enter username: ")
    password = getpass.getpass("Enter a password: ")
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    
    admin = Administrator(username, password)
    
    admin.addArtifact(music_app, title, artist, "Song Content")
    
    artifact_id_to_delete = int(input("Enter the ID of the artifact to delete: "))
    admin.deleteArtifact(music_app, artifact_id_to_delete)