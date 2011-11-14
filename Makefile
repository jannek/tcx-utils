graph.pdf: Makefile graph.gp data.txt
	@gnuplot graph.gp

data.txt: Makefile activity.tcx
	@./tcx-haversine.py >$@

clean:
	@rm -f data.txt graph.pdf

distclean: clean
	@rm -f activity.tcx
