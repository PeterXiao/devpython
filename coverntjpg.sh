cat convertlist|while read line; do
                #convert -quality 90% $line $line-resized;
                echo $line  $line-backup;
                echo $line-resized $line
                echo $line
done