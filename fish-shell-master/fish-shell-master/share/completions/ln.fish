# Completions for ln
# Author: SanskritFritz (gmail)

complete -c ln -f -s s -l symbolic                   -d 'Make symbolic links instead of hard links'
complete -c ln -f      -l backup -a "none off numbered t existing nil simple never" -d 'Make a backup of each existing destination file'
complete -c ln -f -s b                               -d 'Make a backup of each existing destination file'
complete -c ln -f -s d -l directory                  -d 'Allow superuser to attempt to hard link directories'
complete -c ln -f -s f -l force                      -d 'Remove existing destination files'
complete -c ln -f -s i -l interactive                -d 'Prompt whether to remove destinations'
complete -c ln -f -s L -l logical                    -d 'Dereference TARGETs that are symbolic links'
complete -c ln -f -s n -l no-dereference             -d 'Treat symlink to directory as if it were a file'
complete -c ln -f -s P -l physical                   -d 'Make hard links directly to symbolic links'
complete -c ln -f -s S -l suffix                     -d 'Override the usual ~ backup suffix'
complete -c ln -f -s t -l target-directory -a '(__fish_complete_directories)' -d 'Specify the DIRECTORY in which to create the links'
complete -c ln -f -s T -l no-target-directory        -d 'Treat LINK_NAME as a normal file'
complete -c ln -f -s v -l verbose                    -d 'Print name of each linked file'
complete -c ln -f      -l help                       -d 'Display help and exit'
complete -c ln -f      -l version                    -d 'Output version information and exit'
