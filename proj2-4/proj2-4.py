import sys
import string



def initializeFirstCol(distanceMatrix, rows, source):
  distanceMatrix = [[distanceMatrix[i-1, 0] + del_cost(source[i]) for j in range(0, 1)] for i in range(1, rows)]
  
  for i in range(1, rows):
    distanceMatrix[i, 0] = distanceMatrix[i-1, 0] + del_cost(source[i])
  
  return distanceMatrix

def initializeFirstRow(distanceMatrix, collumns, source):
  distanceMatrix = [[distanceMatrix[0, j-1] + ins_cost(target[j]) for i in range(0, 1)] for j in range(1, columns)]
  
  for i in range(1, columns):
    distanceMatrix[0, j] = distanceMatrix[0, j-1] + ins_cost(target[j])
  
  return distanceMatrix

def computeMinEditDistance(distanceMatrix, rows, columns, source, target):
  for i in range(1, rows):
    for j in range(1, columns):
        distanceMatrix[i,j] = MIN(
                                  distanceMatrix[i-1, j] + del_cost(source[i]),
                                  distanceMatrix[i-1, j-1] + sub_cost(source[i], target[j]),
                                  distanceMatrix[i, j-1] + ins_cost(source[j])
                                  )
  return distanceMatrix[n,m]


def del_cost(char):
  return 1

def ins_cost(char):
  return 1

def sub_cost(src, trgt):
  return (src != trgt) ? 2 : 0




main():
  source = sys.argv[1]
  target = sys.argv[2]
  
  n = len(source)
  m = len(target)

  distanceMatrix[][] = initializeMatrix([[0 for j in range(0, m)] for i in range(0, n)],
                                        n, m, source, target)


main()
