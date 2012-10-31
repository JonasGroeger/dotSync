# dotSync

## Usage
To use this script, put any dotfiles (.bashrc and alike) in the same directory as the script.py. **Use a text editor to edit the files you want to sync.**

It should look somewhat like this:

    .
    ├── .bash_aliases
    ├── .bash_functions
    ├── .bashrc
    ├── .bash_ssh
    ├── .git
    ├── .gitconfig
    ├── .gitignore
    ├── .hgrc
    ├── .idea
    ├── .inputrc
    ├── .minttyrc
    ├── .pythonstartup
    └── .vimrc

Then, execute setup.py by:

    chmod +x setup.py
    ./setup.py

This will ask you for confirmation and then overwrite all specified dotfiles in the home directory "~".

## License
The script is licensed under [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/de/).