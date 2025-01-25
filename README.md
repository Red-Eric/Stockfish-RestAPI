# Stockfish REST API

A simple REST API built with Flask that uses the Stockfish chess engine to calculate the best move from a given FEN position.
Download the .exe in the official website : https://stockfishchess.org/

## Features

- Get the best move for a specific chess position using the Stockfish engine.
- Simple API with a POST endpoint to interact with Stockfish.
- CORS support to allow cross-domain requests.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## API Overview

The API provides an endpoint to evaluate chess positions and get the best moves. By sending a FEN string representing a chess position to the `/best` endpoint, the API returns:
- An evaluation score for the position.
- A list of the best 5 moves.
- A list of evaluation scores for each of the best moves.

## Endpoints

### POST /best

This endpoint evaluates the given FEN string and returns the best possible moves and their evaluation scores.

#### Request Body
The request body should be a JSON object containing the FEN string representing the chess position.

```json
{
  "fen": "your_fen_string_here"
}

