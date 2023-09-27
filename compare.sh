wc_man=$(man man | wc -l)
wc_ls=$(man ls | wc -l)
wc_find=$(man find | wc -l)

echo "man, "$wc_man" lines" >> result.sh
echo "ls, "$wc_ls" lines" >> result.sh
echo "find, "$wc_find" lines" >> result.sh

cat result.sh | sort -g -k 2 -r -t ,

rm result.sh
