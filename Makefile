MAIN = main
TARGET_DIR = target
MAIN_TEX = ./tex/$(MAIN).tex
MAIN_PDF = $(TARGET_DIR)/$(MAIN).pdf
BIB = ./references.bib

TEXINPUTS := ./tex//:
export TEXINPUTS

TRASH = *.aux $(MAIN).blg $(MAIN).run.xml $(MAIN).bbl $(MAIN).log $(MAIN).toc $(MAIN).bcf

all:
	mkdir -p $(TARGET_DIR)
	pdflatex -output-directory=$(TARGET_DIR) $(MAIN_TEX)
	biber $(TARGET_DIR)/main
	pdflatex -output-directory=$(TARGET_DIR) $(MAIN_TEX)
	pdflatex -output-directory=$(TARGET_DIR) $(MAIN_TEX)

.PHONY: fast
fast:
	pdflatex -output-directory=$(TARGET_DIR) $(MAIN_TEX)

.PHONY: clean
clean:
	rm -f $(foreach f,$(TRASH),$(TARGET_DIR)/$(f))

