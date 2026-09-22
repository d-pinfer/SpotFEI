# 🎵 SpotFEI

SpotFEI is a terminal-based music platform developed in **Python** as an academic project at **Centro Universitário FEI**.

The application simulates core features of a music streaming platform, allowing users to create accounts, search for songs, manage playlists and keep a history of likes and dislikes.

## 🚀 Features

- User registration and login
- Music search
- Playlist creation and management
- Add and remove songs from playlists
- Rename and delete playlists
- Like and dislike songs
- User interaction history
- Local data persistence using text files

## 💻 Technologies and Concepts

- Python
- File handling
- Dictionaries and lists
- Functions and modularization
- String manipulation
- Input validation
- Control structures
- Algorithms and programming logic

## 📁 Project Structure

```text
SpotFEI/
├── main.py
├── musicas.txt
├── README.md
└── .gitignore
```

The application also uses local files for user-generated data:

- `cadastros.txt` — user accounts
- `historico.txt` — likes and dislikes
- `playlists.txt` — user playlists

These files are intentionally ignored by Git because they may contain personal or user-generated information.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/d-pinfer/SpotFEI.git
cd SpotFEI
```

### 2. Create the local data files

Before running the project for the first time, create these empty files in the project folder:

```text
cadastros.txt
historico.txt
playlists.txt
```

The music catalog is already included in `musicas.txt`.

### 3. Run the application

```bash
python main.py
```

or, depending on your environment:

```bash
python3 main.py
```

## 🧠 How It Works

SpotFEI uses menu-based interaction in the terminal. User information, playlists and interaction history are stored locally in text files, while `musicas.txt` acts as the application's music catalog.

The project was developed to practice fundamental programming concepts such as data validation, file reading and writing, structured text manipulation and decomposition of the program into functions.

## 🔒 Security Note

This is an academic project created for learning purposes. User data is stored locally in plain-text files and the authentication model is not intended for production use.

## 🎥 Demo

Watch a test/demo of the project on YouTube:

[▶️ SpotFEI — Project Demo](https://youtu.be/SxKgklxKK-c)

## 🎓 Academic Context

Project developed during the **Computer Science** program at **Centro Universitário FEI**.

## 👨‍💻 Author

**Davi Pinheiro Ferreira**
