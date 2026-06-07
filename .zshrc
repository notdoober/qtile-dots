HISTFILE=~/.zsh_history
HISTSIZE=5000
SAVEHIST=5000
setopt appendhistory sharehistory incappendhistory

autoload -Uz compinit
compinit

zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$XDG_CACHE_HOME/zsh/zcompcache"

zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

zstyle ':completion:*' menu select

zstyle ':completion:*' list-colors "di=34:ln=35:so=32:pi=33:ex=31:bd=34;46:cd=34;43"

source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null


ZSH_AUTOSUGGEST_STRATEGY=(completion history)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#414868"

alias ff='fastfetch'

PS1="%K{#7aa2f7}%F{#1a1b26} :3 %~ %k%K{#414868}%F{#7aa2f7}%F{#c0caf5} ❯ %k%F{#414868}%f "

fastfetch
