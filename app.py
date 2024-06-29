import sys #poder parar meu codigo quando quiser sys.exit()
import datetime
import pygame #para implementar som
import random
from time import sleep #poder dar pausas no meu codigo sleep()
from dateutil.relativedelta import relativedelta # logica dos anos bisextos
import colorama  # dar cor no terminal
colorama.init()
pygame.init()
pygame.mixer.music.set_volume(0.05)
musica_fundo = pygame.mixer.music.load('musica_fundo.mp3')
som_perdeu = pygame.mixer.Sound('perdeu.wav')
som_acertar = pygame.mixer.Sound('coin.wav')
class cor:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
#------Geração do Personagem-------
#Utilize datetime para gerar uma data de nascimento aleatória dentro de um intervalo razoável (por exemplo, entre 1970 e 2000).
data_min = datetime.date(1970, 1, 1).toordinal()
data_max = datetime.date(2000, 1, 1).toordinal()
data_ordinal = random.randint(data_min, data_max)
data_aleatoria = datetime.date.fromordinal(data_ordinal)#data de aniversario do personagem
nomes_f = ["Maria", "Ana", "Joana", "Sofia", "Luísa", "Carolina", "Mariana", "Beatriz", "Inês", "Matilde", "Rita", "Diana", "Catarina", "Mafalda", "Helena", "Margarida", "Andreia", "Clara", "Teresa", "Laura"]
nomes_m = ["João", "Pedro", "António", "Miguel", "Manuel", "Carlos", "Francisco", "José", "Diogo", "Luís", "André", "Tiago", "Ricardo", "Daniel", "Bruno", "Tomás", "Nuno", "Rafael", "David", "Bartolomeu"]
#Crie características básicas para o personagem: Saúde, Riqueza e Felicidade. Todas começam em um valor médio arbitrário.
#------Inicio-----
print(cor.GREEN+"--------------------------------------BEM VINDO AO JOGO------------------------------------------"+cor.RESET)
print(cor.RED+"""
       ▄█  ▄▀▀▀▀▄   ▄▀▀▀▀▄    ▄▀▀▀▀▄       ▄▀▀█▄▄   ▄▀▀█▄       ▄▀▀▄ ▄▀▀▄  ▄▀▀█▀▄    ▄▀▀█▄▄   ▄▀▀█▄  
 ▄▀▀▀█▀ ▐ █      █ █         █      █     █ ▄▀   █ ▐ ▄▀ ▀▄     █   █    █ █   █  █  █ ▄▀   █ ▐ ▄▀ ▀▄ 
█    █    █      █ █    ▀▄▄  █      █     ▐ █    █   █▄▄▄█     ▐  █    █  ▐   █  ▐  ▐ █    █   █▄▄▄█ 
▐    █    ▀▄    ▄▀ █     █ █ ▀▄    ▄▀       █    █  ▄▀   █        █   ▄▀      █       █    █  ▄▀   █ 
  ▄   ▀▄    ▀▀▀▀   ▐▀▄▄▄▄▀ ▐   ▀▀▀▀        ▄▀▄▄▄▄▀ █   ▄▀          ▀▄▀     ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ █   ▄▀  
   ▀▀▀▀            ▐                      █     ▐  ▐   ▐                  █       █ █     ▐  ▐   ▐   
                                          ▐                               ▐       ▐ ▐                
"""+cor.RESET)
pygame.mixer.music.play(-1)#tocar musica de fundo
escolha_sexo = str(input("Escolha um personagem feminino ou masculino, digite"+ cor.YELLOW+"(f ou m):\n"+cor.RESET)).lower()
print("Criando data e nome para seu personagem...")
sleep(2)
if escolha_sexo == "f":
    nome = random.choice(nomes_f)
    print(f"O nome da sua guerreira é {cor.RED+nome+cor.RESET}, e ela nasceu em: {cor.MAGENTA+data_aleatoria.strftime('%d/%m/%Y')+cor.RESET}")
elif escolha_sexo == "m":
    nome = random.choice(nomes_m)
    print(f"O nome do seu guerreiro é {cor.RED+nome+cor.RESET}, e ele nasceu em: {cor.MAGENTA+data_aleatoria.strftime('%d/%m/%Y')+cor.RESET}")
else:
    pygame.mixer.music.stop()
    som_perdeu.play()
    print(cor.RED+"Por não digitar de maneira correta o que pedimos, você foi expulso do jogo!"+cor.RESET)
    sleep(7)
    sys.exit()
sleep(3)
print(cor.GREEN+"-----REGRAS DO JOGO-----"+cor.RESET)
print(f"Durante a vida de {cor.RED+nome+cor.RESET} acontecerão eventos, e você será responsável por prosseguir esses eventos ou rejeitá-los.\nPorém, seu personagem nasce com algumas características básicas, ambas com valor "+ cor.YELLOW+"50"+cor.RESET +", e ao final do jogo, de \nacordo com as suas escolhas, suas características serão totalmente alteradas!\nTente seguir uma vida boa! Bom jogo!")
print(cor.RED+"o jogo começara em breve..."+cor.RESET)
sleep(20)
print(cor.GREEN+"----- QUE COMEÇE O JOGO DA VIDA -----"+cor.YELLOW)
sleep(2)
#Etapas da Vida:
marcos_positivos_s = [
    f'{cor.RED+nome+cor.RESET}, seus amigos convidaram você para começar fazer academia!', 
    f'{cor.RED+nome+cor.RESET} completou sua primeira meia maratona!', 
    f'{cor.RED+nome+cor.RESET} está a 3 semanas sem comer porcarias!', 
    f'{cor.RED+nome+cor.RESET} pegou finalmente o hábito de dormir cedo todos os dias!']

marcos_positivos_r = [
    f'{cor.RED+nome+cor.RESET} comprou sua primeira cripto!',
    f'{cor.RED+nome+cor.RESET} já economizou mais de R$:300,00 esse mês em seu cofrinho!',
    f'{cor.RED+nome+cor.RESET} agora está estudando sobre ações',
    f'{cor.RED+nome+cor.RESET} montou um planilha de finança para controlar seus gastos!']

marcos_positivos_f = [
    f'{cor.RED+nome+cor.RESET} fez novos amigos incríveis e pretende manter contato!',
    f'{cor.RED+nome+cor.RESET} prometeu passar todos domingos ao lado da sua amada mamãe',
    f'{cor.RED+nome+cor.RESET} decidiu fazer sua tão amada viagem dos sonhos para Suíça!',
    f'{cor.RED+nome+cor.RESET} agora conheçeu seu verdadeiro amor e pretende se casar!']

marcos_positivos_i = [
    f'{cor.RED+nome+cor.RESET} começou meditar todos os dias antes de dormir',
    f'{cor.RED+nome+cor.RESET} agora le livros e reflete mais sobre a vida!',
    f'{cor.RED+nome+cor.RESET} está controlando seus sentimentos e tenta não se estressar facilmente',
    f'{cor.RED+nome+cor.RESET} agora conversa mais com Deus e busca orar frequentemente']


marcos_negativos_s = [
    f'{cor.RED+nome+cor.RESET} decidiu comer pizza todo final de semana', 
    f'{cor.RED+nome+cor.RESET} agora joga com seus amigos até 5 horas da manhã todos os dias', 
    f'{cor.RED+nome+cor.RESET} já não pratica esporte à 6 mesês', 
    f'{cor.RED+nome+cor.RESET} decidiu começar fumar um verde, pra desestressar']

marcos_negativos_r = [
    f'{cor.RED+nome+cor.RESET} decidiu comprar todos aqueles tênis caros que sempre teve vontade', 
    f'{cor.RED+nome+cor.RESET} agora ja não economiza, afinal cachão não tem gaveta!', 
    f'{cor.RED+nome+cor.RESET} está pensando em tacar o fds e comprar logo seu carro dos sonhos!', 
    f'{cor.RED+nome+cor.RESET} agora não tem dó mais de gastar dinheiro no shopping!']

marcos_negativos_f = [
    f'{cor.RED+nome+cor.RESET} decidiu não ter mais amigos e se afastar de todos!',
    f'{cor.RED+nome+cor.RESET} agora gosta de ouvir musicas que te deixam triste',
    f'{cor.RED+nome+cor.RESET} agora escuta os problemas dos outros e absorve para si mesmo',
    f'{cor.RED+nome+cor.RESET} decidiu não sair mais de casa se não for necessário!']

marcos_negativos_i = [
    f'{cor.RED+nome+cor.RESET} decidiu xingar todos que não te convêm',
    f'{cor.RED+nome+cor.RESET} começou a dirigir em alta velocidade sem se importar com o transito, para sentir adrenalina',
    f'{cor.RED+nome+cor.RESET} começou a praticar crimes, para dar mais emoção a sua vida',
    f'{cor.RED+nome+cor.RESET} decidiu treinar luta, e agora arruma briga durante a noite para praticar seus golpes!']

marcos_positivos_s = random.choice(marcos_positivos_s)
marcos_positivos_r = random.choice(marcos_positivos_r)
marcos_positivos_i = random.choice(marcos_positivos_i)
marcos_positivos_f = random.choice(marcos_positivos_f)

marcos_negativos_s = random.choice(marcos_negativos_s)
marcos_negativos_r = random.choice(marcos_negativos_r)
marcos_negativos_i = random.choice(marcos_negativos_i)
marcos_negativos_f = random.choice(marcos_negativos_f)

marcos18 = [marcos_positivos_r, marcos_positivos_i]
marcos30 = [marcos_positivos_f, marcos_negativos_s]
marcos40 = [marcos_negativos_f, marcos_negativos_r]
marcos50 = [marcos_negativos_i]
marcos60 = [marcos_positivos_s]


    #Defina marcos de vida aos 18, 30, 40, 50, 60 anos. Em cada marco, ocorrerá um evento significativo determinado aleatoriamente.
saude = 50
riqueza = 50
felicidade = 50
insanidade = 50

#marco de vida aos 18
print(cor.YELLOW+f"\n{nome}-''FINALMENTE {(data_aleatoria + relativedelta(years=18)).strftime('%d/%m/%Y')}''\nAgora {nome} completou seus tão esperado 18 anos e:\n"+cor.RESET)

event = random.choice(marcos18)
    
resposta = str(input(f"{event}\n Prossegue  ou  Rejeita  digite(p/r)").lower())
som_acertar.play()
#negativos
if event == marcos_negativos_s:
    if resposta == "p":
        saude = saude - 10
    elif resposta == "r":
        saude = saude + 10
if event == marcos_negativos_r:
    if resposta == "p":
        riqueza = riqueza - 10
    elif resposta == "r":
        riqueza = riqueza + 10
if event == marcos_negativos_f:
    if resposta == "p":
        felicidade = felicidade - 10
    elif resposta == "r":
        felicidade = felicidade + 10
if event == marcos_negativos_i:
    if resposta == "p":
        insanidade = insanidade - 10
    elif resposta == "r":
        insanidade = insanidade + 10
#positivos
if event == marcos_positivos_s:
    if resposta == "p":
        saude = saude + 10
    elif resposta == "r":
        saude = saude - 10
if event == marcos_positivos_r:
    if resposta == "p":
        riqueza = riqueza + 10
    elif resposta == "r":
        riqueza = riqueza - 10
if event == marcos_positivos_f:
    if resposta == "p":
        felicidade = felicidade + 10
    elif resposta == "r":
        felicidade = felicidade - 10
if event == marcos_positivos_i:
    if resposta == "p":
        insanidade = insanidade + 10
    elif resposta == "r":
        insanidade = insanidade - 10


#marco de vida aos 30
print(cor.YELLOW+f"\n{nome}-''{(data_aleatoria + relativedelta(years=30)).strftime('%d/%m/%Y')} Pois é, então 30toooooou''\nAgora {nome} completou seus 30 anos, a vida começa a dar forma, e:\n"+cor.RESET)

event = random.choice(marcos30)
    
resposta = str(input(f"{event}\n Prossegue  ou  Rejeita  digite(p/r)").lower())
som_acertar.play()

#negativos
if event == marcos_negativos_s:
    if resposta == "p":
        saude = saude - 10
    elif resposta == "r":
        saude = saude + 10
if event == marcos_negativos_r:
    if resposta == "p":
        riqueza = riqueza - 10
    elif resposta == "r":
        riqueza = riqueza + 10
if event == marcos_negativos_f:
    if resposta == "p":
        felicidade = felicidade - 10
    elif resposta == "r":
        felicidade = felicidade + 10
if event == marcos_negativos_i:
    if resposta == "p":
        insanidade = insanidade - 10
    elif resposta == "r":
        insanidade = insanidade + 10
#positivos
if event == marcos_positivos_s:
    if resposta == "p":
        saude = saude + 10
    elif resposta == "r":
        saude = saude - 10
if event == marcos_positivos_r:
    if resposta == "p":
        riqueza = riqueza + 10
    elif resposta == "r":
        riqueza = riqueza - 10
if event == marcos_positivos_f:
    if resposta == "p":
        felicidade = felicidade + 10
    elif resposta == "r":
        felicidade = felicidade - 10
if event == marcos_positivos_i:
    if resposta == "p":
        insanidade = insanidade + 10
    elif resposta == "r":
        insanidade = insanidade - 10

    
#marco de vida aos 40
print(cor.YELLOW+f"\n{nome}-''NOSSA!, hoje é meu aniversário, tinha até me esquecido...{(data_aleatoria + relativedelta(years=40)).strftime('%d/%m/%Y')}''\nAgora {nome} completou seus 40 anos, as dificuldades da vida já são nítidas e:\n"+cor.RESET)

event = random.choice(marcos40)
    
resposta = str(input(f"{event}\n Prossegue  ou  Rejeita  digite(p/r)").lower())
som_acertar.play()

#negativos
if event == marcos_negativos_s:
    if resposta == "p":
        saude = saude - 10
    elif resposta == "r":
        saude = saude + 10
if event == marcos_negativos_r:
    if resposta == "p":
        riqueza = riqueza - 10
    elif resposta == "r":
        riqueza = riqueza + 10
if event == marcos_negativos_f:
    if resposta == "p":
        felicidade = felicidade - 10
    elif resposta == "r":
        felicidade = felicidade + 10
if event == marcos_negativos_i:
    if resposta == "p":
        insanidade = insanidade - 10
    elif resposta == "r":
        insanidade = insanidade + 10
#positivos
if event == marcos_positivos_s:
    if resposta == "p":
        saude = saude + 10
    elif resposta == "r":
        saude = saude - 10
if event == marcos_positivos_r:
    if resposta == "p":
        riqueza = riqueza + 10
    elif resposta == "r":
        riqueza = riqueza - 10
if event == marcos_positivos_f:
    if resposta == "p":
        felicidade = felicidade + 10
    elif resposta == "r":
        felicidade = felicidade - 10
if event == marcos_positivos_i:
    if resposta == "p":
        insanidade = insanidade + 10
    elif resposta == "r":
        insanidade = insanidade - 10


#marco de vida aos 50
print(cor.YELLOW+f"\n{nome}-''{(data_aleatoria + relativedelta(years=50)).strftime('%d/%m/%Y')}... Xiii to ficando véi já''\nAgora {nome} completou seus 50 anos, as dorzinhas nas costas estão incomodando e:\n"+cor.RESET)

event = random.choice(marcos50)
    
resposta = str(input(f"{event}\n Prossegue  ou  Rejeita  digite(p/r)").lower())
som_acertar.play()

#negativos
if event == marcos_negativos_s:
    if resposta == "p":
        saude = saude - 10
    elif resposta == "r":
        saude = saude + 10
if event == marcos_negativos_r:
    if resposta == "p":
        riqueza = riqueza - 10
    elif resposta == "r":
        riqueza = riqueza + 10
if event == marcos_negativos_f:
    if resposta == "p":
        felicidade = felicidade - 10
    elif resposta == "r":
        felicidade = felicidade + 10
if event == marcos_negativos_i:
    if resposta == "p":
        insanidade = insanidade - 10
    elif resposta == "r":
        insanidade = insanidade + 10
#positivos
if event == marcos_positivos_s:
    if resposta == "p":
        saude = saude + 10
    elif resposta == "r":
        saude = saude - 10
if event == marcos_positivos_r:
    if resposta == "p":
        riqueza = riqueza + 10
    elif resposta == "r":
        riqueza = riqueza - 10
if event == marcos_positivos_f:
    if resposta == "p":
        felicidade = felicidade + 10
    elif resposta == "r":
        felicidade = felicidade - 10
if event == marcos_positivos_i:
    if resposta == "p":
        insanidade = insanidade + 10
    elif resposta == "r":
        insanidade = insanidade - 10


#marco de vida aos 60
print(cor.YELLOW+f"\n{(data_aleatoria + relativedelta(years=60)).strftime('%d/%m/%Y')}\nAgora {nome} tem 60 anos, está cansado, nem se lembra mais do seu aniversário, quer se aposentar logo e:\n"+cor.RESET)

event = random.choice(marcos60)
    
resposta = str(input(f"{event}\n Prossegue  ou  Rejeita  digite(p/r)").lower())
som_acertar.play()

#negativos
if event == marcos_negativos_s:
    if resposta == "p":
        saude = saude - 10
    elif resposta == "r":
        saude = saude + 10
if event == marcos_negativos_r:
    if resposta == "p":
        riqueza = riqueza - 10
    elif resposta == "r":
        riqueza = riqueza + 10
if event == marcos_negativos_f:
    if resposta == "p":
        felicidade = felicidade - 10
    elif resposta == "r":
        felicidade = felicidade + 10
if event == marcos_negativos_i:
    if resposta == "p":
        insanidade = insanidade - 10
    elif resposta == "r":
        insanidade = insanidade + 10
#positivos
if event == marcos_positivos_s:
    if resposta == "p":
        saude = saude + 10
    elif resposta == "r":
        saude = saude - 10
if event == marcos_positivos_r:
    if resposta == "p":
        riqueza = riqueza + 10
    elif resposta == "r":
        riqueza = riqueza - 10
if event == marcos_positivos_f:
    if resposta == "p":
        felicidade = felicidade + 10
    elif resposta == "r":
        felicidade = felicidade - 10
if event == marcos_positivos_i:
    if resposta == "p":
        insanidade = insanidade + 10
    elif resposta == "r":
        insanidade = insanidade - 10

print(cor.CYAN+f"Após um longa vida cheio de marcos inesquecíveis, {nome} decide se aposentar...\nporém aos 63 anos {nome} falece em seu aniversário, e agora sim podemos dizer\n"+cor.RESET + cor.RED+"FIM DE JOGO!"+cor.RESET)
pygame.mixer.music.stop()
som_perdeu.play()
print(cor.MAGENTA+f"{nome} nasceu em: {data_aleatoria.strftime('%d/%m/%Y')}\nmorreu em: {(data_aleatoria + relativedelta(years=63)).strftime('%d/%m/%Y')}"+cor.RESET)
if saude > 50:
    print(f"Saúde:{saude}, {nome} teve uma vida muito "+cor.GREEN+"SAUDÁVEL"+cor.RESET)
elif saude == 50:
    print(f"Saúde:{saude}, {nome} teve uma vida "+cor.YELLOW+"saudável"+cor.RESET)
else:
    print(f"Saúde:{saude}, {nome} teve uma saúde de "+cor.RED+"bosta"+cor.RESET)

if felicidade > 50:
    print(f"Felicidade:{felicidade}, {nome} teve uma vida muito "+cor.GREEN+"FELIZ"+cor.RESET)
elif felicidade == 50:
    print(f"Felicidade:{felicidade}, {nome} teve uma vida "+cor.YELLOW+"feliz"+cor.RESET)
else:
    print(f"Felicidade:{felicidade}, {nome} teve uma tristeza "+cor.RED+"absurda"+cor.RESET)

if riqueza > 50:
    print(f"Riqueza:{riqueza}, {nome} foi "+cor.GREEN+"MILIONÁRIA"+cor.RESET)
elif riqueza == 50:
    print(f"Riqueza:{riqueza}, {nome} teve uma vida financeira "+cor.YELLOW+"normal"+cor.RESET)
else:
    print(f"Riqueza:{riqueza}, {nome} foi super "+cor.RED+"pobreta"+cor.RESET)

if insanidade > 50:
    print(f"Insanidade:{insanidade}, {nome} viveu totalmente em "+cor.GREEN+"PAZ"+cor.RESET)
elif insanidade == 50:
    print(f"Insanidade:{insanidade}, {nome} teve uma vida emocional "+cor.YELLOW+"normal"+cor.RESET)
else:
    print(f"Insanidade:{insanidade}, {nome} foi considerada uma pessoa completamente "+cor.RED+"retardada"+cor.RESET)

sleep(30)