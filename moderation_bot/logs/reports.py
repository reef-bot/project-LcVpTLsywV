# reports.py

import pymongo
from datetime import datetime

class Reports:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["moderation_bot"]
        self.collection = self.db["reports"]

    def log_report(self, report_type, user_id, reason):
        report = {
            "report_type": report_type,
            "user_id": user_id,
            "reason": reason,
            "timestamp": datetime.now()
        }
        self.collection.insert_one(report)

    def get_reports(self):
        reports = self.collection.find()
        return reports

    def clear_reports(self):
        self.collection.delete_many({})