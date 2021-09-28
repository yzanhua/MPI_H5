This folder contains c/c++ codes to test/demo MPICH.

Each subfolder contains a test.

<br>

1. HelloWorld: (C code)
    ```shell
    cd HelloWorld
    make clean
    make
    make run
    ```

2. SendReceive: (C code)<br>
    This folder contains two tests: test_send_receive and test_ping_pong. In `send_receive.c:main()`, uncomment the corresponding line, then:
    ```shell
    cd SendReceive
    make clean
    make
    make run
    ```
3. DynamicReceiving: (C code) <br>
    This folder tests usage of MPI_Probe().
    ```shell
    cd DynamicReceiving
    make clean
    make
    make run
    ```

4. HelloCPP: (C++ code) <br>
    This test is the same as SendReceive but is written in C++.
    ```shell
    cd HelloCPP
    make clean
    make
    make run
    ```


