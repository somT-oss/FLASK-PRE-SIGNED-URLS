from flask import Blueprint, request, jsonify
from database import db, Bucket

bucket = Blueprint("bucket", __name__, url_prefix='/bucket')

@bucket.get("/")
def all_bucket():
    all_buckets = Bucket.query.all()
    bucket_list = []
    for bucket in all_buckets:
        bucket_list.append({
            "bucket-id": bucket.bucket_id,
            "bucket-name": bucket.name,
            "bucket-description": bucket.description
        })

    return jsonify({"buckets": bucket_list}), 200 

@bucket.post("/create-bucket")
def create_bucket():
    pass 
