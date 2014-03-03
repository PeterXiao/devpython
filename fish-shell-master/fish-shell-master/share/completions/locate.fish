# Completions for locate
# Author SanskritFritz (gmail)

complete -c locate -s A -l 'all'          -d 'Match all non-option arguments'
complete -c locate -s b -l 'basename'     -d 'Match against the base name of the file'
complete -c locate -s c -l 'count'        -d 'Print only the number of matches found'
complete -c locate -s d -l 'database' -r  -d 'Use different DATABASE file[s]'
complete -c locate -s e -l 'existing'     -d 'Match only existing files'
complete -c locate -s L -l 'follow'       -d 'Consider broken symbolic links to be non-existing files'
complete -c locate -s P -l 'nofollow'     -d 'Treat broken symbolic links as if they were existing'
complete -c locate -s H -l 'nofollow'     -d 'Treat broken symbolic links as if they were existing'
complete -c locate -s i -l 'ignore-case'  -d 'Ignore case distinctions'
complete -c locate -s l -l 'limit' -r     -d 'Limit  the number of matches'
complete -c locate -s 0 -l 'null'         -d 'Use ASCII NUL as a separator'
complete -c locate -s S -l 'statistics'   -d 'Print statistics about databases and exit'
complete -c locate -s w -l 'wholename'    -d 'Match against the whole name of the file'
complete -c locate -s r -l 'regex'        -d 'The pattern is a regular expression'
complete -c locate -s h -l 'help'         -d 'Print a summary of the options and exit'
complete -c locate -s V -l 'version'      -d 'Print the version number and exit'
