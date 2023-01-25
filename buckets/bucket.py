from flask import Blueprint, request, jsonify
from database import db, Bucket, User
from flask_jwt_extended import get_jwt_identity, jwt_required

bucket = Blueprint("bucket", __name__, url_prefix='/bucket')

@bucket.get("/")
@jwt_required()
def all_bucket():
    all_buckets = Bucket.query.all()
    bucket_list = []
    for bucket in all_buckets:
        bucket_list.append({
            "bucket-id": bucket.bucket_id,
            "bucket-name": bucket.name,
            "bucket-description": bucket.description,
            "image_link": bucket.image_link,
        })

    return jsonify({"buckets": bucket_list}), 200 


@bucket.post("/create-bucket")
@jwt_required()
def create_bucket():
    bucket_name = request.json.get("name", "")
    bucket_description = request.json.get("description", "")
    bucket_image_link = request.json.get("image_link", "")

    bucket = Bucket.query.filter_by(name=bucket_name).first()
    if bucket:
        return jsonify({"Error": "A Bucket with this name already exists"}), 400
    
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    created_bucket = Bucket(name=bucket_name, description=bucket_description, image_link=bucket_image_link, user_id=user.id)
    db.session.add(created_bucket)
    db.session.commit()
    return jsonify({
        "Bucket": {
            "name": bucket_name,
            "description": bucket_description,
            "image_link(s)": bucket_image_link,
            "bucket_id": created_bucket.bucket_id,
            "created_at": created_bucket.created_at,
            "updated_at": created_bucket.updated_at
        }
    }), 200

@bucket.get("/bucket/<bucket_id>")
@jwt_required()
def get_bucket(bucket_id):
    bucket_info = Bucket.query.filter_by(bucket_id=bucket_id).first()

    if not bucket_info:
        return jsonify({"Error": "Incorrect bucket id"}), 400
    
    return jsonify({
        "Bucket": {
            "name": bucket_info.name,
            "description": bucket_info.description,
            "bucket_id": bucket_info.bucket_id,
            "image_link": bucket_info.image_link,
            "created_at": bucket_info.created_at,
            "updated_at": bucket_info.updated_at
        }
    }), 200


@bucket.put("/bucket/<bucket_id>/edit/")
@bucket.patch("bucket/<bucket_id>/edit/")
@jwt_required()
def edit_bucket(bucket_id):
    image_link = request.json.get("image_link", "")

    bucket = Bucket.query.filter_by(bucket_id=bucket_id).first()

    if not bucket:
        return jsonify({"Error": "Invalid bucket ID"}), 400 
    bucket.image_link = image_link
    db.session.commit()

    return jsonify({
        "Message": "Bucket successfully updated"
    }), 200