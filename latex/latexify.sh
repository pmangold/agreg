cat header.txt > final_file.txt
python3 gen_latex.py > temp.txt
cat developpements.txt >> final_file.txt
cat couplages.txt >> final_file.txt
cat temp.txt >> final_file.txt
cat footer.txt >> final_file.txt
rm temp.txt
