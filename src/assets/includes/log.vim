" Vim syntax highlighting file for custom log format

if exists("b:current_syntax")
  finish
endif

syn match   log_error 	'\c.*\<\(FATAL\|ERROR\|ERRORS\|FAIL\|FAILED\|FAILURE\|UVM_ERROR\|UVM_FATAL\).*'
syn match   log_warning 	'\c.*\<\(WARNING\|DELETE\|DELETING\|DELETED\|RETRY\|RETRYING\|UVM_WARNING\).*'
syn match   log_success 	'\c.*\<\(PASS\|PASSED\|SUCCESS\|SUCCEEDED\|OK\|DONE\).*'
syn region  log_string 	start=/'/ end=/'/ end=/$/ skip=/\\./
syn region  log_string 	start=/"/ end=/"/ skip=/\\./
syn match   log_number 	'0x[0-9a-fA-F]*\|\[<[0-9a-f]\+>\]\|\<\d[0-9a-fA-F]*'
syn match   log_brackets display '\[\w\+\]'
syn match   log_date '\(Jan\|Feb\|Mar\|Apr\|May\|Jun\|Jul\|Aug\|Sep\|Oct\|Nov\|Dec\) [ 0-9]\d *'
syn match   log_date '\d\{4}-\d\d-\d\d'
syn match   log_time '\d\d:\d\d:\d\d\s*'
syn match   log_time '\c\d\d:\d\d:\d\d\(\.\d\+\)\=\([+-]\d\d:\d\d\|Z\)'
syn match   log_uvm_filepath  '[^a-zA-Z0-9"']\@<=\/\w[^\n|,; \(\)'"\]{}]\+(\d\+)\s@\s\d\+:'
syn match   log_uvm_hierarchy 'uvm_test_top\.[a-zA-Z._@\[\]0-9]\+'
syn keyword log_keyword  UVM_INFO UVM_DEBUG

hi def link log_string 		    String
hi def link log_number 		    Number
hi def link log_keyword		    Identifier
hi def link log_date 		      Constant
hi def link log_time 		      Type
hi def link log_success 	    DiffAdd
hi def link log_warning 	    WarningMsg
hi def link log_error 		    Error
hi def link log_uvm_filepath  Comment
hi def link log_uvm_hierarchy Comment
hi def link log_brackets      Define

let b:current_syntax = "log"