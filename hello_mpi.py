import mpi

if mpi.rank == 0:
        for i in range(1,mpi.size):
                print mpi.recv()[0]
else:
        mpi.send("Hello from process " + str(mpi.rank),0)