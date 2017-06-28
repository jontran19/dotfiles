# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Pull in git tab completion
if [ -f ~/bash_completions/.git-completion.bash ]; then
    . ~/bash_completions/.git-completion.bash
fi

# Pull in docker tab completion
if [ -f ~/bash_completions/.docker-completion.bash ]; then
    . ~/bash_completions/.docker-completion.bash
fi

# Pull in kubernetes tab completion
if [ -f ~/bash_completions/kubectl ]; then
    . ~/bash_completions/kubectl
fi

#export TERM='xterm-256color'
shopt -s histappend
export HISTTIMEFORMAT="[%Y/%m/%d %T] "
export HISTFILESIZE=1000000
export HISTSIZE=100000
export HISTIGNORE=ls:h:lt:l:d:..:[1-9]:1[0-4]
# Avoid duplicates
export HISTCONTROL=ignoredups:erasedups  
shopt -s cmdhist
VIRTUAL_ENV_DISABLE_PROMPT=1
source $HOME/venv/bin/activate
source $HOME/mdp_profile

# When the shell exits, append to the history file instead of overwriting it

# After each command, append to the history file and reread it
export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"
# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
alias em='emacsclient -nw'
alias feh='find -name .#*'

if [ -f ~/bash_completions/.git-prompt.sh ]; then
    source ~/bash_completions/.git-prompt.sh
    PS1='\[\e[1;33m\]\u@\h\[\e[1;36m\] \w ->\n\[\e[1;32m\]\t\[\e[1;31m\] \!\[\e[1;34m\] ($(__git_ps1 "%s")) \$\[\e[m\] '
else
    PS1='\[\e[1;34m\]\u@\h\[\e[1;36m\] \w ->\n\[\e[1;32m\]\t\[\e[1;31m\] \!\[\e[1;34m\] \$\[\e[m\] '
fi

function gg()
{
    if test x$* = x ; then
        echo "gg - grep recursive for string in files at or below cwd"
        echo "Usage:"
        echo "        gg string"
    else
        find . -type f -exec grep $1 {} /dev/null \;
    fi
}

