#Cores no terminal
#\033[style;text;backgroundm -> representação de cores no Python
#\033[0;33;44m -> exemplo de representação 

#Style

#0(none) -> Sem estilo nenhum
#1(bold) -> coloca o texto em negrito 
#4(underline) -> sublinha o texto
#7(negative) -> inverte as configurações, o que foi pra fundo vai pra letra e vice versa

#//Text

#30 -> branco
#31 -> vermelho
#32 -> verde
#33 -> amarelo
#34 -> azul
#35 -> magenta
#36 -> ciano
#37 -> cinza

#Back

#40 -> branco
#41 -> vermelho
#42 -> verde
#43 -> amarelo
#44 -> azul
#45 -> magenta
#46 -> ciano
#47 -> cinza

#Exemplos

#teste(branco com fundo vermelho) -> \033[0;30;41m
#teste(azul com fundo amarelo e sublinhada) -> \033[4;33;44m
#teste(roxo com fundo amarelo e em negrito) -> \033[1;35;43m
#teste(cinza com fundo verde) -> \033[30:42m
#teste(cinza com fundo preto) -> \033[m
#teste(preta com fundo branco) -> \033[7;30m

print('\033[0mOla mundo')
