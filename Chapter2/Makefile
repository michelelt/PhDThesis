#Makefile for creating pdf document with fonts within it
mainfile=paper
outfile=paper
sources:=*.tex *.bib *.cls
#  *.bst
# figdir=figures
epsfiles=$(wildcard figures/*.eps ; wildcard figures/plot-ranking/*.eps ; wildcard figures/plots/*.eps)
pdffiles=$(epsfiles:.eps=.pdf)

all: ${outfile}.pdf
     
# pdf: ${outfile}.pdf

default: ${outfile}.pdf

clean-tmp:
	rm -f ${mainfile}.bbl
	rm -f ${mainfile}.blg
	rm -f *.log
	rm -f *.aux
	rm -f *.out
	rm -f *.spl

clean: clean-tmp
	rm -f ${outfile}.pdf
	rm -f ${mainfile}.dvi
	rm -f ${mainfile}.ps

%.pdf: %.eps
	@echo $@
	epstopdf $< --outfile=$@

pdf: ${sources} ${pdffiles}
	pdflatex ${mainfile}.tex
	bibtex ${mainfile}
	pdflatex ${mainfile}.tex
	pdflatex ${mainfile}.tex
	make clean-tmp

${mainfile}.dvi: ${sources}  #figs
	latex ${mainfile}.tex
	bibtex ${mainfile}
	latex ${mainfile}.tex
	latex ${mainfile}.tex
	make clean-tmp

${mainfile}.ps: ${mainfile}.dvi
	dvips -o ${mainfile}.ps ${mainfile}.dvi

${outfile}.pdf: ${mainfile}.ps
	gs -dSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -dCompatibilityLevel=1.4 -dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true  -sOutputFile=${outfile}.pdf ${mainfile}.ps 
