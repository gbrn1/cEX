import random

def banner():
    banners = [r"""             //   / / \\ / / 
    ___     //____     \  /  
  //   ) ) / ____      / /   
 //       //          / /\\  
((____   //____/ /   / /  \\ 
""",
r"""63 45 58""",
r"""       EEEEEEE XX    XX 
  cccc EE       XX  XX  
cc     EEEEE     XXXX   
cc     EE       XX  XX  
 ccccc EEEEEEE XX    XX""",
 r"011000110100010101011000",
 r"""      _____  __
 ____/ __/ |/_/
/ __/ _/_>  <  
\__/___/_/|_|""",
r"""   ___                        .           .____                .                            
 .'   \ .___  ,    .  \,___, _/_     __.  /      _  .- \,___,  |     __.  .___    ___  .___ 
 |      /   \ |    `  |    \  |    .'   \ |__.    \,'  |    \  |   .'   \ /   \ .'   ` /   \
 |      |   ' |    |  |    |  |    |    | |       /\   |    |  |   |    | |   ' |----' |   '
  `.__, /      `---|. |`---'  \__/  `._.' /----/ /  \  |`---' /\__  `._.' /     `.___, /    
               \___/  \                                \                                    """]
    
    print(random.choice(banners) + '\n')

