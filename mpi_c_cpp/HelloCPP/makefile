PROJNAME=hello_cpp
EXEC=${PROJNAME}_exec
MPICC?=mpicxx

all: ${EXEC}
${EXEC}: ${PROJNAME}.cc
	${MPICC} -o ${EXEC} ${PROJNAME}.cc
run:
	mpirun -n 2 ./${EXEC}
create:
	touch -a ${PROJNAME}.cc
clean:
	rm -f ${EXEC}