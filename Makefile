all:
	rm -rf lib
	mkdir lib
	g++ -std=c++11 -Wall -Wextra -pedantic -c -fPIC src/mylib.cpp -o lib/mylib.o
	g++ -shared lib/mylib.o -o lib/libmylib.so

clean:
	rm -rf lib/*.o lib/*.so

ultraclean: clean
	rm -rf lib