all: mst.out

mst.out: main.o graph.o nodelist.o utility.o floyd.o
	gcc -Wextra -Wall -O3 main.o graph.o nodelist.o utility.o floyd.o -o mst.out
	rm *.o

main.o: main.c header/nodelist.h header/graph.h header/utility.h
	gcc -Wextra -Wall -O3 -c main.c -o main.o

utility.o: header/utility.h source/utility.c
	gcc -Wextra -Wall -O3 -c source/utility.c -o utility.o

graph.o: header/graph.h source/graph.c header/utility.h header/nodelist.h
	gcc -Wextra -Wall -O3 -c source/graph.c -o graph.o

nodelist.o: header/nodelist.h source/nodelist.c header/utility.h
	gcc -Wextra -Wall -O3 -c source/nodelist.c -o nodelist.o

floyd.o: header/floyd.h
	gcc -Wextra -Wall -O3 -c source/floyd.c -o floyd.o

clean:
	rm *.o

veryclean: clean
	rm *.out

