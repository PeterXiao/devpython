ls *.jpg | while read NAME
do
        mv $NAME ${NAME%\.jpg}.png
done