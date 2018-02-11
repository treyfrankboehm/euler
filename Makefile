LANG=haskell
NUM=007
SRC=$(NUM).hs
PROGRAM=$(NUM).bin
TEST=test.py

$(LANG)/$(PROGRAM): $(LANG)/$(SRC)
	@echo "  GHC  " $(LANG)/$(SRC)
	@ghc -o $(LANG)/$(PROGRAM) $(LANG)/$(SRC)

hs: clean
	@echo "  Testing all Haskell solutions"
	@./$(TEST) hs

py: clean
	@echo "  Testing all Python solutions"
	@./$(TEST) py

c: clean
	@echo "  Testing all C solutions"
	@./$(TEST) c

test: $(LANG)/$(SRC)
	@./$(TEST) $(SRC)

clean:
	@echo "  Cleaning"
	@rm -f haskell/*.bin haskell/*.hi haskell/*.o
	@rm -f c/*.out

