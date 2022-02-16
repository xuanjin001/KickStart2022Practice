# TODO: Complete the get_ruler function
def get_ruler(kingdom):
  ruler = ''
  # TODO: Add logic to determine the ruler of the kingdom
  # It should be either 'Alice', 'Bob' or 'nobody'.
  kingdom = kingdom.lower()
  #print(kingdom)
  vowels = {'a', 'e', 'i', 'o', 'u'}
  size = len(kingdom)
  #print('kingdom low=', kingdom[size-1])
  if kingdom[size-1] == 'y':
    ruler = 'nobody'
  elif kingdom[size-1] in vowels :
    ruler = 'Alice'
  else:
    ruler = 'Bob'
  
  #print(ruler)
      
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()

