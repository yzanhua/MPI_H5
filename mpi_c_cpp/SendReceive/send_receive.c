#include <mpi.h>
#include <stdio.h>

void test_send_receive();

void test_ping_pong();

void test_wrapper(void (*)(), int *);

int main() {
    int test_count = 0;

    // uncomment one of the following two lines.
    //test_wrapper(test_send_receive, &test_count);  // test send and receive
    test_wrapper(test_ping_pong, &test_count);      // test ping pong
    return 0;
}

void test_send_receive() {
    // Initialize the MPI environment
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Get the rank of the processes
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int number;
    if (world_rank == 0) {
        number = -1;
        MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        number = 2;
    } else if (world_rank == 1) {
        MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD,
                 MPI_STATUS_IGNORE);
    }
    printf("Process %d received number %d from process 0\n", world_rank,
           number);
    // finalize the MPI environment
    MPI_Finalize();
}

void test_ping_pong() {
    // Initialize the MPI environment
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Get the rank of the processes
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int ping_pong_count = 0;
    int partner_rank = (world_rank + 1) % 2;
    int PING_PONG_LIMIT = 15;
    while (ping_pong_count < PING_PONG_LIMIT) {
        if (world_rank == ping_pong_count % 2) {
            // Increment the ping pong count before you send it
            ping_pong_count++;
            MPI_Send(&ping_pong_count, 1, MPI_INT, partner_rank, 0,
                     MPI_COMM_WORLD);
            printf("%d sent and incremented ping_pong_count "
                   "%d to %d\n", world_rank, ping_pong_count,
                   partner_rank);
        } else {
            MPI_Recv(&ping_pong_count, 1, MPI_INT, partner_rank, 0,
                     MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("%d received ping_pong_count %d from %d\n",
                   world_rank, ping_pong_count, partner_rank);
        }
    }
    // finalize the MPI environment
    MPI_Finalize();
}

void test_wrapper(void (*test_func_ptr)(), int *test_count_ptr) {
    if ((*test_count_ptr) == 0) {
        test_func_ptr();
        (*test_count_ptr)++;
    }
}