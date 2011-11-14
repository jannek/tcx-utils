graph.pdf: Makefile graph.gp data.txt
	@gnuplot graph.gp

data.txt: Makefile activity.tcx
	@./tcx-haversine.py >$@
