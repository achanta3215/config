set rtp+=/usr/local/opt/fzf
syntax on
set relativenumber
set number

call plug#begin('~/.vim/plugged')

Plug 'christoomey/vim-tmux-navigator'
Plug 'diepm/vim-rest-console'

set tabstop=2
set shiftwidth=2
set expandtab

noremap Zz <c-w>_ \| <c-w>\|
noremap Zo <c-w>=

call plug#end()

command! -bang -nargs=* GGrep
  \ call fzf#vim#grep(
  \   'git grep --line-number '.shellescape(<q-args>), 0,
  \   fzf#vim#with_preview({'dir': systemlist('git rev-parse --show-toplevel')[0]}), <bang>0)

augroup filetypedetect
  au! BufRead,BufNewFile *.spec.js.snap      setfiletype snap
augroup END
