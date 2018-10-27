OUTDIR='../bin/'
gmy2hgb: cannonsim.cc
	mkdir -p ${OUTDIR}
	g++ -O3 -lm -Wall cannonsim.cc -o ${OUTDIR}cannonsim
debug: cannonsim.cc
	mkdir -p ${OUTDIR}
	g++ -g -lm cannonsim.cc -o ${OUTDIR}cannonsim
