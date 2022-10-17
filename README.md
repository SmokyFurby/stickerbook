# Sticker book Solver
Aim: automate the process of solving puzzles Matthew Scroggs posts in Puzzle Village from his puzzle_solver webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

## Puzzle solver
Currently, the solver is CLI-only.

### How to install
Clone the repo:
```shell
git clone https://github.com/SmokyFurby/stickerbook.git
```
E.g. if the repo folder is called ```stickerbook```, run
```shell
cd stickerbook
```

then install the solver package with
```shell
pip install -e .
```

### Inputting the desired puzzle
Enter the 3 rows and 3 columns in your txt file e.g. "+ + 11" for a row or column saying: ? + ? + ? = 11

### How to run
E.g. if the puzzle txt is at ```./example_puzzles/puzzle_str.txt```, 

cd to repo folder (if not already) and run:
```shell
python ./scripts/main.py --puzzle_path="./example_puzzles/puzzle_str.txt"
```
