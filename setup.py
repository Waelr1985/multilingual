from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.1",
    author="waelr1985",
<<<<<<< HEAD
    author_email="waelr1985@gmail.com",
=======
    author_email="waelr1985@ineuron.ai",
>>>>>>> c8e0ca39ed581800037ff33b8874953f0d54975a
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)