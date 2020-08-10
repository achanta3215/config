# config
Shareable Configuration - Vim, Spacemacs, fish shell

Automatized Common utility tools to be made available to terminal by simply running a script to add to bash_profile.

Objective: To add more tools incrementally, and to get a common set-up across systems, by simply running a script.

**VIM**
Run :PlugInstall to update plugins

**Fish**
Initial Setup:
`curl https://git.io/fisher --create-dirs -sLo ~/.config/fish/functions/fisher.fish`
Symlink creation for fish config `ln -s ~/dev/config/config.fish ~/.config/fish/config.fish`

**TMUX**
Symlink creation for TMUX configuration: `ln -s ~/dev/config/.tmux.conf ~/.tmux.conf`

**Brew**
Prerequisite packages:
`brew install reattach-to-user-namespace`
