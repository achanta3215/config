set shell=/bin/bash
set rtp+=/usr/local/opt/fzf
set relativenumber
set number
let vim_markdown_preview_github=1
let vim_markdown_preview_temp_file=1
let vim_markdown_preview_browser='Google Chrome'
let g:coc_global_extensions = [ 'coc-tsserver' ]

nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

call plug#begin('~/.vim/plugged')

Plug 'alvan/vim-closetag'
let g:closetag_filenames = '*.html,*.xhtml,*.xml,*.vue,*.phtml,*.js,*.jsx,*.coffee,*.erb'
Plug 'jiangmiao/auto-pairs'
Plug 'rakr/vim-one'

Plug 'christoomey/vim-tmux-navigator'
Plug 'diepm/vim-rest-console'
Plug 'andreshazard/vim-logreview'
Plug 'JamshedVesuna/vim-markdown-preview'
Plug 'pangloss/vim-javascript'    " JavaScript support
Plug 'leafgarland/typescript-vim' " TypeScript syntax
Plug 'maxmellon/vim-jsx-pretty'   " JS and JSX syntax
Plug 'jparise/vim-graphql'        " GraphQL syntax
Plug 'neoclide/coc.nvim' , { 'branch' : 'release' }

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
nnoremap <C-p> :Files<Cr>


nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

set tabstop=2
set shiftwidth=2
set expandtab

autocmd BufNewFile,BufRead *catalina.out set ft=logreview

noremap Zz <c-w>_ \| <c-w>\|
noremap Zo <c-w>=

call plug#end()
let g:airline_theme='one'
set background=dark
colorscheme one
set termguicolors


command! -bang -nargs=* GGrep
  \ call fzf#vim#grep(
  \   'git grep --line-number '.shellescape(<q-args>), 0,
  \   fzf#vim#with_preview({'dir': systemlist('git rev-parse --show-toplevel')[0]}), <bang>0)

augroup filetypedetect
  au! BufRead,BufNewFile *.spec.js.snap      setfiletype snap
augroup END
