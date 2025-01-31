MAIN = main

TRASH = *.aux $(MAIN).bcf $(MAIN).log $(MAIN).run.xml $(MAIN).bbl $(MAIN).blg $(MAIN).toc

$(MAIN).pdf: *.tex appendices/*.tex references.bib
	pdflatex $(MAIN) > /dev/null
	biber    $(MAIN) > /dev/null
	pdflatex $(MAIN) > /dev/null
	pdflatex $(MAIN)

.PHONY: fast
fast:
	pdflatex $(MAIN)

.PHONY: clean
clean:
	rm -f $(TRASH)
