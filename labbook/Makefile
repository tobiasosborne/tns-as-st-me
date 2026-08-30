all:
	latexmk -pdf -interaction=nonstopmode main.tex

clean:
	latexmk -C main.tex
	rm -f sections/*.aux

.PHONY: all clean
