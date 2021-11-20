from mpi4py import MPI
comm = MPI.COMM_WORLD

tag_ub = comm.Get_attr(MPI.TAG_UB)
print(tag_ub)