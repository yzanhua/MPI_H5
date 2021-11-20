from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

buff = np.empty(10, dtype='i')

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

# get file name
file_name = "testFile"
if len(sys.argv) > 1:
    file_name = sys.argv[1]


cmode  = MPI.MODE_CREATE | MPI.MODE_RDWR
fh = MPI.File.Open(comm, file_name, cmode, MPI.INFO_NULL)

for i in range(10):
    buff[i] = 100 * rank + i

offset = rank * 10 * MPI.INT.Get_size()
fh.Set_view(offset, MPI.INT, MPI.INT, "native", MPI.INFO_NULL)
fh.Write_all(buff)

fh.Close()