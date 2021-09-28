#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<mpi.h>


int main(){
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    if (world_size != 2) {
        fprintf(stderr, "Must be two processes for this example.");
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    int this_rank, other_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &this_rank);
    other_rank = 1 - this_rank;

    const int MAX_NUM = 100;
    int nums[MAX_NUM];
    int num_amount;

    if (this_rank == 0) {
        // pick a random amount of numbers to send to process 1
        srand(time(NULL));
        num_amount = (rand() / (float)RAND_MAX) * MAX_NUM;
        for (int i = 0; i < num_amount; i ++) {
            nums[i] = i;
        }
        MPI_Send(nums, num_amount, MPI_INT, other_rank, 0, MPI_COMM_WORLD);
        printf("Sever %d sent %d numbers to server %d.\n", this_rank, num_amount, other_rank);
    }
    else if (this_rank == 1) {
        /**
        MPI_Status status;
        MPI_Recv(nums, MAX_NUM, MPI_INT, other_rank, 0, MPI_COMM_WORLD, &status);
        MPI_Get_count(&status, MPI_INT, &num_amount);
        printf("Server %d received %d numbers from server %d. Message source = %d, tag = %d\n",
           this_rank, num_amount, other_rank, status.MPI_SOURCE, status.MPI_TAG);
        for (int i = 0; i < num_amount; i ++) {
            printf("number %d is received.\n", nums[i]);
        }
        */

       MPI_Status status;

       // probe for an incoming message.
       MPI_Probe(other_rank, 0, MPI_COMM_WORLD, &status);

       // get message info
       MPI_Get_count(&status, MPI_INT, &num_amount);

       // allocate a buffer to hold the incoming numbers
       int* buffer_ptr = (int*) malloc(sizeof(int) * num_amount);

       MPI_Recv(buffer_ptr, num_amount, MPI_INT, other_rank, 0, MPI_COMM_WORLD, &status);
       printf("1 dynamically received %d numbers from 0.\n", num_amount);  

       free(buffer_ptr);

    }
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();

    return 0;
}