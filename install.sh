# Create the binary file.
pyinstaller --onefile dark_souls_boss.py

# Copy the binary into /usr/local/bin (sudo needed).
sudo cp dist/dark_souls_boss /usr/local/bin/dark_souls_boss
