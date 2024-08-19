# Dark Souls Bosses program.
This program just prints on stdout a randomly Dark Souls boss.

The program is loaded with Dark Souls 1, 2 & 3 bosses.

The user can set the quantity of bosses the program will print.

## Installation:
You can just call **install.sh** script or follow the next commands.


To compile the program just execute the following command:
```shell
pyinstaller --onefile dark_souls_boss.py
```
In linux, move the bin file created using this command (sudo needed).
```shell
sudo cp dist/dark_souls_boss /usr/local/bin/dark_souls_boss
```
