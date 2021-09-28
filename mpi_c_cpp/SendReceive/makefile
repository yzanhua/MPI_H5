PROJNAME=send_receive
EXEC=${PROJNAME}_exec
MPICC?=mpicc

all: ${EXEC}
${EXEC}: ${PROJNAME}.c
	${MPICC} -o ${EXEC} ${PROJNAME}.c
run:
	mpirun -n 2 ./${EXEC}
clean:
	rm -f ${EXEC}