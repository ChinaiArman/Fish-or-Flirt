from art import *
import sys
import time

title = r"""

 ________ .-./`)    .-'''-. .---.  .---.             ,-----.    .-------.             ________   .---.    .-./`) .-------. ,---------.  
|        |\ .-.')  / _     \|   |  |_ _|           .'  .-,  '.  |  _ _   \           |        |  | ,_|    \ .-.')|  _ _   \\          \ 
|   .----'/ `-' \ (`' )/`--'|   |  ( ' )          / ,-.|  \ _ \ | ( ' )  |           |   .----',-./  )    / `-' \| ( ' )  | `--.  ,---' 
|  _|____  `-'`"`(_ o _).   |   '-(_{;}_)        ;  \  '_ /  | :|(_ o _) /           |  _|____ \  '_ '`)   `-'`"`|(_ o _) /    |   \    
|_( )_   | .---.  (_,_). '. |      (_,_)         |  _`,/ \ _/  || (_,_).' __         |_( )_   | > (_)  )   .---. | (_,_).' __  :_ _:    
(_ o._)__| |   | .---.  \  :| _ _--.   |         : (  '\_/ \   ;|  |\ \  |  |        (_ o._)__|(  .  .-'   |   | |  |\ \  |  | (_I_)    
|(_,_)     |   | \    `-'  ||( ' ) |   |          \ `"/  \  ) / |  | \ `'   /        |(_,_)     `-'`-'|___ |   | |  | \ `'   /(_(=)_)   
|   |      |   |  \       / (_{;}_)|   |           '. \_/``".'  |  |  \    /         |   |       |        \|   | |  |  \    /  (_I_)    
'---'      '---'   `-...-'  '(_,_) '---'             '-----'    ''-'   `'-'          '---'       `--------`'---' ''-'   `'-'   '---'    
                                                                                                                                        
"""

crab = r"""
                                                                                                                                                      
                                             ``                                                                                                       
                                             i:                                                                                                       
                                            ,*.                                                                                                       
                                           `;:                                                                                                        
                                           ,:,                                                                                                        
                                          `::`                                                             ``                                         
                                          ,,:`                                                             .+`                                        
                                         .,,,                                                              `i:                                        
                                        ,+,,,                                                               ::`                                       
                                       .ii,,.                                                               ::.                                       
                                      `;;:,:`                                                               ::.                                       
                                     `:;:.,:`                                                               ,:.`                                      
                                     ,;::,,,                                                                ,:..                                      
                                    `;:::;:,                                                                ,:..                                      
                                    ,;,,:;;.                                                                ,;,,`                                     
                                   `;:,:,:i,                                                                ,i,,`                                     
                                   ii,,,,:i:                                                                ,**:.                                     
                                  ,+;,,:::i.                                                                ,ii;,                                     
                                  i+;,,;i;i`                                                                ,;;::.                                    
                                 `*+;,:***i`                                                                :i;:,;`                                   
                                 ,++;,;+++;                                                                `i*i:,:,                                   
                                 :++i;*+++:                                                                `**i:,.:`                                  
                                 ;+#**++#+,                                                                .*ii:,.,,                                  
                                 i+#+*++##.                 .,                                             .*ii:,..:                                  
                                 i#++++##+:..              ;@W*                                            ,***:,.,;`                                 
                                 ;##+++####z*             `WW#x`                :n+                        :+#+:,,;i.                                 
                                 :###++##*#zni            ,@#WW.               `xMW:                       ;##+;,:i*,                                 
                                 .###++#+i##zn.           .@#WW+;;;ii:,`  ``..`+WWW*                       iz#+;:;**,                                 
                                  i###++**#zzn*         `.:W#WWWn#nxMMx#i+znxxnM###*`                    .i+z#+i;***,                                 
                                  .####+*+##znn`     `:*zxM@@WWW@WWMMMMxxMWWWWMW@#@#i:,`                `#xzz#+*i*+*.                                 
                                   i#zz#+zz#znn:   ,#MWWM@@##@@W@@MxnnxMMMMMW@@@@#@Wx#*i,``             +xx#z#++*+**`                                 
                                   i+###zz##+#xi `+MWWWWMW@@###@@MnnnnznnnxxW@@W@@@@WMx#**i;:.         ,xxxzz##++++i                                  
                                   ,####z#i:;i#; :MWWWWWWMWW@##@@MxnxxxxnnnxM@#@@MM@@MxMxxxnnz*.       #xMxzzz#++++,                                  
                                    :####i:::;*zi*MWWW@WWWWWW@@WWWWWWWWWMxxWWMWW@xxMMMnnnznxMMMni`    .MxMxnn#####*`                                  
                                 ``,.inn+;;;;;*x*#MMWW@@WWWWW@@WWWWW@W@@WW@@WWWWWWWMMxnxnnnxMWWWWz.   :MxxMxnz####:                                   
                             `,i+++xnnnz#;i;:i#ninMxxMMMMxxxM@WMnWWWWMMW@@@@WW@@WMMxxxnzznnxMWWWWWM:  :znxxxnzz##*,                                   
                           `:+nxxxMMMMMz#i;;ii+nixMxxxxMMMxxMMxnxWW@@@W@@@@WMMx@Mxxnnn###zxMMMMWWWWx,#*++znnnzz#**`                                   
                          .*nxxxxMMMMMM#++**#+#x+xMxxxxxxxxxxnnMMxxxW@MWWMMWMxxxMxxn#++++#znxMMWWW@M#x***+znnz#++.                                    
                         .+xxxxxxMMMMMMx+#zzzznnzxMMnxxxxxxxxnxMxxxxnMWMxxMxxMxxxnnn###zzzznnxxMWW@@nn+**+++nnz#.                                     
                        .#xxxxxn;zxMMMMMnzzzzzznnxMMxxxxxxxxxxMMxMxxxnMxxxxxxnxxxxxxxnnnnnnnnxxxMW@@nn+*i*iizz*`                                      
                       `;nxxxxn*.,zMMMMMx#zzzzzxxMWMxxxxxxxxxMMMxMxxxnMxxxMMxxxxxxxnxnnnnnnnxxxxxMWWzn#*;;i*z,                                        
                      .iznnnnnz. `:xMMMMM#zznnnnxMWWxxxxxxxxMMMMMMxxxzMxMMMMMxxxxxxxnnnnnnnxxxxxxxMxzzz+*;;+#.       ``.`                             
                     .+xnxnnnn;` `:nMMMMMz#znnnnxMWWMxxxnxxxxMMMMMxxzxMnMMMxxxxnxxxxnnnnnxxxxxxxxMMz##zzz#++:      .i#zz#i:`                          
                    ,#nxxxnnn*.  `;nxMMMMx##nnnnnMWWMxxxxnnxnxxxMxxxzxMznxxxxxxnxxxnnnnnnnxxxxxxxMx##+##++#;     `;znnnnnzzzi`                        
                   ,#nnnnnnn#,`  .#nnMMMMMz#znnnnxWWMMxnnnnnnnnxxxxz#zxnznxxxxnnnxnnnnnnnnxxxxxxMM#######++`    .+nznnzzzz#zz*`                       
                  ,#nnnnnnnni`  `:zxnxMMMMM##nnnzzMWWMxxnnnxnnnnnzzn+*nzz#znzzznnnnnnnznnnxxxxxxMn*i#####+;`.,.:znnnnnnzzz#z#*i`                      
                 .+nnnnnnnzi.`  `;nxxxMMMMMx#znnzznWWMMxxnnxnnnz#znxnnMxzz#+zznnnnzzzznnxxxxxxxxM#iii*+#+#*znnznnnznnzzzz#+z#*i;`                     
                `*nnnnzzzzi.`   `inxxxxMMMMMn#znzzzMWWMxxnznnnnnnz#zxxMxz##znnnznnzzznnxxxxxxxxMx*;i*ii++nxxxnnnnnnnnzzz+*.*z+ii,                     
                ,znnzzzz+;.`    `inxxxznMMMMMn##+###zMWMxnzznnnnnz#+nxxx##znnnznznzzznnxxxxxxMMM#*iiiii*nxxxnnnnnnzzzzz#zn:*z#*ii`                    
               `;nnzzzz*,.`   ```innnn+:nMMMMMz#+##z**xWWMxnnnnnzz#++nnn++znnzzzzn##znnnxxxxxMMn+*+*iiizxxxnnnnnnzzzzz#zxxnnz##i+;                    
               `inzzz+;..``.:;;;;inxnn;`;xMMMMMnz+##+i*#nMMMMnzzz#++#nnn#++zzzzz#zz#zznnxxMMMMn#*##+**zxxxnnnnnzzzzzz##xxxxnz##*++;`                  
               `*zz+i,..``:#nxxxxxxxxz;..ixMMMMMx++++i;;i*+zxnzzz#+#++#z##+#zzzzz#znxxxxxxMMxz##++**+zxxxnnnnnzzzzzz##xxxnnzz#+*++##i.                
               .*++:.....,*nnxxxxxxxxxxz+*#xMMMMWn##**iii;i+#zz####++**+++#+#z###+#nnnnxnnnnz#*++++#nxxxnnnnnzzzzzzzzxxxnn#:;#+**+#zz#,               
               .*+*,..:*#znxnxxxxxxxxxxxxMxMMMMMMWWxz+*i;i**;+nnzz##+*####+++++#+#+z+++##+*###**++#nxxxxnnnzzzzzz#zzznxnzz#;`#z##+#z#zz+,             
               .*+*::+nnzzznzznxxxxxxxxxxxxxxMMMMMMWxx#**+#*;+nzz##++##**+#++##+##++*+***ii*++**zzxxxxxxnnzzz####znzzznzzzz*`:z####zzzzzzi.           
              `.**i*nnn#zz#+zznnnnnnnxnnxxxxxxMMMWMMMx####*;*#nnzz###z#+*i+++++###*+i#+*iii*++*+nxxxxxxnz####znnxxxznz##zzz; `*z#####znzzz+,          
              `,*++znn##z+++###zzznzzznnnnxxxxxMMMxxxxx#+ii+#zzzz##+###++**+++####*+i*#+ii+#znnxxxxxxxzznnxxxxxxxxxnzn#.#z#.  .+z#####zzzzzz;`        
              `,+nzzz+*#*;i**##zz##++++##zznnnnxxnnznxxxxn+++++###+++####+*+**++++*i+**++++nxxnxnnnnnxxxxxxxxxxxxxnnznx*+#;` ``.+#####zzzzzz#i`       
             `.,+zzz#i*#:::::i#zzzzz#+***+++##zxnz###zzzn#****++++++####+****ii*****i+*ii*#nnnnnznnnxxxxxxxxxxxxnnnnnnn#+;` ````,+######zzzzz#;`      
             `.:+zz#++#;,,,,,,,:i#zzzzz##+##z#nn##i;;*#zz+**+++++++#+++#z#*i***iiiiiii+#znnzzzzzznnnxxxxxxxxxxxnnnzznnn+;` ```` `,#######zzz###.      
            `.,#znnz#+*,,,,,..,,,,:;*######++*i;;::::;i*++**+++++**+*++++**i;;i+++****iiinnzzzz#znnxxxxxxxxxxnnnnznnnzz:````` ````,+####+#####z;      
            `.+nnnnz#+:.............,,,::;:,,,,,,,,::::::::;;;;;iiiiii******ii;i+++++++***###zzz#znxxxxxnnnnnnnnnnnzzz+,.``````````.+#+++,;+#z#i`     
           ``izznznz#*....````.`````.....,........,,,,,,,,,,,,,,,,,,:::;;iiiiiiii*ii*****+#zznnnz+*##zzzzzznnnnnn#z#zz;...``````````,+##+,.,:*+*,     
           `:znzzzzz+,...```````````````.........................,,,,,,,,,,,,,,,,,:::::::::;;;;;:::,,:;*+++*i;inn####+,...``````````.,*#*,...:*i:`    
           .+zzzz###,.```````````````````````````````.............................,,,,,,,,,,,,,,,,,,..,,,,,,,:znnz#++:,...``````````..i*i,....ii;`    
           :zzzzz#+,``````````````````````````````````````````````````````.................................,,*nnnzz#*,...```````````..**i,....;**`    
          `+zzzz#+:```````````                  ```````````````````````````````````..........................#nnnzz+,...````````````..**i,,...:#+.    
          .#zzz#+:.``````                                         `````````````````````````````````````````.,nznnzz;.````````````````.**:....,:##.    
         `.+nz#+:..``````                                                ```````````````````````````````````*nzzzzz,`````````````````:**....`.,;;`    
          `+zz#;.`````                                                              `   ```````````````````.#zzzzz+``  ````` ````````;+i.````````     
          `i#+*i:````                                                                             `````````:zzzzzz;             `````+#,````          
           `;*iii:.                                                                                ````````*zzzz#+`              ```.#z.``            
           `.:iii;;.`                                                                               ``````.#zzz##,                ``:#;`              
            `.,:ii;;,`                                                                              ``````,zzz##*`                  ,:`               
             `..,;i*i;.                                                                              `````:###+*.                                     
              ``..,:;iii.                                                                            `````;+##*,                                      
                 ````..,:.                                                                           ```.:+*+i:`                                      
                                                                                                   `````;**ii.`                                       
                                                                                                   `` `;iiii.`                                        
                                                                                                    ``;ii*;``                                         
                                                                                                    .;*ii,`                                           
                                                                                                  `.+**i.`                                            
                                                                                                 `:*++,`                                              
                                                                                               `:*+*:.                                                
                                                                                              `ii:,`                                                  
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      

"""

blushing = r"""
⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⣿⣇⠀⠀⠀⠀
⣿⢏⣹⣳⣯⣗⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠃⠒⣜⣮⢧⡀⠀⠀
⣿⡞⠁⡉⠙⠻⣷⣿⢦⣤⣤⣶⣶⣶⣶⣶⣶⣾⣿⡿⠋⠀⠌⡐⠈⢿⣿⣣⠀⠀
⣿⠀⢂⠐⡁⢂⣬⣿⣿⢫⠉⠀⠀⠀⠀⠀⠀⠜⡹⢿⣿⣿⣶⣶⣤⣈⣿⣷⣗⠀
⡇⢀⣦⣼⣾⣿⣿⣿⡭⡃⠌⠀⠀⠀⠀⠀⠀⠀⠑⡹⣚⢿⣿⣿⣿⣿⣿⣿⣼⠀
⣿⣿⣿⣿⣿⣿⣟⢧⢃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⢎⠳⢯⡟⣿⣻⢿⣯⡷
⣿⣿⡿⣟⡿⡓⢎⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣰⣬⣧⡝⢊⠙⣷
⠟⢧⠛⠥⠃⢉⠀⣴⣾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⠀⠀⢸
⠈⠄⡈⠤⣁⠢⡀⢿⣿⣿⣿⠃⠀⠀⠀⠀⢠⡄⠀⣴⠀⠀⡀⢙⢛⡛⠭⢠⠃⢆
⠐⡠⢑⡒⡄⠓⡌⣌⢩⣩⠷⠶⣤⠀⠀⠀⠀⠳⠾⠃⢀⢸⡼⠋⠋⠛⢦⡃⠞⡠
⢀⠱⡈⢖⡈⢣⠜⣠⠟⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⠐⣾⠁⠀⠀⠀⠈⢧⢣⢸
⣆⠠⢑⠢⣉⠆⢼⡟⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠈⣷⢯
⡏⠀⠀⢁⠂⢌⡟⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠈⣗⠀⠀⠀⠀⠀⠀⠈⢯
⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀
"""

flirt_fail = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡿⢛⣾⣿⠿⠟⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⠟⠛⠻⠷⠶⢦⣄⡉⠻⢿⣿⣿⠃⣸⢋⣤⡾⠟⠛⠓⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⠞⠉⠀⠀⠈⠉⣙⣶⣦⣴⠿⠷⠿⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠶⢶⣤⣀⣡⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⡏⠀⣀⣤⣶⠾⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⡀⠀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢽⣷⡾⠛⠉⠀⠀⠀⢀⣴⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⣿⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡿⢾⣿⣄⠀⠀⠀⠀⠀⠸⣿⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠛⠀⠀⠀⠀⠀⠀⠰⣄⠀⠈⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠉⠙⠃⠀⠀⠀⠀⠀⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⣀⣀⣀⣀⣿⣷⡀⠀⠹⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡿⠿⠿⠿⢿⣦⣄⡀⠀⢠⡿⠋⠁⠀⠀⠀⠈⠉⠉⠁⣰⣿⣇⠀⠀⢻
⣿⣿⣿⣿⣿⣿⣿⠋⠀⢀⣴⠃⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠉⠀⢀⣀⣠⣤⣀⣈⠻⣷⣄⣿⣣⣶⠿⠿⠛⠿⠿⠿⠟⠛⠉⣼⣿⠀⠀⠘
⣿⣿⣿⣿⣿⣿⠃⠀⠀⣾⢿⣆⠀⠀⠀⢀⣤⣶⠟⠋⠀⠀⣠⣶⡿⠟⠋⠉⠉⠛⢷⣾⣿⣿⣿⣥⣤⣄⣀⠀⠀⠀⣀⣤⡾⢫⡿⠀⠀⠀
⣿⣿⣿⣿⣿⡏⠀⠀⢰⣿⡄⠙⠛⠛⠛⠛⠉⠀⠀⢀⣴⣾⠟⠉⠀⠀⣀⣤⣶⡶⠶⢿⣿⣿⣯⡀⠉⠙⠛⠛⠛⠛⠛⠉⣠⣾⠃⠀⠀⢰
⣿⣿⣿⣿⣿⠁⠀⠀⢸⣟⠻⣦⣤⣀⣀⣠⣤⣴⠾⠟⠋⠀⠀⠀⣠⣴⡿⠛⠁⠀⠀⣼⣿⠁⠻⣿⣦⣤⣀⣀⣀⣠⣤⣾⠟⠃⠀⠀⠀⣼
⣿⣿⣿⣿⣿⠀⠀⠀⠘⣿⣦⡀⠉⠉⠉⠉⠉⠀⠀⠀⠀⣀⣴⣾⠟⠋⠀⠀⠀⣠⣾⣿⠃⠀⠀⠀⠉⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⣰⣿
⣿⣿⣿⣿⣿⡀⠀⠀⠀⠹⣿⡿⣶⣤⣤⣀⣠⣤⣤⣶⠿⠟⠋⠀⠀⠀⠀⣀⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿
⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠘⢿⣶⣌⡉⠉⠉⠉⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣶⣶⣶⣾⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡆⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠿⠋⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⠛⠻⠿⠶⣦⣤⣀⣴⡾⠟⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⣀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠐⣉⣻⣽⣤⣤⣀⣤⣄⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡇⠀⣀⣶⣿⣿⣿⣿⣿⣿⠟⠉⠉⠃⠀⢸⣿⣿⡟⠋⠁⠈⠙⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠋⠁⠀⠀⣿⣿⣾⣿⣿⠟⠛⢻⣿⣿⠁⠀⢀⣶⠀⠀⢸⣿⡟⠀⠀⣶⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣤⣾⣿⡏⠁⢠⠃⠀⠀⠀⢻⡇⠀⠀⣾⣿⠀⠀⢸⣿⠁⠀⢰⣿⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠛⠉⢸⣿⡇⠀⠀⢠⡴⠀⠀⣸⠁⠀⢠⣿⣿⠀⠀⢸⡇⠀⠀⠛⠛⠀⠀⣸⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⣠⣾⣿⣿⣿⣿⢿⠏⠁⣿⠀⠀⢸⣿⠇⠀⠀⣿⡇⠀⠀⣿⡀⠀⢸⣿⣿⠀⠀⣾⡇⠀⠀⢶⣶⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⣰⣿⣿⣿⣿⡟⠁⠈⠀⣠⡏⠀⠀⢸⣿⠀⠀⢰⣿⡇⠀⠀⣿⡇⡀⠀⣿⡟⠀⠀⣿⣿⡄⠀⠘⢿⡿⠟⠙⢿⣿⣿
⣿⣿⣿⠇⠀⠀⠀⣼⣿⣿⣿⣿⣿⠁⠀⠀⣸⣿⡗⠀⠀⣾⣿⠀⠀⢸⣿⠀⠀⠀⠛⣿⡙⠄⠈⢢⠀⠀⣿⣿⣷⡀⠀⠀⠀⢀⣴⣿⣿⣿
⣿⣿⠏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⢰⣿⣿⡇⠀⠀⣿⣿⠀⠀⢸⣿⣆⠀⢀⣴⣿⣿⣶⣶⡿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠛⣿⠀⣀⣼⣿⣿⣿⣿⣿⠉⠛⠿⠿⠃⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣇⠀⢀⣴⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⠀⠀⠹⡿⠛⠁⢸⣿⡏⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣦⣄⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

boat = r"""
             ____
              ---|
  \/            /|     \/
               / |\
              /  | \        \/
             /   || \
            /    | | \
           /     | |  \
          /      | |   \
         /       ||     \
        /        /       \
       /________/         \
       ________/__________--/
 ~~~   \___________________/
         ~~~~~~~~~~       ~~~~~~~~
~~~~~~~~~~~~~     ~~~~~~~~~
                               ~~~~~~~~~
"""
# tprint("True Final Boss")

welcome_message = "Welcome to Fish or Flirt. In this game, you can fish\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nor flirt. Let's start!"

choose_class = "What class do you want be in? Do you want to be a:"

class_options = ["doctor", "neurosurgeon", "lawyer", "fisherman", "dentist", "psychologist", "magician", "Prime Minister of Canada", "Premier of Australia", "astronaut", "rocket scientist"]

after_class_input = "Well, I'm a computer, so I can't hear you. Maybe hit your keyboard harder next time. Well, you get no autonomy anyways, so you're a fishman now. Congrats.\n"

story_1 = "Let me set the scene. Once upon a time, a long long time ago, in a small little village, a fisherman was born.\nThat's you!\n" \
          "You came out of the womb with a fishing rod in your precious little hands. Your mother had to get a C-section just to get it out!" \
          " Poor mama-fisherman.\nOn that fateful day, a prophecy was discovered. " \
          "You alone are destined to defeat the monster of the deep.\nYour parents have trained you all of life for this."

get_name = "So now, we all know why you're here.\n" \
           "You wish to fish.\n" \
           "You want to warp a carp,\n" \
           "getta a betta, net a flounder ten-pounder, snag a daring red haring–\n" \
           "OK.\n" \
           "I'll stop embarrassing you.\n" \
           "Here.\n" \
           "Take a fishing rod,\n" \
           "and go wild kid.\nBut first. What is your name?\n"

random_encounter_crab = [
    "You were thoroughly enjoying the feeling of sand beneath your toes, until a crab decides your toes were looking at it the wrong way. The crab challenges you to a duel.",
    "You see a crab.\nYou are filled with hatred.\nThe crab is also filled with hatred.\nYou are hatred itself.\nThe crab one-ups you and decides that it is despisal.\nYou and the crab lock eyes and the first one to blink loses.",
    "Crab. What more should I say? Crab.",
    "You step forward, the crab steps forward.\nYou step left, and it, left.\nYou try to eurostep that fool, but you are no match for the agility of the magnificent crab, and gets your ankles broken.\nYou take immense damage to your pride (not a real stat).",
    "You see a crab. The crab sees you. It's too late to run, the only option for you now is to stand your ground,\nand FIGHT.",
    "Legend says that by defeating a crab, you can gain a crab's power. Do you desire to absorb the might of this crab?"
]

random_encounter_fisherman = [
    "You see another person, wearing a straw hat, holding a rod and a bucket in each hand.\nYou both startle and point and each other in excitement.\nNeither of you say a word, but the intent is clear.\nFISH.",
    "The only living being a fisherman hates more than a crab, is another fisherman. You see another fisherman.",
    "You see a person, with a fish. What a nice fish, you think. They see a person with a fish. What a nice fish, they think.",
    "You see a person with a rod, and a bucket.\nThere is no fish in their bucket.\nYou are filled with overwhelming pity for them.\nYou are filled with overwhelming self-superiority over them.\nThis is the start of your villain arc."
]

random_encounter_mermaid = [
    "Me-me-mermaid... Pretty.",
    "You see a person in the water! They may be drowning!\n"
    "You try to rush over towards them before you are met with many many many many many many many many many many many "
    "many many many many many many many many many many many many many many many many many many many many many many many "
    "many many teeth.\nWhew! It was only a mermaid.\nMermaids can't drown silly. Don't worry about it.",
    "There's a mermaid. It's a mermaid.",
    "'Wow!' You think, 'What a big fish!' A mermaid hits you for calling them derogatory terms."
]

no_encounter_land = [
    "I don't like sand. ( ｡ •̀ ᴖ •́ ｡) It's coarse and rough and irritating and it gets everywhere.",
    "WOW! CONGRATS! YOU FOUND\nseaweed... You found wet soggy seaweed... congrats",
    "What kind of fisherman stays landlocked! Go to the sea, you'll find nothing on this barren land.",
    "The 'racle hast possess'd me, I f'resee a prophecy...\nGasp! the young gudgeon'rman finds nothing h're!"
]

no_encounter_sea = [
    "You set forward on your little boat in search of bigger fish to fry, but to your demise, you catch not even a single fly",
    "You thought you saw a fish in this direction. Turns out you thought wrong.",
    "You throw out your fishing rod. It returns you a chewed through boot with a hole in the toe.",
    "You came, you saw, you left empty handed. Ain't no fish here pal!"
]

encounter_boat = "You see an old, but sturdy sailboat. It's well loved, with the signs of time decorating its sides.\n" \
                 "However, the paint was recently redone a brilliant white, and you could see that the sails have been changed.\n" \
                 "Beside the boat, an old fisherman sits, as if waiting for a friend.\nThe fisherman beckons you towards them, and gestures at their boat.\n" \
                 "Behemoth, it reads. A worthy aid to help you in your journey against the monsters of the sea.\n" \
                 "The old fisherman tips their straw hat, a twinkle shinning in their eyes, and walks away, humming a happy little tune."

acquired_boat = "You touch the boat, and you feel an energy pulse through you. You've gotten stronger, my young friend. " \
                "The hope of all those who've come before you empowers you on your journey."

encounter_island = "There's a small island in the midst of the angry waves. There's a forest of palm trees on that island.\n" \
                   "Through them, you think you can glimpse movement.\n" \
                   "You're not sure if it's friend or foe, but there's only one (or two) real choices anyways."

encounter_pirate = "You see a group of pirates, each with a two shovels in hand.\n\"Why are they all carrying two shovels?\" " \
                   "You ask yourself.\"WOW CAPT'N! YOU'RE ABSOLUTELY BILLY-ANT. " \
                   "DIGGING WITH TWO SHOVELS MAKES US SO MUCH MORE IF-FEET-SEE-ENT THAN ONLY DIGGING WITH ONE!\"\n" \
                   "Oh, what, interesting(?) pirates. " \
                   "You see a big map lying behind them, with \"LOCATION OF LEVIANTHAN\" scrawled in the most horrendous writing you've seen." \
                   "Actually, it's a wonder you were able to read it in the first place. To get to it, you must get through all the shovel carrying pirates. " \
                   "Good luc-\nOh. One of the pirates accidentally smacked all the other pirates in the head.\n...\nThat sure was a very very very loud noise." \
                   "All of them are now unconscious. I'm not even sure if all of them are breathing. " \
                   "Well then, 1 pirate isn't that hard to deal with. I'll feel bad for the poor pirate if I wished you luck. Go on then."

pirate_defeated = "You've successfully wooed the pirate. They swoon romantically and fall into your inventory.\nYou've acquired the location of the terror of the sea, the Leviathan."

encounter_leviathan = "Abandon hope all ye who enters here.\n" \
                      "For here lies the lair of Leviathan, ruler of the deep and vicious seas.\n" \
                      "If you unlucky sailors find yourselves in its maw, despair!\n" \
                      "<You have reached the final boss, the Leviathan! Are your stats high enough to fish or " \
                      "capture the heart of this fearsome foe? Take up your rod and find out!>"

leviathan_defeated_fish = "With your strong rod and amazing fishing skills, you've fished the Leviathan from the sea!\n" \
                          "I can't believe you even have enough bicep strength to do that! Amazing!\n" \
                          "You've fulfilled the prophecy, and your parents will finally love you, I mean what."

leviathan_defeated_flirt = "You should be jailed! Your irresistible charm and dashing good looks have stolen the Leviathan's heart.\n" \
                           "When talking with the Leviathan, you discovered that the only reason it was terrorizing the seas was because it had a terrible stomach ache.\n" \
                           "After giving the Leviathan drugs, I MEAN, asprin, it felt a lot better, and no longer terrorizes the sea.\n" \
                           "You and the Leviathan, and all the other animals and people you've wooed along the way now live happily ever after."

invalid_move_land = [
    "You can't step here!",
    "There's nothing for you here.",
    "The crabs look at you with disgust. What are you, stupid? You can't go there! Go somewhere else!",
    "Error 102. Test subject is attempting to breach the wall. Alert. Alert. Alert. Alert. Alert. Al-\n"
    "The crabs look at you with disgust. What are you, stupid? You can't go there! Go somewhere else!",
    "WOW! You found a fish!... Is that what you thought would happen? You think you're so clever huh. You fool. There's nothing here!!"
]

invalid_move_water = [
    "Careful there buddy! If you go over the edge you'll fall off this world!",
    "You look into the void.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe void looks back.\nYou should turn back",
    "Did you know that the world is actually a hemisphere laid onto of four elephants standing onto of a giant turtle? "
    "You should be careful going that way, you might fall off the earth and onto a turtle.",
    "The water current gently brings you back on your right path. There's a monster to slay, you know! You don't want to slay it? Well, I guess there's a monster to fish!"
]

invalid_move_island = [
    "I don't know how you got here. You can't even move incorrectly on this island. How did you manage to make an invalid move?",
    "Let's review our NUMBERS. 1 for NORTH. 2 for SOUTH. 3 for EAST. 4 for SOUTH. Try again.",
    "How did you get here again? We should change your name into little Alice Liddell. Stop following the White Rabbit and go."
]

start_fish = [
    "You throw your rod into the sea. The bobber creates small ripples in the water, growing larger as they expand outwards. You feel one with the sea.",
    "The ocean breeze gently blows across your face like soft and loving caress. You think you'll find good fish today.",
    "In the distance, you hear the call of seagulls. They too, are accompanying you in your fishing.",
    "You throw your rod into the sea. The ocean's crystalline surface breaks for a moment, before returning to its original calm.",
    "You hum a soft tune under your breath as you wait for a fish to take the bait. You're not sure where it came from, but it comforts your soul."
]

fishing_success = [
    "FSIH FISH FISHS FSIHDSF FSIFH FSIHF FISHF FISHF FISH. There's a fish.",
    "It's your lucky day! You've found a strange looking being with 21 limbs, "
    "oil and tar dripping from its skin and sliding onto the sea. It looks at you with beady, soulless eyes, "
    "and without knowing the reason, you are overcome with the desire to look away. But you must keep your eyes on it, "
    "after all, IT'S SUCH A COOL FISH!!",
    "You found a fish. Good job buddy.",
    "It looks like a fish, it smells like a fish, it sounds like a fish, it feels like a fish, it tastes like a fish.\nGasp!\nI think you've found a fish!"
]

fishing_fail = []

start_flirt = ""

flirt_dialogue = [
    "I wish you were a fish so I could reel you in.",
    "You’re the only fish in the sea for me.",
    "You know I don’t go fishing often, But you’re quite the catch!",
    "You’re like an award-winning fish",
    "A shark just ate my girlfriend during our fishing trip. Will you be my new one?",
    "Are you Swedish? 'Cause you the sweetest fish I sea."
]

flirt_harder_dialogue = [
    "Do you believe in love at first sight, or should I float by again?",
    "Hey baby, you wanna cast a line with me?",
    "I always knew the best catch of my life would be on this ocean.",
    "I can feel a lot of tension between us.",
    "If you were a fish, you’d be an Angelfish.",
    "You just reeled me in with your beauty.",
    "You’ve got me hook, line, and sinker."
]

invalid_flirt = "That's not flirting kid. You suck."

# different flirt success and fails for different flirt-able things
flirt_success_crab = ""

flirt_fail_crab = ""

flirt_success_fisherman = ""

flirt_fail_fisherman = ""

flirt_success_mermaid = ""

flirt_fail_mermaid = ""

flirt_success_whale = ""

flirt_fail_whale = ""

flirt_success_pirate = ""

flirt_fail_pirate = ""

flirt_success_leviathan = ""

flirt_fail_leviathan = ""

fish_for_fish = []

fish_for_mermaid = []

fish_for_whale = []

level_up = ""

# tprint("ERROR 102", "dirty")


def slow_print(dialogue):
    # prints a character at a time
    for char in dialogue:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
