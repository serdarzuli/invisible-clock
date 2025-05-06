# 🧥 Invisible Cloak with OpenCV and Tkinter

A fun and interactive Python project that uses computer vision to create a real-time invisibility effect — just like in sci-fi movies! The user selects a cloak color, and everything in that color range is replaced with the background, making it look "invisible."

---

## 📁 Project Structure

```bash
invisible_cloak/
│
├── src/                       # Main application logic
│   ├── core.py                # Cloak processing logic
│   └── color_picker.py        # Choose color
│   └── ui.py                 # GUI using tkinter
│   
├── main.py                   # Entry point to launch the app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Features

- Real-time webcam capture using `cv2.VideoCapture`
- Select custom cloak color using a simple GUI (Tkinter)
- Automatically captures background and applies invisibility effect
- Morphological operations for smooth cloak mask
- Interactive UI to make it easy for anyone to use

---

## 🛠️ Technologies Used

| Tool / Library | Description                                 |
|----------------|---------------------------------------------|
| Python         | Core language                               |
| OpenCV         | Real-time image processing                  |
| Tkinter        | GUI for user interaction                    |
| NumPy          | Efficient numerical array operations        |
| Colorsys       | RGB to HSV color conversion                 |

---

## 🖥️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/serdarzuli/invisible_cloak.git
cd invisible_cloak
```

### 2. Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Launch the Application

```bash
python main.py
```

---

## 🧪 Run Tests (Optional)

```bash
python -m unittest tests/test_cloak.py
```

---

## 💡 Future Enhancements

- Add image/video saving feature
- Support for multiple color cloaks
- Face/hand tracking to mask selected objects instead of color

---

## 📄 License

MIT License - Feel free to use and modify this project for personal or educational purposes.