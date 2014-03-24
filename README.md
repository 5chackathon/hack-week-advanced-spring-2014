# Hack Week Spring 2014 - Course Reviews

This application was designed for the advanced division of Hack Week. It is a
full-stack web application.

## Installation

Clone the repository to your local machine, or click the `Download ZIP` button
to the left to download the files and drag the folder to wherever you'd like.

### Mac & Linux

Macs come with Python installed. Most Linux distros do as well.
You can check by opening a terminal and executing `python --version`. Ensure
that you have Python version 2.x (i.e., not 3.x).

Open up a terminal (`Command+Spacebar` on Macs). Type

    sudo easy_install pip

Enter your password when prompted. Next navigate to the folder of the project
(you can type `cd`, drag the folder into the terminal, and press enter to go
there) and type the following

    sudo pip install -r requirements.txt

This will install all of the necessary packages to your computer. You're ready
to go!

### Windows

Windows does not come with Python, so there is a bit more installation involved.
There is a program called [Chocolatey] that will assist in the installation.
Type `Win+R` and type `cmd` to open a command prompt. Copy the following text,
and right click on the command prompt to paste the command. Press enter to
execute it.

```powershell
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin
```

If you get errors, you probably don't have PowerShell on your path.

If you already have Python installed, you can skip the next step. Please ensure
that you have a version 2.7. You can check this by typing `python --version`
into a command prompt.

To install the correct version of Python, type the following into a command
prompt:

    cinst python -Version 2.7.6

After installing Python, you need to install `pip`, the Python package manager.
Open a command prompt and type

    cinst easy.install
    cinst pip

Now, navigate to the folder where you stored the project. `Shift+Right Click` on
the folder to open an administrator command prompt, and type the following
command:

    pip install -r requirements.txt

This will install all of the packages necessary for the project to run to your
computer. You're ready to go!

## Running the App

Open a terminal or command prompt in the project root and run `python app.py`.
You should see some messages about the server starting on `localhost:5000`.
Open up a web browser, and enter `localhost:5000` in the address bar to view the
app.

[Chocolatey]: http://chocolatey.org
