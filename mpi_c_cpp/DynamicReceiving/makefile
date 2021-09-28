PROJNAME=dynamic_receive
EXEC=${PROJNAME}_exec
MPICC?=mpicc

all: ${EXEC}
${EXEC}: ${PROJNAME}.c
	${MPICC} -o ${EXEC} ${PROJNAME}.c
run:
	mpirun -n 2 ./${EXEC}
create:
	touch -a ${PROJNAME}.c
clean:
	rm -f ${EXEC}