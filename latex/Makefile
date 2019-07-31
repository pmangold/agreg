all:
	./latexify.sh
	-pdflatex -interaction nonstopmode final_file.txt
	-bibtex final_file.aux
	-pdflatex -interaction nonstopmode final_file.txt
	-pdflatex -interaction nonstopmode final_file.txt
	rm final_file.aux
	rm final_file.log
	rm final_file.toc
	rm final_file.out
	rm final_file.bbl
	rm final_file.blg
