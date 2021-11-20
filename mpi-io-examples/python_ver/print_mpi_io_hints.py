from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if len(sys.argv) != 2:
    print("Usage: {} filename".format(sys.argv[0]))
    exit(1)

fh = MPI.File.Open(comm, sys.argv[1], MPI.MODE_CREATE | MPI.MODE_RDWR, MPI.INFO_NULL)

if rank == 0:
    info_used = fh.Get_info()
    nkeys = info_used.Get_nkeys()
    print("MPI File Info: nkeys =", nkeys)

    for i in range(nkeys):
        key = info_used.Get_nthkey(i)
        value = info_used.Get(key)
        print("MPI File Info: [{}] key = {}, value = {}".format(i, key, value))
    info_used.Free()

fh.Close()
    