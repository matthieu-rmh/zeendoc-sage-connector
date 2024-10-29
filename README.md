### Setup the .asdf tool version manager to ensure correct python version
#### (Currently 3.13)
```sh
#make sure .git is installed first then clone the .asdf repository
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.1
#if you use bash, append this to the end of your .bashrc
. "$HOME/.asdf/asdf.sh"
#restart shell
bash

#Setup isolated python version
asdf plugin add python
asdf install
asdf local python 3.13.0

#activate python env
source py_env/bin/activate
```

### Install python dependencies

```sh
pip install -r requirements.txt
```
### Run the script

```sh
python src/main.py
```
### To run the tests
```sh
python test/{test_file.py} #eg: test_sage_api_calls.py
```
