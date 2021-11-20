from mpi4py import MPI
import sys
import os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
MAX_TRIES=10


sys_err = np.empty(1, dtype="i")

class Error_Wrapper:
    def __init__(self, func):
        self.func = func
    def run(self,*args, **kwargs):
        result = None
        try:
            result = self.func(*args, **kwargs)
        except:
            print("Rank:", rank, "Error in", self.func.__qualname__)
        return result


file_name = "testfile"
buffer = np.empty(10, dtype='i')

for i in range(MAX_TRIES):
    if rank == 0:
        if os.path.isfile(file_name):
            os.unlink(file_name)
            sys_err[0] = 0
        elif not os.path.exists(file_name):
            sys_err[0] = 0
        else:
            sys_err[1] = -1
        
    comm.Bcast(sys_err, 0)

    if sys_err[0] != 0:
        break

    fh = MPI.File.Open(comm, file_name, MPI.MODE_CREATE | MPI.MODE_RDWR, MPI.INFO_NULL)
    if rank == 0:
        fh.Write(buffer)
    fh.Close()
            