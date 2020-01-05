set rtp+=/usr/local/opt/fzf
syntax on
set relativenumber

call plug#begin('~/.vim/plugged')


Plug '/usr/local/opt/fzf'
Plug 'junegunn/fzf.vim'

call plug#end()

command! -bang -nargs=* GGrep
  \ call fzf#vim#grep(
  \   'git grep --line-number '.shellescape(<q-args>), 0,
  \   fzf#vim#with_preview({'dir': systemlist('git rev-parse --show-toplevel')[0]}), <bang>0)
