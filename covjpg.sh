
cat list| while read line  
do
   $lines='sed 's/[ ]*$//' $lines'
   #convert -quality 90% $line $line-resized;
    echo $lines-backup
   #echo $line  $line-backup
   #echo $line-resized $line
   #echo $line
done
