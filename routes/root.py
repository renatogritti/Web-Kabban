from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from dotenv import load_dotenv

from app import *
from models.db import *

load_dotenv()

def init_app(app):
    @app.route('/')
    def index():
        """Render the login page"""
        return render_template('login.html')

    @app.route('/validate_login', methods=['POST'])
    def validate_login():
        """Validate login credentials"""
        data = request.json
        if (data['username'] == os.getenv('ADMIN_USER') and 
            data['password'] == os.getenv('ADMIN_PASSWORD')):
            return jsonify({"success": True})
        return jsonify({"success": False, "message": "Usuário ou senha inválidos"})

    @app.route('/kanban')
    def kanban():
        """Render the main Kanban board page."""
        cards = [card.to_dict() for card in KanbanCard.query.all()]
        teams = [team.to_dict() for team in Team.query.all()]
        tags = [tag.to_dict() for tag in Tag.query.all()]
        projects = [project.to_dict() for project in Project.query.all()]
        
        return render_template('kanban.html', cards=cards, teams=teams, tags=tags, projects=projects)

    @app.route('/projects')
    def projects():
        """Render the projects management page."""
        projects = Project.query.all()
        return render_template('projects.html', projects=projects)

    @app.route('/teams')
    def teams():
        """Render the teams management page."""
        teams = Team.query.all()
        return render_template('teams.html', teams=teams)

    @app.route('/tags')
    def tags():
        """Render the tags management page."""
        tags = Tag.query.all()
        return render_template('tags.html', tags=tags)

    @app.route('/share')
    def share():
        """Render the share management page."""
        return render_template('share.html')

