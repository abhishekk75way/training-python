# Python Training

This repository contains Python training exercises used for learning and experimentation.

## Project Structure

- `python/`: Directory containing Python Documentation.
- `learn/`: Directory containing learning scripts.
  - `basics/`: Directory containing basic scripts.
  - `projects/`: Directory containing project scripts.
- `test/`: Directory containing test scripts.
  - `main.py`: A basic Python script that demonstrates a simple output.

## How to Run

You can run the main script using Python:

```bash
python learn/basics/main.py or learn/basics/addition.py
python test/main.py
```

## Environment Setup Guide

Follow these steps to set up your development environment.

### 1. Setup

- **Python**: Installed Python 3.14
  - Verification: `python3 --version`
- **VS Code Extension**: Installed the "Python" extension for VS Code.
- **Pip**: Ensure `pip` is installed.
  - Verification: `pip3 --version`

- **Python Commands Execution - Output**:

```bash
python --version
pip --version

Python 3.14.2
pip 25.3 from /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip (python 3.14)
```

### 2. Virtual Environments & Version Management

- **Pyenv**: Recommended for managing multiple Python versions.
  - Install via Homebrew: `brew install pyenv`
  - Install a version: `pyenv install 3.14.2`
  - Set global/local version: `pyenv global 3.14.2`
- **Virtual Environments (venv)**: Always use a virtual environment for projects to avoid dependency conflicts.
  - Create: `python3 -m venv venv`
  - Activate: `source venv/bin/activate`
  - Deactivate: `deactivate`
  - Verification: `which python` should point to the `venv` directory.

- **Pyenv Commands Execution - Output**:

```bash
brew install pyenv pyenv install 3.13 pyenv global 3.14.2

==> Auto-updating Homebrew...
Adjust how often this is run with `$HOMEBREW_AUTO_UPDATE_SECS` or disable with
`$HOMEBREW_NO_AUTO_UPDATE=1`. Hide these hints with `$HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/cask).
==> New Casks
glide: Tiling window manager with tree layouts
novation-play: Virtual instrument for Novation Launchkey MK4 hardware

You have 3 outdated formulae installed.

Warning: No available formula with the name "install". Did you mean instead?
==> Searching for similarly named formulae and casks...
==> Formulae
aqtinstall            cargo-binstall        fabric-installer      install-nothing       pyinstaller           ruby-install          instead
cabal-install         custom-install        ideviceinstaller      install-peerdeps      quilt-installer       zero-install

To install aqtinstall, run:
  brew install aqtinstall

==> Casks
betterdiscord-installer               install-disk-creator                  minstaller                            uninstallpkg
eclipse-installer                     kilohearts-installer                  ubports-installer                     zxpinstaller

```

- **Virtual Environment(Venv) Commands Execution - Output**:

```bash
75way-67@75WAY-67s-Mac-mini % python -m venv venv     
75way-67@75WAY-67s-Mac-mini % source venv/bin/activate
(venv) 75way-67@75WAY-67s-Mac-mini % which python            
python: aliased to python3
(venv) 75way-67@75WAY-67s-Mac-mini % which python3
/Users/75way-67/Desktop/training-python/learn/basics/venv/bin/python3
(venv) 75way-67@75WAY-67s-Mac-mini % deactivate
```

### 3. Dependency Management

- **Install Dependencies**: Use `pip` inside your virtual environment.
  - Example: `pip install requests`
- **Requirements File**: Track dependencies in `requirements.txt`.
  - Freeze current deps: `pip freeze > requirements.txt`
  - Install from file: `pip install -r requirements.txt`
- **Important**: Never use the global `pip` for project dependencies.

- **Dependency Commands Execution – Output**:

```bash
(venv) 75way-67@75WAY-67s-Mac-mini projects % pip install requests     
Collecting requests
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.4-cp314-cp314-macosx_10_13_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.4-cp314-cp314-macosx_10_13_universal2.whl (207 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
Successfully installed certifi-2026.1.4 charset_normalizer-3.4.4 idna-3.11 requests-2.32.5 urllib3-2.6.3

(venv) 75way-67@75WAY-67s-Mac-mini projects % pip freeze > requirements.txt

(venv) 75way-67@75WAY-67s-Mac-mini projects % cat requirements.txt
certifi==2026.1.4
charset-normalizer==3.4.4
idna==3.11
python-dotenv==1.2.1
requests==2.32.5
urllib3==2.6.3

(venv) 75way-67@75WAY-67s-Mac-mini projects % pip install -r requirements.txt
Requirement already satisfied: certifi==2026.1.4 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 1)) (2026.1.4)
Requirement already satisfied: charset-normalizer==3.4.4 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 2)) (3.4.4)
Requirement already satisfied: idna==3.11 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 3)) (3.11)
Requirement already satisfied: python-dotenv==1.2.1 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 4)) (1.2.1)
Requirement already satisfied: requests==2.32.5 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 5)) (2.32.5)
Requirement already satisfied: urllib3==2.6.3 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 6)) (2.6.3)
```

### 4. Configuration & Secrets

- **Environment Variables**: Use `.env` files for secrets (DB credentials).
  - Library: `python-dotenv`
  - Usage:

    ```python
    from dotenv import load_dotenv
    import os
    load_dotenv()
    db_conn = os.getenv("DB_CONNECTION")
    print(db_conn)
    ```

  - Create `.env` file in the projects directory of your project.

    ```bash
    DB_CONNECTION=mysql://root:root@localhost:3306/mydb
    ```

- **Environment & dotenv Commands Execution – Output**:

```bash
75way-67@75WAY-67s-Mac-mini projects % python -m venv venv     
75way-67@75WAY-67s-Mac-mini projects % source venv/bin/activate

(venv) 75way-67@75WAY-67s-Mac-mini projects % pip install python-dotenv
Collecting python-dotenv
  Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.2.1

(venv) 75way-67@75WAY-67s-Mac-mini projects % python main.py           
mysql://root:root@localhost:3306/mydb
```

- **Security**: Never commit `.env` files to version control. Add `.env` to your `.gitignore`.
