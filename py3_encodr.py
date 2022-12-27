import os,marshal,time,random
try :
    from pyfiglet import *
    from rainbowtext import *
    from colorama import init
except:
    os.system('pip install pyfiglet')
    os.system('pip install rainbowtext')
    os.system('pip install colorama')
    from pyfiglet import *
    from rainbowtext import *
    from colorama import *

init()

#colors
r='\033[1;31m'
g='\033[32;1m'
y='\033[1;33m'
w='\033[1;37m'
figleted = [figlet_format("  sina maFia  ",font='slant'),figlet_format("  sina maFia  ",font='slant'),figlet_format("  sina maFia  ",font='banner'),figlet_format("  sina maFia  ",font='digital'),figlet_format("  sina maFia  ",font='devilish'),figlet_format("  sina maFia  ",font='diamond'),figlet_format("  sina maFia  ",font='arrows'),figlet_format("  sina maFia  ",font='heavy_me'),figlet_format("  sina maFia  ",font='epic'),figlet_format("  sina maFia  ",font='banner4'),figlet_format("  sina maFia  ",font='banner3-D'),figlet_format("  sina maFia  ",font='zig_zag_'),figlet_format("  sina maFia  ",font='banner3'),figlet_format("  sina maFia  ",font='shadow')]
banner = text(random.choice(figleted)+'\n'+'github : https://github.com/sina-mafia\ntelegram : https://t.me/I_get_tired_But_not_surrender')

print(banner)
print(g)

file_path = input('please enter python3 file path (example : src/file.py ) : ')

if '.py' not in file_path:
    print(f'{r}ERR : please enter .py file!')
else:
    try:
        file=open(file_path,'r').read()
        name = file_path.replace('.py','')
    except IOError:
        print(f'{r}ERR : {y}No such file or directory')
        time.sleep(5)
        exit()
try:
    compiled_file = compile(file,'','exec')
    encoded_code = marshal.dumps(compiled_file)
except TypeError:
    print(f'{r}-ERR : {w} file already compiled!!!')
    time.sleep(5)
    exit()
ofile = open(f'{name}_encoded.py','w')
ofile.write('#encoded by sina maFia\n# my github: https://github.com/sina-mafia\n')
ofile.write('import marshal\n')
ofile.write('exec(marshal.loads(' + repr(encoded_code) + '))')
ofile.close()
print(f'{g}+{y}  succes!!\nencoded file saved in {r}{name}_encoded.py')
time.sleep(5)

