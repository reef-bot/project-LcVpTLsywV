# mongodb.py

import pymongo

class MongoDB:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        
    def insert_moderation_action(self, action_data):
        try:
            self.db.moderation_actions.insert_one(action_data)
            return True
        except Exception as e:
            print(f"Error inserting moderation action: {e}")
            return False
        
    def get_moderation_actions(self):
        try:
            actions = self.db.moderation_actions.find()
            return list(actions)
        except Exception as e:
            print(f"Error getting moderation actions: {e}")
            return []
        
    def insert_user_data(self, user_data):
        try:
            self.db.user_data.insert_one(user_data)
            return True
        except Exception as e:
            print(f"Error inserting user data: {e}")
            return False
        
    def get_user_data(self, user_id):
        try:
            user = self.db.user_data.find_one({"user_id": user_id})
            return user
        except Exception as e:
            print(f"Error getting user data: {e}")
            return None

    def update_user_data(self, user_id, new_data):
        try:
            self.db.user_data.update_one({"user_id": user_id}, {"$set": new_data})
            return True
        except Exception as e:
            print(f"Error updating user data: {e}")
            return False

    def delete_user_data(self, user_id):
        try:
            self.db.user_data.delete_one({"user_id": user_id})
            return True
        except Exception as e:
            print(f"Error deleting user data: {e}")
            return False

    def close_connection(self):
        self.client.close()