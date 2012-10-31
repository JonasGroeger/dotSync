#!/usr/bin/env python3.2
# coding: utf-8

from os import remove, symlink, path
from socket import gethostname
from filecmp import cmp

DOTFILES = ['.bash_aliases', '.bash_functions', '.bashrc', '.bash_ssh', '.gitconfig', '.hgrc', '.inputrc', '.minttyrc',
            '.pythonstartup', '.vimrc']
HOME = path.expanduser("~")

def createSymlinks(homeDirectory=None):
  # Select home directory
  if homeDirectory is None:
    homeDirectory = HOME

  # Nice confirmation with name and folder
  machine = gethostname()
  msg = 'Replace/create {0} dotfiles in {1} on this machine: {2} ?'

  if confirm(msg.format(str(len(DOTFILES)), homeDirectory, machine), True):
    replaced = 0
    created = 0

    for f in DOTFILES:
      # File in home directory
      homefile = path.join(homeDirectory, f)

      # File in vcs directory (git, hg, svn)
      sourcefile = path.abspath(f)
      replaced_file = False

      # Remove existing dotfiles
      if path.lexists(homefile):
        replaced_file = True
        remove(homefile)

      # Do the linking
      symlink(sourcefile, homefile)

      # Print some infos
      if replaced_file:
        print('Replaced ' + str(f) + ' in ' + str(homeDirectory))
        replaced += 1
      else:
        print('Created ' + str(f) + ' in ' + str(homeDirectory))
        created += 1

    print('Done. Created {0} and replaced {1} dotfiles.'.format(created, replaced))


def confirm(prompt=None, resp=False):
  """
  Querys the user for confirmation. Returns True for input "y" or "Y". Else False.
    prompt is the question you want to confirm.
    resp is the default answer that will be selected when just pressing enter.
  """
  if prompt is None:
    prompt = 'Confirm'

  if resp:
    prompt = '{0} [{1}]|{2}: '.format(prompt, 'y', 'n')
  else:
    prompt = '{0} [{1}]|{2}: '.format(prompt, 'n', 'y')

  while True:
    ans = input(prompt)
    if not ans:
      return resp
    if ans not in ['y', 'Y', 'n', 'N']:
      print('please enter y or n.')
      continue
    if ans == 'y' or ans == 'Y':
      return True
    if ans == 'n' or ans == 'N':
      return False

if __name__ == '__main__':
  createSymlinks(HOME)
