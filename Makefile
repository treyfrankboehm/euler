NUM=007
SRC=$(NUM).hs
PROGRAM=$(NUM).bin

$(PROGRAM): $(SRC)
	@echo "  GHC  " $(SRC)
	@ghc -o $(PROGRAM) $(SRC)

all: clean
	@echo "  Testing all solutions"
	@./test.py all

test: $(PROGRAM)
	@time ./$(PROGRAM)

clean:
	@echo "  Cleaning"
	@rm -f *.bin *.hi *.o

