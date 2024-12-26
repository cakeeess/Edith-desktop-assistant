#Edith: Text/Voice-Based Desktop Assistant#
Edith is a Python-based desktop assistant that leverages text and voice commands to perform various tasks such as web browsing, opening applications, checking the time, sending emails, and more. With a simple GUI and voice recognition capabilities, Edith makes it easy to interact with your system.

Features
Voice Recognition: Execute commands using natural speech.
Text Commands: Perform tasks via a text-based input GUI.
Task Execution:
Open common applications (e.g., Notepad, Calculator).
Search the web using Google.
Retrieve summaries from Wikipedia.
Open popular websites like YouTube and Stack Overflow.
Send emails.
Display the current time.
Operate the system's camera.
Responsive Interaction: Edith greets users based on the time of day and provides feedback for commands.
Simple GUI: A user-friendly interface built with Tkinter.
Requirements
Python 3.7+
Required Python libraries:
tkinter
pyttsx3
speech_recognition
wikipedia
opencv-python
datetime
smtplib
webbrowser
os
Install dependencies using pip:

bash
Copy code
pip install pyttsx3 speechrecognition wikipedia opencv-python
How to Use
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/edith-desktop-assistant.git
cd edith-desktop-assistant
Run the Script: Execute the main script to launch Edith:

bash
Copy code
python edith.py
Interact with Edith:

Use the GUI to type commands or speak into the microphone for voice commands.
Examples:
"Open Notepad"
"Search Python programming on Google"
"What's the time?"
Quit the Application: Click the Quit button in the GUI or say "Exit" to terminate the program.

Demo
Edith GUI:
A simple GUI with buttons for text and voice command execution, and a text area to display interactions.

File Structure
bash
Copy code
edith-desktop-assistant/
├── edith.py         # Main script to run the assistant
├── README.md        # Documentation
Important Notes
Email Sending:

Update the email credentials in the sendEmail function with your own email and app password.
Ensure that "Allow less secure apps" is enabled for your email account if using Gmail (not recommended for security).
Privacy:

Be cautious when providing sensitive commands or using Edith in public spaces.
Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance Edith's functionality.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you'd like any adjustments to the README
