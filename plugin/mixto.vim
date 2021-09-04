let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

if !has("python3")
  echo "Vim has to be compiled with +python3 to run the mixto plugin"
  finish
endif

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python3'))
sys.path.insert(0, python_root_dir)
import mixto_vim
EOF

let s:mixto_entry_ids = []
python3 mixto_vim._get_ids()

function! Eids(arg, ...)
  return filter(s:mixto_entry_ids, 'v:val =~ "'.a:arg.'"')
endfunction

function! MixtoCommit(entryID)
  python3 mixto_vim.mixto_commit()
endfunction
command! -nargs=1 -complete=customlist,Eids MixtoCommit call MixtoCommit(<f-args>)
