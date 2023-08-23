import pyfiglet
from simple_chalk import chalk

print(chalk.black(pyfiglet.figlet_format(text='HIKO DZ', font='slant')))
print(chalk.black(pyfiglet.figlet_format(text='Multiplication Table From 1 to 10', font='digital')))
#* use function range for print line lterative multiplication :
y = list(range(1, 11))
print((f'{"      "}'),chalk.bgBlack( '     '.join(f'{num:2}' for num in y)))
print(chalk.black('-' * 73))
#* create function for return result or multiplication in list and custom  format in output:
def line_output(number):
    x = [number * num for num in range(1, 11)]
    print(chalk.bgBlack(f' {str(number):2}  | '), chalk.white('     '.join(f'{str(num):2}' for num in x)))
# use for loop and repetition finction result for  multiplication 
for i in range(1, 11):
    line_output(i)
