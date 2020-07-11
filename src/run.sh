FILE=dataset.csv
if [ -f "$FILE" ]; then
    echo "Downloaded $FILE Already"
else 
    wget https://gist.githubusercontent.com/ucalyptus/5ea2c461d2949e2fe3235fd9406a9479/raw/e377e68091c55ba3cee496b49337d56e6801a502/dataset.csv
fi
python3 src/trainmodel.py
python3 src/sanitize.py
python3 src/pred.py
python3 src/getpredout.py
