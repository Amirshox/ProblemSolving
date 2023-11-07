import sys

from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

number = sys.argv[1]

numbers_per_process = 100 // size
print(f"Rank {rank} will sum {numbers_per_process} numbers")
start_number = rank * numbers_per_process + 1
end_number = start_number + numbers_per_process

partial_sum_of_squares = sum(number ** 2 for number in range(start_number, end_number))

total_sum_of_squares = comm.reduce(partial_sum_of_squares, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total sum of squares is {total_sum_of_squares}")

MPI.Finalize()
