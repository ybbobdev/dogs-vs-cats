env setup
```
# install pyenv if you don't have it already
brew update && brew install pyenv
pyenv install 3.7.0

# set global default version of python
pyenv global 3.7.0

# Add for `~/.zshrc` set pyenv path for all sessions
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

# verify with 
pyenv version
# 3.7.0
python --version
# 3.7.0

# install miniconda to applications

# deps
pip install numpy
pip install opencv-python

# download Kaggle data and put contents in the root of this repo

```

links
 - [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg)
 - [Kaggle data](https://www.kaggle.com/c/dogs-vs-cats/data)
 - [Tutorial](https://www.youtube.com/watch?v=FLf5qmSOkwU&ab_channel=BalajiSrinivasan)

