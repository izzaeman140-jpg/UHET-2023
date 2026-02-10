# UHET 2023 - Urdu Handwriting Education Tool

An Android/Desktop application for learning Arabic alphabet handwriting with stroke order validation using deep learning.

## Features

- **Handwriting Recognition**: Recognizes 10 Arabic/Urdu characters using a CNN model
- **Stroke Order Validation**: Real-time feedback on correct stroke sequences
- **Text-to-Speech**: Audio pronunciation of characters (desktop and Android)
- **Interactive Drawing Canvas**: Practice writing characters with immediate feedback
- **Character Reference**: Display random character images to practice

## Supported Characters

The app recognizes these 10 Arabic/Urdu characters:
- ع (Ain)
- ا (Alif)
- ب (Bay)
- د (Daal)
- ہ (Gol Haa)
- ح (Haa)
- ل (Laam)
- م (Meem)
- ن (Noon Ghuna)
- و (Wao)

## System Requirements

### Desktop (Windows/Linux)
- Python 3.7 or higher
- 4GB RAM minimum
- Windows 10+ or Ubuntu 18.04+

### Android
- Android 5.0 (Lollipop) or higher
- 100MB free storage
- ARM or ARM64 processor

## Installation

### Desktop Setup

1. **Clone or download the project**
```bash
cd "d:\UHET\UHET 2023\UHET 2023"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

### Android APK Installation

1. **Download the APK** from the `bin/` folder after building
2. **Enable "Install from Unknown Sources"** in Android settings
3. **Transfer APK** to your Android device
4. **Install** by tapping the APK file

## Building for Android

### Prerequisites
- Docker (for containerized build environment)
- 10GB free disk space for build tools

### Build Steps

1. **Ensure Docker is running**

2. **Build using Buildozer** (via Docker for consistent environment):

```bash
# Using Docker (recommended)
docker run --rm -v "d:\UHET\UHET 2023\UHET 2023":/app kivy/buildozer buildozer android debug

# Or directly with Buildozer (if installed on Linux)
buildozer android debug
```

3. **Find the APK**
```
output location: bin/uhet2023-0.1-arm64-v8a_armeabi-v7a-debug.apk
```

## Usage

### Desktop Application

1. **Launch the app**: Run `python main.py`
2. **Main Screen**: Click "Draw" to start practicing
3. **Drawing Screen**:
   - Draw a character with your mouse/touchpad
   - Click "Check Stroke Order" to validate
   - Click "Clear" to reset the canvas
   - Click "Dictate the Alphabets" to see a random character
   - Click "Back" to return to main menu

### Android Application

1. Launch the app from your device
2. Same interface as desktop
3. Use your finger to draw characters on the touchscreen

## Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: 128x128 grayscale images
- **Output**: 10 character classes
- **Desktop Model**: `modelchar.hdf5` (TensorFlow/Keras)
- **Android Model**: `modelchar.tflite` (TensorFlow Lite)
- **Accuracy**: Trained on custom Arabic handwriting dataset

## Project Structure

```
UHET 2023/
├── main.py                    # Main application entry point
├── app.kv                     # Kivy UI definition
├── buildozer.spec             # Android build configuration
├── requirements.txt           # Python dependencies
├── modelchar.hdf5             # TensorFlow model (desktop)
├── modelchar.tflite           # TFLite model (Android)
├── cnn_new.py                 # Model training script
├── generate_characters.py     # Character image generator
├── characters/                # Reference character images
│   ├── ain.jpg
│   ├── alif.jpg
│   └── ... (10 total)
├── logo.jpg                   # App logo
└── Alphabets (1).png          # Main screen image
```

## Training Your Own Model

If you want to retrain the model with your own dataset:

1. **Prepare training data**:
   - Create folder structure: `i_data/character_name/`
   - Add handwriting samples (images) for each character
   - Update label ranges in `cnn_new.py` (lines 75-84)

2. **Train the model**:
```bash
python cnn_new.py
```

3. **Convert to TFLite** (for Android):
```bash
python convert_tf_to_tflite.py
```

## Dependencies

### Desktop
- kivy - UI framework
- tensorflow - Deep learning
- opencv-python - Image processing
- numpy - Array operations
- pyttsx3 - Text-to-speech (Windows)
- Pillow - Image handling

### Android
- kivy - UI framework
- tflite-runtime - Lightweight TensorFlow
- opencv - Image processing
- numpy - Array operations
- plyer - Platform-specific features (TTS)

## Troubleshooting

### Desktop Issues

**Problem**: `ModuleNotFoundError`
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

**Problem**: App crashes on launch
```bash
# Solution: Check Python version
python --version  # Should be 3.7+
```

### Android Build Issues

**Problem**: Build fails with NDK error
```bash
# Solution: Clean build and retry
buildozer android clean
buildozer android debug
```

**Problem**: APK won't install
- Enable "Unknown Sources" in Android settings
- Check minimum Android version (5.0+)
- Ensure sufficient storage space

## License

Educational project for Urdu handwriting education.

## Contributing

This is an educational project. Feel free to:
- Report issues
- Suggest improvements
- Add more characters
- Improve the model accuracy

## Credits

- Developed for UHET 2023
- CNN model trained on custom Urdu/Arabic handwriting dataset
- Built with Kivy framework and TensorFlow

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review buildozer build logs in `build_current.log`
3. Ensure all dependencies are properly installed

---

**Version**: 0.1  
**Last Updated**: February 2026
