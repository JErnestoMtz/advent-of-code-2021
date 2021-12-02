import Init.System.IO
import Init.Data.List.Basic
import Init.Data.List.BasicAux
open IO
open FS

def get_file : IO String := 
	readFile "input_1.txt"

def hellow_world : IO Unit :=
	print "lol"

def newlines: Char -> Bool
	| '\n' => true
	| defoult => false

def sum (xs: Array Nat) : IO Nat := do
	let mut s := 0
	for x in xs do 
		print s!"x: {x}"
		s := s + x
	return s


def head? (a: List α) : Option α :=
  | []   => none
  | a::_ => some a

def head : (as : List α) → Option α 
	| [] => none
  | a::_ => some a

def main : IO Unit := do
	let f ← get_file
	let b ← f.split newlines
	let w ← b 
	print w 







#eval main


