# FootballGraphDB

Comparative analysis of football data using relational (PostgreSQL) and graph (Neo4j) databases, with Python integration for visualization and API endpoints.

## Overview

FootballGraphDB is a project that compares two database approaches for managing complex football data. The project involves:
- **Data Modeling & Import:** Cleaning and transforming a football dataset from Kaggle, importing it into PostgreSQL, and exporting it to Neo4j.
- **Query Analysis:** Developing and analyzing complex SQL and Cypher queries to compare performance and execution plans.
- **Graph Analytics:** Leveraging Neo4j’s Graph Data Science Library with algorithms such as PageRank and Louvain to identify key nodes and communities.
- **Python Integration:** Using a Jupyter Notebook for interactive visualizations and a Flask application to expose REST endpoints for triggering graph algorithms.

## Dataset

The dataset used in this project is available on Kaggle:  
[Football Dataset](https://www.kaggle.com/datasets/davidcariboo/player-scores/data)

## Repository Structure

- **app.py** — Flask application for REST endpoints  
- **script_clubs.py** — Python script handling club-related operations  
- **script_transfers.py** — Python script handling transfer-related operations  
- **script_games.py** — Python script handling game-related operations  
- **script_players.py** — Python script handling player-related operations  
- **cypher.cyp** — Cypher scripts for Neo4j data import and queries  
- **tables.sql** — SQL script for PostgreSQL table creation and data import  
- **neo4j_demo.ipynb** — Jupyter Notebook for interactive analysis and visualizations

## Prerequisites

- **Neo4j:** An instance configured for importing and analyzing graph data.
- **PostgreSQL:** A relational database system for initial data import.
- **Python 3.x:** With libraries such as Flask, neo4j-driver, pandas, and matplotlib.

## Flask Application:
Start the Flask mini-server to access REST endpoints.
```bash
python app.py
```