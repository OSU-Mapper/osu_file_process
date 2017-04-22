#

for path in $1/* ;do
    # echo "path:$path"
    csvpath="$path/feature-v1.csv"
    for osupath in "$path"/*.osu  ; do
        #echo "$osupath"
        # Put your code here
        # e.g. 
        # python blah-blah.py "$osupath" "$csvpath"
    done
done
