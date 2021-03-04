import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ6568", "r")

MEMORY = [0] * 32
ADDER = 0
PROGRAM_COUNTER = 0
EXIT_FLAG = False

def sta(x) :
  global ADDER
  x = int(x, 2)
  MEMORY[x] = bin(ADDER)[2:]
def lda(x) :
  global ADDER
  x = int(x,2)
  ADDER = int(MEMORY[x],2)
def beq(x) :
  global ADDER
  global PROGRAM_COUNTER
  if ADDER == 0 :
    PROGRAM_COUNTER = int(x,2)
def nop() :
  return
def dec() :
  global ADDER
  ADDER -= 1
  if ADDER < 0 :
    ADDER = 255

def inc() :
  global ADDER
  ADDER += 1
  if ADDER > 255:
    ADDER = 0
def jmp(x) :
  global PROGRAM_COUNTER
  PROGRAM_COUNTER = int(x,2)
def hlt() :
  global EXIT_FLAG
  EXIT_FLAG = True


index = 0
while True :
  line = sys.stdin.readline().rstrip()
  if not line : 
    break
  MEMORY[index] = line
  index += 1 
  if index >= 32 :
    PROGRAM_COUNTER = 0
    index = 0
    ADDER = 0
    EXIT_FLAG = False
    
    while True :
      command , memaddress = MEMORY[PROGRAM_COUNTER][:3] , MEMORY[PROGRAM_COUNTER][3:]
      PROGRAM_COUNTER += 1
      if PROGRAM_COUNTER >= 32 :
        PROGRAM_COUNTER = 0
      if EXIT_FLAG :
        print(bin(ADDER)[2:].zfill(8))
        break
      if command == '000' :
        sta(memaddress)
        continue
      if command == '001' :
        lda(memaddress)
        continue
        
      if command == '010' :
        beq(memaddress)
        continue
        
      if command == '011' :
        nop()
        continue
        
      if command == '100' :
        dec()
        continue
        
      if command == '101' :
        inc()
        continue
      if command == '110' :
        jmp(memaddress)
        continue
        
      if command == '111' :
        hlt()
        continue
    