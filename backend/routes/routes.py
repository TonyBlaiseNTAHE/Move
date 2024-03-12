from flask import Flask, request, jsonify, Blueprint
from app import db
from user import User
from movie import Movie
from subscription import Subscription
from paypal import Payment

bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@bp.route('/movies', methods=['POST'])
def create_movie():
    title = request.json['title']
    release_date = request.json['release_date']
    movie = Movie(title=title, release_date=release_date)
    db.session.add(movie)
    db.session.commit()
    return jsonify({'message': 'Movie created'}), 201

@bp.route('/subscriptions', methods=['POST'])
def create_subscription():
    user_id = request.json['user_id']
    movie_id = request.json['movie_id']
    
    subscription = Subscription(user_id=user_id, movie_id=movie_id)
    db.session.add(subscription)
    db.session.commit()
    return jsonify({'message': 'Subscription created'}), 201

@bp.route('/payments', methods=['POST'])
def create_payment():
    user_id = request.json['user_id']
    amount = request.json['amount']
    
    payment = Payment(user_id=user_id, amount=amount)
    db.session.add(payment)
    db.session.commit()
    return jsonify({'message': 'Payment created'}), 201