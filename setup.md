Install MPICH
===
1. Download source code from [this link](https://www.mpich.org/downloads/): 

    ```shell
    cd ~
    wget http://www.mpich.org/static/downloads/3.4.2/mpich-3.4.2.tar.gz
    ```

2. Unpack the tar file:
    ```shell
    tar xfz mpich-3.4.2.tar.gz
    ```

3. Choose the installation directory:
    ```
    mkdir ~/.mpich
    ```
4. Choose a build directory (this directory will be deleted after installation.)
   ```
   mkdir ~/mpich-build
   ```
5. Enter the build directory and run configuration. Output the results of configuration to `c.txt`.
    ```
    cd ~/mpich-build

    /homes/zhd1108/mpich-3.4.2/configure \
    -prefix=/homes/zhd1108/.mpich \
    --with-device=ch4:ofi 2>&1 | tee c.txt
    ```
6. Build MPICH (output to m.txt):
    ```
    make 2>&1 | m.txt
    ```
7. Install MPICH Commands (output to mi.txt):
   ```
   make install 2>&1 | tee mi.txt 
   ```
8. Add `bin` to `PATH`. In `~/.zshrc`:
    ```
    export PATH="$HOME/.mpich/bin:$PATH"
    ```
9. Remove `mpich-3.4.2.tar.gz` and `mpich-build` (build directory)

<br>

Install h5py and mpi4py
===
1. Create a virtual environment:
    ```
    cd ~
    mkdir envs
    cd envs
    python3.8 -m venv env_mpih5
    ```
2. activate virtual env:
    ```
    cd ~
    source ~/envs/env_mpih5/bin/activate
    ```
3. upgrade pip
   ```
   pip install --upgrade pip
   ```
4. install h5py and mpi4py
   ```
   pip install h5py
   pip install mpi4py
   ```