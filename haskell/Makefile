NUM=007
SRC=$(NUM).hs
PROGRAM=$(NUM).bin

$(PROGRAM): $(SRC)
	@echo "  GHC  " $(SRC)
	@ghc -o $(PROGRAM) $(SRC)

test: $(PROGRAM)
	@time ./$(PROGRAM)

clean:
	@echo "  Cleaning"
	@rm -f hs-build-files/*
	@rm -f $(PROGRAM) $(NUM).hi $(NUM).o

spotless: clean
	@echo "  Removing all executable, intermediate, and object files"
	@rm -f *.bin *.hi *.o
