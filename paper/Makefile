# paper/Makefile
# Build the Letter (main.pdf) and, optionally, the standalone Supplemental
# Material (supplement.pdf) via latexmk. Both hooks from main.tex (inline
# End Matter vs. separate supplement.tex) are covered by separate targets;
# `make` / `make all` builds only the Letter, matching the "4-page PRL is
# the product" law (L9) -- the SM is not part of the page count.

LATEXMK = latexmk
LATEXMK_FLAGS = -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all main supplement clean distclean

all: main

main:
	$(LATEXMK) $(LATEXMK_FLAGS) main

supplement:
	$(LATEXMK) $(LATEXMK_FLAGS) supplement

clean:
	$(LATEXMK) -c main
	$(LATEXMK) -c supplement
	rm -f *.bbl *.blg *.log *.aux *.fdb_latexmk *.fls *.out *.synctex.gz main.pdf supplement.pdf

distclean: clean
