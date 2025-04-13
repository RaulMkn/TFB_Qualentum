#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=postgresql://maken:Yukio2025@127.0.0.1:1234/tfb_database python3 manage.py
