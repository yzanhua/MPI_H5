from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

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

# Users can set customized I/O hints in info object
info = MPI.INFO_NULL  # no user I/O hint

# set file open mode
cmode  = MPI.MODE_CREATE  # to create a new file
cmode |= MPI.MODE_WRONLY  # with write-only permission

fh = MPI.File.Open(comm, file_name, cmode, info)
fh.Close()

flag = True
file_name += "mm"
# set file open mode
omode = MPI.MODE_RDONLY  # with read-only permission


openfunc = Error_Wrapper(MPI.File.Open)
fh = openfunc.run(comm, file_name, omode, info)
if fh is not None:
    print(rank, " closing fh")
    fh.Close()


