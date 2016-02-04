# ajoutez vos programmes ci-dessous
PROGS_SRC=test-freqs.cxx filter-az.cxx

SRC=freqs.cxx utils.cxx
OBJ=${SRC:.cxx=.o}
HEADERS=freqs.h utils.h
PROGS=${PROGS_SRC:.cxx=}
CXXFLAGS=-O3 -g -Wall

all: ${PROGS}

test-freqs: test-freqs.cxx ${OBJ} ${HEADERS} 
	clang++ ${CXXFLAGS} $< ${OBJ} -o $@

filter-az: filter-az.cxx ${OBJ} ${HEADERS} 
	clang++ ${CXXFLAGS} $< ${OBJ} -o $@

%.o: %.cxx %.h
	clang++ ${CXXFLAGS} -c $<

clean:
	rm -f ${PROGS} ${OBJ}
