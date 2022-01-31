CC=h5pcc # h5 parallel cc in /home/zanhua/.hdf5/bin
H5_INCLUDE_DIR=/homes/zhd1108/HDF5/1.13.0/include

# add more headers here
HEADERS=$(H5_INCLUDE_DIR)

INCLUDE_PARAM=$(HEADERS:%=-I%)

# add more C flags here
CFLAGS=$(INCLUDE_PARAM)

all:
	$(CC) $(CFLAGS) main.c -o out

clean:
	rm -rf out *.o *.h5 *.hdf5