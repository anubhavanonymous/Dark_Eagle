import os
import sys
import time
import random
from termcolor import colored, cprint

def Banner():

	bn1 = colored(''' \033[92m	
              .---.        .-----------
             /     \  __  /    ------
            / /     \(  )/    -----
           //////   ' \/ `   ---       DARK EAGLE !!
          //// / // :    : ---
         // /   /  /`    '--
        //          //..\\
               ====UU====UU====
                   '//||\\`
                     ''`` ''',)

	bn2 = colored(''' \033[93m                         
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |   DARK EAGLE!   |  |  |     |         |      |
     |  |  Web pentesting |  |  |/----|`---=    |      |
     |  |    Framework    |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
			''',)

	bn3 = colored('''\033[92m 
  \033[92m  Dark Eagle \033[27m   
   -----------                
      \                
       \    
        \
\                 | 
      ____________    __ -+-  ____________ 
      \_____     /   /_ \ |   \     _____/
       \_____    \____/  \____/    _____/
        \_____                    _____/
          \___________  ___________/
                     /____\                 
                                ''',)   
                                  
	bou = [bn1, bn2, bn3]
	const = bou[random.randint(0, 2)] 
	print const


Banner()
