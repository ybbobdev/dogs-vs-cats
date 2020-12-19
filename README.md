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
```

 - [Miniconda3 MacOSX 64-bit pkg](https://docs.conda.io/en/latest/miniconda.html)
 - https://www.kaggle.com/c/dogs-vs-cats/data


