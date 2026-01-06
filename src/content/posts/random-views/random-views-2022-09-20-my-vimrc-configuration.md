---
author: glenzac
categories:
  - "random-views"
date: "2022-09-20T14:22:51+00:00"
draft: "true"

title: My .vimrc configuration
---
```
" Disable compatibility with vi which can cause unexpected issues
set nocompatible
"============================================================================="
"                              Themes
"============================================================================="
" Molokai Theme "
"let g:molokai_original = 1
"colorscheme molokai

" PaperColor Theme "
"set background=dark
set background=light
colorscheme PaperColor

" Enable the built-in matchit plugin
runtime macros/matchit.vim
" Enable type file detection. Vim will be able to try to detect the type of file in use.
filetype on
" Enable plugins and load plugin for the detected file type.
filetype plugin on
" Load an indent file for the detected file type.
filetype indent on
"============================================================================="
"                        Custom Key Bindings
"============================================================================="
" Set comma as the <Leader>
:let mapleader = ","
" Remaps Esc to ,, in insert mode
inoremap <Leader>, <Esc>
" Use Space while in normal mode to enter commands
nnoremap <Space> :
" Insert Disclaimer placed at ~/file_header.txt
nnoremap <Leader>fh ggi<CR><Esc>k:r~/file_header.txt<CR> kdd
" File saving
nnoremap <Leader>s :w<CR>
" Open netrw
nnoremap <Leader>e :Ex<CR>
" Go to file under cursor in vsplit mode
nnoremap <Leader>gf <C-W>vgf
" Quit vim
nnoremap <Leader>q :q<CR>
" Create a new tab
nnoremap <Leader>n :tabnew<CR>
" Turn on syntax highlighting
nnoremap <Leader>son :syntax on<CR>
" Turn off syntax highlighting
nnoremap <Leader>sof :syntax off<CR>
" Copy from cursor to line end
nnoremap <Leader>y y$
" Copy all the lines
nnoremap <Leader>ya :%y+<CR>
" Select all lines
nnoremap <Leader>sa ggVG<CR>
" Delete all the lines
nnoremap <Leader>da :%d<CR>
" Delete selection into blackhole register
nnoremap <Leader>d "_d
" Reload .vimrc
nnoremap <Leader>v :source<Space>~/.vimrc<CR>
" Ripgrep for searching through directory
nnoremap <Leader>r :Rg<Space>
" Display selected lines in reg/clipboard
nnoremap <Leader>c :reg "" 0 1 2 3 * +<CR>
" Open fzf window showing files
nnoremap <silent> <Leader>f :Files<CR>
" Open fzf window for files in git
nnoremap <silent> <Leader>g :GFiles<CR>
" Open fzf window to search through help
nnoremap <silent> <Leader>h :Helptags<CR>
" View current key mappings
nnoremap <silent> <Leader>m :Maps<CR>
" Open fzf window to search through lines in file
nnoremap <silent> <Leader>l :Lines<CR>
" Open fzf window to search through all the commits
nnoremap <silent> <Leader>gc :Commits<CR>
" Show all the highlight groups
nnoremap <Leader>hg :so<Space>$VIMRUNTIME/syntax/hitest.vim<CR>

"============================================================================="
"                          Autocompletion
"============================================================================="
" Automatically add closing ( { [ ' " `
inoremap { {}<ESC>i
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap " ""<ESC>i
inoremap ' ''<ESC>i

" Custom implementation of Tab for autocompletion
function! SmartTab()
    " if its the beginning of a line insert a literal tab
    let col = col('.') - 1
    let before_cursor = getline('.')[:col('.')-2]
    let char = strcharpart(before_cursor, strchars(before_cursor)-1)

    if !col
        return "\<tab>"
    else
        if char =~ '\s$'
	        return "\<Tab>"
	    else
	        return "\<C-N>"
        endif
	endif
endfunction

inoremap <Tab> <C-R>=SmartTab()<CR>
inoremap <C-Tab> <C-X><C-L>

" File completion similar to bash
set wildmode=longest,list,full
set wildmenu

"============================================================================="
"                              Configuration
"============================================================================="
" Turns syntax highlighting on
syntax on
" Set the max. number of tabs that can be opened simultaneously
set tabpagemax=50
" Set required font and size
set guifont=Bitstream\ Vera\ Sans\ Mono\ 17
" Shows line numbers
set number
" Wrap really long lines
set wrap
" Highlight cursor line underneath the cursor horizontally.
set cursorline

" Indentation settings
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

" Apply indentation to wrapped lines
set breakindent
" Adds 4 spaces before wrapped lines
set showbreak=\ \ \ \

" Display only the filename and modification status on tabs
:set guitablabel=%t\ %M
" Autowrap comments and allow formatting of comments using gq
set formatoptions=cq

" make searches case-sensitive only if they contain upper-case characters
set ignorecase
set smartcase

" Show the current mode on the last line.
set showmode

" Perform incremental search
set incsearch

" Highlight search string
set hlsearch

" Set indent based folding for files
set foldmethod=indent
" only fold at the highest level
set foldnestmax=1
" Initially open a file unfolded
set nofoldenable

" Backspace key works in all cases
set backspace=indent,eol,start

" Display .svh files with .sv syntax highlighting
au BufRead,BufNewFile *.svh set filetype=systemverilog

" Display .f files with .pl syntax highlighting
au BufRead,BufNewFile *.f set filetype=tcl

" Display .cfg files with YAML syntax highlighting
au BufRead,BufNewFile *.cfg set filetype=yaml
"autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

" Display .log files with special syntax highlighting
au BufRead,BufNewFile *.log set filetype=log wrap linebreak breakat=@

" Display .gzdoc files with special syntax highlighting
au BufRead,BufNewFile *.gzdoc set filetype=gzdoc wrap linebreak breakat=@

" Highlight the following keywords
if has("autocmd")
  " Highlight TODO, FIXME, NOTE, etc.
  if v:version > 701
    autocmd Syntax * call matchadd('DiffAdd',  '\W\zs\(TODO\|FIXME\|CHANGED\|HACK\)')
    autocmd Syntax * call matchadd('DiffChange', '\W\zs\(NOTE\|VERIFY\|REFER\)')
    autocmd Syntax * call matchadd('ErrorMsg', '\W\zs\(BUG\)')
  endif
endif

"============================================================================="
"                      Status line modifications
"============================================================================="
" To always enable the vim status line
set laststatus=2

" Building a custom status line
set statusline=
" Highlight to be used
set statusline+=%#MatchParen#
" Show line number with min. width for 3 digits
set statusline+=\ %3l\
" Highlight to be used
set statusline+=%#StatusLineTerm#
" Show the full path and filename
set statusline+=\ %f\
" Highlight to be used
set statusline+=%#DiffDelete#
" Show modification status
set statusline+=%m\
" Show read-only status
set statusline+=%r\
set statusline+=%h\
set statusline+=%w\
" Separation point between left and right aligned items
set statusline+=%=
" Highlight to be used
set statusline+=%#StatusLineNC#
" Show detected file type
set statusline+=\ %Y\
" Highlight to be used
set statusline+=%#DiffAdd#
" Show file encoding
set statusline+=\ %{&fileencoding?&fileencoding:&encoding}
set statusline+=\[%{&fileformat}\]\
" Highlight to be used
set statusline+=%#StatusLine#
" Shows current_line/total line
set statusline+=\ Line:\ %3l/%3L\
" Shows column number
set statusline+=\|\ Column:%3c\
set statusline+=\
" Get file sizes using FileSize function
set statusline+=%{FileSize(line2byte('$')+len(getline('$')))}

function! FileSize(bytes)
  let l:bytes = a:bytes | let l:sizes = ['B', 'KB', 'MB', 'GB'] | let l:i = 0
  while l:bytes >= 1024 | let l:bytes = l:bytes / 1024.0 | let l:i += 1 | endwhile
  return l:bytes > 0 ? printf(' %.1f%s ', l:bytes, l:sizes[l:i]) : ''
endfunction

"============================================================================="
"                            netrw configuration
"============================================================================="

" Make the default netrw to work in tree liststyle
" modes: thin, long, wide, tree
"let g:netrw_liststyle = 0

" To remove the netrw top banner
"let g:netrw_banner = 0

" To open the files in the previous window
"let g:netrw_browse_split = 4

" Keeps netrw open on the left side and the file on the right side
"let g:netrw_altv = 1

" Keep the split window size to only 30% of the window
"let g:netrw_winsize = 30

"============================================================================="
"                           Plugin Configuration
"============================================================================="

"Ultisnips config
"runtime path for ultinips plugin
set runtimepath+=~/.vim/plugin/ultisnips
"Set ultisnips triggers and for moving between placeholders
let g:UltiSnipsExpandTrigger="<C-B>"
let g:UltiSnipsJumpForwardTrigger="<C-B>"
let g:UltiSnipsJumpBackwardTrigger="<S-Tab>"
let g:UltiSnipsListSnippets="<S-Tab>"
"folder to look for snippets
let g:UltiSnipsSnippetDirectories=['~/.vim/plugin/ultisnips/UltiSnips']
"set the folder to look for snippets when UltiSnipsEdit is called
let g:UltiSnipsSnippetStorageDirectoryForUltiSnipsEdit = ['~/.vim/plugin/ultisnips/snippets', 'snippets']

```
