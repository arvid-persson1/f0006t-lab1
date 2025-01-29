MAIN = main

TRASH = *.aux $(MAIN).bcf $(MAIN).log $(MAIN).run.xml $(MAIN).bbl $(MAIN).blg $(MAIN).toc

$(MAIN).pdf: *.tex references.bib
	pdflatex $(MAIN) > /dev/null
	biber    $(MAIN) > /dev/null
	pdflatex $(MAIN) > /dev/null
	pdflatex $(MAIN) > /dev/null

.PHONY: fast
fast:
	pdflatex $(MAIN) > /dev/null

.PHONY: clean
clean:
	rm -f $(TRASH)
