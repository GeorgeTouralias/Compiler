import os
import sys

alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']

file= open('check_pinakas.cpy','r',encoding='utf8')


#Xaraktires pinaka metavasewn

white_char=0
letters=1
num=2
plus=3
minus=4
multiply=5
divide=6
equal=7
less_than=8
greater_than=9
EOF=10
oxi_apodekto_simvolo=11
koma=12
erwtimatiko=13
arist_parenthesi=14
deksia_parenthesi=15
arist_agkili=16
deksia_agkili=17
anoigma_block=18
kleisimo_block=19
allagi_grammis= 20
anwkatw_teleia=21
hashtag=22
dollar=23
quotes=24
katw_paula=25
thaumastiko=26

#Katastaseis

katastasi_start=0
katastasi_letter=1
katastasi_num=2
katastasi_lessthan=3
katastasi_greaterthan=4
katastasi_ison=5
katastasi_hashtag=6
katastasi_sxolia=7
katastasi_kleinei_hashtag=8
katastasi_divide=9
katastasi_thaumastiko=10

#Tokens

id_tk=30
num_tk=31
plus_tk=32
minus_tk=33
multiply_tk=34
divide_tk=35
equal_tk=36
lessthan_tk=37
greaterthan_tk=38
EOF_tk=39
koma_tk=41
erwtimatiko_tk=42
arist_parenthesi_tk=43
deksia_parenthesi_tk=44
arist_agkili_tk=45
deksia_agkili_tk=46
anoigma_block_tk=47
kleisimo_block_tk=48
lessORequal_tk=49
greaterORequal_tk=50
anwkatw_teleia_tk=51
anathesi_tk=52
diaforo_tk=53
quotes_tk=54
hashtag_tk=55


#DESMEUMENES LEKSEIS PROGRAMMATOS

desmeumenes_lexeis=['def' ,'#declare','if','else','while','return',
                    'and','or','not','input','print','int','__name__','__main__']
                                        
                                        

def_tk=100
declare_tk=101
if_tk=102
else_tk=103
while_tk=104
return_tk=105
and_tk=106
or_tk=107
not_tk=108
input_tk=109
print_tk=110
int_tk=111
name_tk=112
main_tk=113

#Errors

ERROR_MH_APODEKTO_SYMBOLO=-1
ERROR_PSIFIO_GRAMMA=-2
ERROR_ARITHMOS_EKTOS_DIASTHMATOS=-3
ERROR_PANW_APO_30_CHARAKTIRES=-4
ERROR_ANOIGMA_SXOLIWN_ME_EOF=-5
ERROR_DOLLARIO_MONO_TOU=-6
ERROR_SLASH_MONO_TOU=-7
ERROR_LEFT_AGGISTRO_MONO_TOU=-8
ERROR_RIGHT_AGGISTRO_MONO_TOU=-9
ERROR_ID_KSEKINA_ME_KATW_PAYLA=-10
ERROR_HASHTAG_MONO_TOU=-11
ERROR_THAUMASTIKO_MONO_TOU=-12

pinakas_metavasewn=[
    #katastasi_start
        [katastasi_start,katastasi_letter,katastasi_num,plus_tk,minus_tk,multiply_tk, katastasi_divide,
         katastasi_ison,katastasi_lessthan,katastasi_greaterthan,EOF_tk,ERROR_MH_APODEKTO_SYMBOLO,
         koma_tk,erwtimatiko_tk,arist_parenthesi_tk,deksia_parenthesi_tk,arist_agkili_tk,deksia_agkili_tk,ERROR_LEFT_AGGISTRO_MONO_TOU,ERROR_RIGHT_AGGISTRO_MONO_TOU,
         katastasi_start,anwkatw_teleia_tk,katastasi_hashtag,ERROR_DOLLARIO_MONO_TOU,quotes_tk,katastasi_letter,katastasi_thaumastiko],
        
    #katastasi_letter
        [id_tk,katastasi_letter,katastasi_letter,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,ERROR_MH_APODEKTO_SYMBOLO,
         id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,id_tk,katastasi_letter,id_tk],
        
    #katastasi_num
        [num_tk,ERROR_PSIFIO_GRAMMA, katastasi_num,num_tk,num_tk,num_tk,
         num_tk,num_tk,num_tk,num_tk,num_tk,ERROR_MH_APODEKTO_SYMBOLO,
         num_tk,num_tk,num_tk,num_tk,num_tk,num_tk,num_tk,num_tk,
         num_tk,num_tk,num_tk,num_tk,num_tk,num_tk,num_tk],

    #katastasi_lessthan
        [lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,
         lessthan_tk,lessORequal_tk,lessthan_tk,lessthan_tk,lessthan_tk,ERROR_MH_APODEKTO_SYMBOLO,
         lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,
         lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk,lessthan_tk],

    #katastasi_greaterthan
        [greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,
         greaterthan_tk,greaterORequal_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,ERROR_MH_APODEKTO_SYMBOLO,
         greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,
         greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk,greaterthan_tk],

     #katastasi_ison
        [anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,
         anathesi_tk,equal_tk,anathesi_tk,anathesi_tk,anathesi_tk,ERROR_MH_APODEKTO_SYMBOLO,
         anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,
         anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk,anathesi_tk],

     #katastasi_hashtag
        [ERROR_HASHTAG_MONO_TOU,katastasi_letter,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,
         ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_MH_APODEKTO_SYMBOLO,
         ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,anoigma_block_tk,kleisimo_block_tk,
         ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,katastasi_sxolia,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU,ERROR_HASHTAG_MONO_TOU],

     #katastasi_sxolia
        [katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,ERROR_ANOIGMA_SXOLIWN_ME_EOF,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_kleinei_hashtag,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia],

     #katastasi_kleinei_hashtag
        [katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,ERROR_ANOIGMA_SXOLIWN_ME_EOF,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia,
         katastasi_sxolia,katastasi_sxolia,katastasi_kleinei_hashtag,katastasi_start,katastasi_sxolia,katastasi_sxolia,katastasi_sxolia],

     #katastasi_divide
        [ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,
         divide_tk,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_MH_APODEKTO_SYMBOLO,
         ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,
         ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU,ERROR_SLASH_MONO_TOU],

     #katastasi_thaumastiko
        [ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,
         ERROR_THAUMASTIKO_MONO_TOU,diaforo_tk,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_MH_APODEKTO_SYMBOLO,
         ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,
         ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU,ERROR_THAUMASTIKO_MONO_TOU]

        ]

                

line=1


def lex():
        global line
        prod_wrd=''
        current= katastasi_start
        
        linecounter= line
        resultlex=[]
        while(current>=0 and current<=10):
                char = file.read(1)

                if (char == ' ' or char == '\t'):
                        char_tk = white_char
                elif (char in alphabet):
                        char_tk = letters
                elif (char in numbers):
                        char_tk = num
                elif (char == '+'):
                        char_tk = plus
                elif (char == '-'):
                        char_tk = minus
                elif (char == '*'):
                        char_tk = multiply
                elif (char == '/'):
                        char_tk = divide
                elif(char == '='):
                        char_tk = equal
                elif (char == '<'):
                        char_tk = less_than
                elif (char == '>'):
                        char_tk = greater_than
                elif (char == ':'):
                        char_tk = anwkatw_teleia
                elif (char == ','):
                        char_tk = koma
                elif (char == ';'):
                        char_tk = erwtimatiko
                elif (char == '('):
                        char_tk = arist_parenthesi
                elif (char == ')'):
                        char_tk = deksia_parenthesi
                elif (char == '['):
                        char_tk = arist_agkili
                elif (char == ']'):
                        char_tk = deksia_agkili
                elif (char == '{'):
                        char_tk = anoigma_block
                elif (char == '}'):
                        char_tk = kleisimo_block
                elif (char == '\n'):
                        linecounter=linecounter+1
                        char_tk = allagi_grammis
                elif (char == ''):  # H EOF tha epistrepsei sto telos tou arxeiou   to  ''
                        char_tk = EOF
                elif (char == '.'):
                        char_tk = teleia
                elif (char == '#'):
                        char_tk = hashtag
                elif (char == '$'):
                        char_tk = dollar
                elif (char == '"'):
                        char_tk = quotes
                elif (char == '_'):
                        char_tk = katw_paula
                elif (char == '!'):
                        char_tk = thaumastiko
                else:
                        char_tk = oxi_apodekto_simvolo

                #print('Trexousa katastasi ', current )
                #print('Vlepo xaraktira ', char )
                
                current=pinakas_metavasewn[current][char_tk]
                
                #print('Nea katastasi ', current)
                #input("Press Enter to continue...")
                
                if(len(prod_wrd)<30):
                        if(current!=katastasi_start and current!=katastasi_sxolia and current!=katastasi_kleinei_hashtag):
                              prod_wrd+=char
                        else:
                              prod_wrd=''

                else:
                        current=ERROR_PANW_APO_30_CHARAKTIRES


#Mexri edw exw brei token!!!!!!!

        if(current==id_tk or current==num_tk or current==lessthan_tk or current==greaterthan_tk or current==anathesi_tk):
                if (char == '\n'):
                        linecounter -= 1
                char=file.seek(file.tell()-1,0)  #epistrefei to teleutaio char pou diabase sto File (px avd+)

                prod_wrd = prod_wrd[:-1]        #kovei to +

        if(current==id_tk):
                if(prod_wrd in desmeumenes_lexeis):
                        if(prod_wrd=='def'):
                                current=def_tk
                        elif(prod_wrd=='#declare'):
                                current=declare_tk
                        elif (prod_wrd == 'if'):
                                current = if_tk
                        elif (prod_wrd == 'else'):
                                current = else_tk
                        elif (prod_wrd == 'while'):
                                current = while_tk
                        elif (prod_wrd == 'and'):
                                current = and_tk
                        elif (prod_wrd == 'or'):
                                current = or_tk
                        elif (prod_wrd == 'not'):
                                current = not_tk
                        elif (prod_wrd == 'input'):
                                current = input_tk
                        elif (prod_wrd == 'int'):
                                current = int_tk
                        elif (prod_wrd == 'print'):
                                current = print_tk
                        elif (prod_wrd == 'return'):
                                current = return_tk
                        elif (prod_wrd == '__name__'):
                                current = name_tk
                        elif (prod_wrd == '__main__'):
                                current = main_tk
                elif (prod_wrd[0] == '_'):
                     current=ERROR_ID_KSEKINA_ME_KATW_PAYLA


        #PERIORISMOS ARITHMOU PSIFIWN ALLA KAI TOU DIASTHMATOS [-32767,32767]
        if (current == num_tk):
                if (int(prod_wrd) >= pow(2,32)):
                    current = ERROR_ARITHMOS_EKTOS_DIASTHMATOS

        #ELEGXOS TWN ERRORS
        if(current==ERROR_MH_APODEKTO_SYMBOLO):
                print("ERROR: Exoume mh apodekto symbolo glwssas")
        elif(current==ERROR_PSIFIO_GRAMMA):
                print("ERROR: Akolouthei gramma meta apo kapoio psifio")
        elif(current==ERROR_ARITHMOS_EKTOS_DIASTHMATOS):
                print("ERROR: O arithmos den einai sto diasthma [-(2^32-1),2^32-1]")
        elif(current==ERROR_ANOIGMA_SXOLIWN_ME_EOF):
                print("ERROR: Ta sxolia /* anoi3an swsta alla den ekleisan sto telos tou arxeiou")
        elif(current==ERROR_PANW_APO_30_CHARAKTIRES):
                print("ERROR: H leksi exei panw apo 30 charaktires")
        elif(current==ERROR_DOLLARIO_MONO_TOU):
                print("ERROR: H leksi einai ena $ mono tou")
        elif(current==ERROR_SLASH_MONO_TOU):
                print("ERROR: H leksi einai ena / mono tou")
        elif(current==ERROR_LEFT_AGGISTRO_MONO_TOU):
                print("ERROR: H leksi einai ena { mono tou")
        elif(current==ERROR_RIGHT_AGGISTRO_MONO_TOU):
                print("ERROR: H leksi einai ena } mono tou")
        elif(current==ERROR_ID_KSEKINA_ME_KATW_PAYLA):
                print("ERROR: H leksi de ginetai na ksekina me _")
        elif(current==ERROR_HASHTAG_MONO_TOU):
                print("ERROR: H leksi einai ena # mono tou")
        elif(current==ERROR_THAUMASTIKO_MONO_TOU):
                print("ERROR: H leksi einai ena ! mono tou")


        #STIN THESH 0 TOY PINAKA EXOUME TO TOKEN
        #STIN THESH 1 TOY PINAKA EXOUME THN LEXH POU SXHMATISE O LEKTIKOS ANALYTHS
        #STIN THESH 2 TOY PINAKA EXOUME TON ARITHMO GRAMMHS

        resultlex.append(current)
        resultlex.append(prod_wrd)
        resultlex.append(linecounter) #oxi aparaithto
        line=linecounter

        print(resultlex)
        #input("Press Enter to continue.")
        return resultlex

'''
while(1):
        lexres = lex()
        if (lexres[0] == EOF_tk):
                break
        #print(lexres)
'''

# Endiamesos kodikas

global listOfAllQuads		#lista me Oles tis tetrades pou tha paraxthoun apo to programma.
listOfAllQuads = []
countQuad = 1				#O arithmos pou xarakthrizei thn tetrada. Brisketai mprosta apo thn 4ada.
def nextQuad():
	'Epistrefei ton arithmo ths epomenhs tetradas pou prokyptei otan paraxthei.'
	global countQuad
	
	return countQuad
def genQuad(first, second, third, fourth):
	'Dhmiourgei thn epomenh 4ada.'
	'Prwto stoixeio sth lista tha balw ton arithmo ths nextQuad(), ousiastika tha ginei 5ada.'
	global countQuad
	global listOfAllQuads
	list = []
	
	list = [nextQuad()]			#Bazw prwta ton arithmo.
	list += [first] + [second] + [third] + [fourth]		#Epeita ta orismata
	
	countQuad +=1	#Ayksanw kata 1 ton arithmo ths epomenhs 4adas.
	listOfAllQuads += [list] 	#Put quad in global listOfAllQuads.
	return list

T_i = 1
listOfTempVariables = []
def newTemp():
	'Dhmiourgei kai epistrefei mia nea proswrinh metablhth, ths morfhs T_1, T_2,.. .'
	global T_i
	global listOfTempVariables
	
	list = ['T_']
	list.append(str(T_i))
	tempVariable="".join(list)
	T_i +=1

	ent = Entity()								#Create an Entity
	ent.type = 'TEMP'							#
	ent.name = tempVariable						#
	ent.tempVar.offset = compute_offset()		#
	new_entity(ent)								#

	return tempVariable
def emptyList():
	'Dhmiourgei mia kenh lista etiketwn 4dwn.'
	pointerList = []	#Arxikopoihsh pointer list.
	
	return pointerList
def makeList(x):
	'Dhmiourgei mia lista etiketwn tetradwn pou periexei mono to x.'
	
	listThis = [x]
	
	return listThis
def merge(list1, list2):
	'Dhmiourgei mia lista etiketwn 4dwn apo th synenwsh listwn list1, list2.'
	list=[]
	list += list1 + list2

	return list
def backPatch(list, z):
	'H lista "list" apoteleitai apo deiktes se tetrades ths listOfAllQuads, twn opoiwn to teleytaio teloumeno Den einai symplhrwmeno.'
	'H backPatch episkeptetai mia mia tis 4des aytes kai tis symplhrwnei me thn etiketa z.'
	'''Prepei na sarwsw th listOfAllQuads kai gia kathe 4ada, pou exei prwto teloumeno arithmo
		pou periexetai sthn list:
		Otan briskw '_' sto 4o teloumeno twn 4dwn aytwn,
		tha to symbplhrwsw me to "z".
	'''
	global listOfAllQuads
	
	for i in range(len(list)):
		for j in range(len(listOfAllQuads)):
			if(list[i]==listOfAllQuads[j][0] and listOfAllQuads[j][4]=='_'):
				listOfAllQuads[j][4] = z
				break;	#to pass second loop faster and enter next i.
	return

###############################################################################
#	Synarthseis PINAKA SYMBOLWN:											  #
###############################################################################	
class Argument():
	' /_\  <- Trigwno'
	def __init__(self):
		self.name = ''		#Dinw to name gia na kserw poio Argument einai.
		self.type = 'Int'	#All variables in this language will be Int.
class Entity():
	' _ _ 				 '
	'|___|	<- Orthogwnio'

	def __init__(self):
		self.name = ''			#Dinw to name gia na kserw poio Entity einai.
		self.type = ''			#  'VAR' or 'SUBPR' or 'PARAM' or 'TEMP'
		# oi 4 katigories
		self.variable = self.Variable()
		self.subprogram = self.SubProgram()
		self.parameter = self.Parameter()
		self.tempVar = self.TempVar()
		
	class Variable: # metavliti
		def __init__(self):
			self.type = 'Int'           # DE xreiazetai
			self.offset = 0				# Apostash apo thn arxh ths stoibas.
	class SubProgram: # ypoprogramma			
		def __init__(self):
			self.type = 'Function'				# DE xreiazetai
			self.startQuad = 0			# H proti tetrada tis (apo ton endiameso).
			self.frameLength = 0		# To mhkos eggrafhmatos drasthriopoihshs.
			self.argumentList = []			#h lista parametrwn (gia na apothikeuso ta TRIGONA)
			
	class Parameter: # parametros
		def __init__(self):
			self.mode = 'CV'				# DE xreiazetai
			self.offset = 0				# Apostash apo thn arxh ths stoibas.
	class TempVar: # prosorini metavliti
		def __init__(self):
			self.type = 'Int'			# DE xreiazetai
			self.offset = 0				# Apostash apo thn arxh ths stoibas.
class Scope():
	'(_)  <- Kyklos'
	def __init__(self):
		self.name = ''						#Dinw to name gia na kserw poio Scope einai.
		self.entityList = []		#h lista apo entities
		self.nestingLevel = 0				# Bathos fwliasmatos.
		self.enclosingScope = None			#DEN to exei ms teams

def new_argument(object): # ftiahno argument= TRIGONO(galazio)
	'Add given object to list'
	global topScope
	
	# entityList[-1] (to teleutaio entity = subprogram (function h' procedure)
	topScope.entityList[-1].subprogram.argumentList.append(object) #add object(TRIGONO) to subprogram.argumentList
	
def new_entity(object):  # ftiahno entity= ORTHOGONIO(kitrino)
	'Add given object to list'
	global topScope
	
	topScope.entityList.append(object)  # sximatika, vazei sto TELOS tis grammis teleutaio to NEO entity (orthogonio)

topScope = None 	#einai to pio PANW scope kathe stigmi

def new_scope(name):  # ftiahno KIKLO(kokkino)
	'create new scope'
	global topScope

	nextScope = Scope()   
	nextScope.name = name
	nextScope.enclosingScope=topScope

	if(topScope == None): #arxika None(null)
		nextScope.nestingLevel = 0
	else:
		nextScope.nestingLevel = topScope.nestingLevel + 1

	topScope = nextScope

def delete_scope(): # svino KIKLO(kokkino)
	global topScope
	
	freeScope = topScope
	topScope = topScope.enclosingScope 
	del freeScope

def compute_offset():
	'Computes how many bytes '
	global topScope
	
	counter=0
	if(topScope.entityList is not []):  # an eho ESTO 1 entity (orthogonio)
		for ent in (topScope.entityList):  # pigaino se OLA ta entities (orthogonia) tis grammis(optika) pou vriskomai
			if(ent.type == 'VAR' or ent.type == 'TEMP' or ent.type=='PARAM'):  # OXI 'SUBPR' = YPOPROGRAMMA (den exei offset)
				counter +=1  # counter posa orthogonia vrika (horis YPOPROGRAMMA)
	#SizeOf Int variable = 4 and 'Fixed starting size': 3*4=12
	offset = 12+(counter*4)   #12 reserved
	
	return offset

def compute_startQuad():  # kaleite stin "block" META to "begin_block"
	'Compute startQuad (=current Quad) of function or procedure.'
	global topScope
	
	#sto apo katw scope(kiklos) sto teleytaio entity (orthogonio einai subprogram) kai enimeronei to startQuad
	topScope.enclosingScope.entityList[-1].subprogram.startQuad = nextQuad()
		
def compute_framelength(): # kaleite stin "block" PRIN to "end_block"
	'Compute frameLength of function or procedure.'
	global topScope
	
	#sto apo katw scope(kiklos) sto teleytaio entity (orthogonio einai subprogram) kai enimeronei to frameLength (sximatika print-screens)
	topScope.enclosingScope.entityList[-1].subprogram.frameLength = compute_offset()
	
def add_parameters():  # kaleite stin "block" amesos META tin "new_scope" kai metatrepei ta TRIGONA(orismata tis apo katw grammis) se ORTHOGONIA (stin panw-NEA grammi)
	'Create Entities of Parameters of functions or procedures. (ec. in a, inout b)'
	global topScope
	
	for arg in topScope.enclosingScope.entityList[-1].subprogram.argumentList: # gia kathe trigwno
		ent = Entity() 
		ent.name = arg.name
		ent.type = 'PARAM'
		ent.parameter.mode = 'CV'
		ent.parameter.offset = compute_offset()
		new_entity(ent)

def print_Symbol_table():
	'Prints Symbol-Table: Scopes, Entities, Arguments'
	global topScope
	
	print("########################################################################################")
	print("")

	sco=topScope
	while sco != None:
		print("SCOPE: "+"name:"+sco.name+" nestingLevel:"+str(sco.nestingLevel))
		print("\tENTITIES:")
		for ent in sco.entityList:
			if(ent.type == 'VAR'):
				print("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t variable-type:"+ent.variable.type+"\t offset:"+str(ent.variable.offset))
			elif(ent.type == 'TEMP'):
				print("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t temp-type:"+ent.tempVar.type+"\t offset:"+str(ent.tempVar.offset))
			elif(ent.type == 'SUBPR'):
				#if(ent.subprogram.type == 'Function'):
					print("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t function-type:"+ent.subprogram.type+"\t startQuad:"+str(ent.subprogram.startQuad)+"\t frameLength:"+str(ent.subprogram.frameLength))
					print("\t\tARGUMENTS:")
					for arg in ent.subprogram.argumentList:
						print("\t\tARGUMENT: "+" name:"+arg.name+"\t type:"+arg.type+"\t parMode:"+arg.parMode)
			elif(ent.type == 'PARAM'):
				print("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t mode:"+ent.parameter.mode+"\t offset:"+str(ent.parameter.offset))
		sco = sco.enclosingScope

	print("########################################################################################")

#Syntaktikos Analyths

def syntax_an():
        global line
        global lexres
        lexres= lex()
        line = lexres[2]

        def startRule():

            new_scope('main') # gia tin kentriki main (prin ksekinisoyn oi alles main)

            def_main_part()
            call_main_part()


        def def_main_part():
            global lexres
            
            def_main_function()
            while(lexres[0] == def_tk):
                 def_main_function()

        def def_main_function():
                global line 
                global lexres
                
                if(lexres[0] == def_tk):
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == id_tk):
                                name = lexres[1]
                                lexres = lex()
                                line = lexres[2]

                                if(lexres[0] == arist_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]
                        
                                        if(lexres[0] == deksia_parenthesi_tk):
                                                lexres = lex()
                                                line = lexres[2]
                                                
                                                if(lexres[0] == anwkatw_teleia_tk):
                                                      lexres = lex()
                                                      line = lexres[2]
                                
                                                      if(lexres[0] == anoigma_block_tk):
                                                          lexres = lex()
                                                          line = lexres[2]

                                                          ent = Entity()						#Create an Entity
                                                          ent.type = 'SUBPR'					#
                                                          ent.name = name					#
                                                          ent.subprogram.type = 'Function'	#
                                                          new_entity(ent)						#

                                                          new_scope(name)

                                                          declarations()
                                                          while(lexres[0] == def_tk):
                                                              def_function()

                                                          genQuad('begin_block',name,'_','_')
                                                          compute_startQuad()
                                                          statements()
                                                          compute_framelength()
                                                          genQuad('end_block',name,'_','_')

                                                          print_Symbol_table()
                                                          os.system("pause")

                                                          delete_scope()

                                                          if(lexres[0] == kleisimo_block_tk):
                                                              lexres = lex()
                                                              line = lexres[2]
                                                          else:
                                                              print("ERROR: Den yparxei #} meta ta statements kapoias main",line)
                                                              exit(-1)
                                                      else:
                                                           print("ERROR: Den yparxei #{ prin ta declarations kapoias main",line)
                                                           exit(-1)
                                                else:
                                                      print("ERROR: Den yparxei : meta apo () kapoias main",line)
                                                      exit(-1)
                                        else:
                                                print("ERROR: Den kleinei h deksia parenthesi meta apo onoma kapoias main",line)
                                                exit(-1)
                                else:
                                        print("ERROR: Den anoigei h aristeri parenthesi meta apo onoma kapoias main",line)
                                        exit(-1)

                        else:
                                print("ERROR: Den yparxei onoma main",line)
                                exit(-1)
                else:
                         print("ERROR: H leksi def den yparxei stin arxi tou programmatos",line)
                         exit(-1)
                        
                        
        def def_function():
                global line 
                global lexres
                
                if(lexres[0] == def_tk):
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == id_tk):
                                name = lexres[1]
                                lexres = lex()
                                line = lexres[2]

                                if(lexres[0] == arist_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]

                                        ent = Entity()						#Create an Entity
                                        ent.type = 'SUBPR'					#
                                        ent.name = name					#
                                        ent.subprogram.type = 'Function'	#
                                        new_entity(ent)						#

                                        id_list(0) # parametroi
                        
                                        if(lexres[0] == deksia_parenthesi_tk):
                                                lexres = lex()
                                                line = lexres[2]
                                                
                                                if(lexres[0] == anwkatw_teleia_tk):
                                                      lexres = lex()
                                                      line = lexres[2]
                                
                                                      if(lexres[0] == anoigma_block_tk):
                                                          lexres = lex()
                                                          line = lexres[2]

                                                          new_scope(name)
                                                          add_parameters()

                                                          declarations()
                                                          while(lexres[0] == def_tk):
                                                              def_function()

                                                          genQuad('begin_block',name,'_','_')
                                                          compute_startQuad()
                                                          statements()
                                                          compute_framelength()
                                                          genQuad('end_block',name,'_','_')

                                                          print_Symbol_table()
                                                          os.system("pause")

                                                          delete_scope()

                                                          if(lexres[0] == kleisimo_block_tk):
                                                              lexres = lex()
                                                              line = lexres[2]
                                                          else:
                                                              print("ERROR: Den yparxei #} meta ta statements kapoias function",line)
                                                              exit(-1)
                                                      else:
                                                           print("ERROR: Den yparxei #{ prin ta declarations kapoias function",line)
                                                           exit(-1)
                                                else:
                                                      print("ERROR: Den yparxei : meta apo () kapoias function",line)
                                                      exit(-1)
                                        else:
                                                print("ERROR: Den kleinei h deksia parenthesi meta apo onoma kapoias function",line)
                                                exit(-1)
                                else:
                                        print("ERROR: Den anoigei h aristeri parenthesi meta apo onoma kapoias function",line)
                                        exit(-1)

                        else:
                                print("ERROR: Den yparxei onoma function",line)
                                exit(-1)
                else:
                         print("ERROR: H leksi def den yparxei stin arxi tou programmatos",line)
                         exit(-1)

        def declarations():
            global lexres
            
            while(lexres[0] == declare_tk):
                 declaration_line()

        def declaration_line():
                global lexres 
                
                if (lexres[0] == declare_tk):
                        lexres = lex()
                        line = lexres[2]
                        
                        id_list(1) # metavlites

                                
        def id_list(flag):
                global line 
                global lexres
                
                if(lexres[0] == id_tk):
                        name = lexres[1]
                        lexres = lex()
                        line = lexres[2]

                        if (flag == 1):  # to kalese i "declaration_line" ara einai Entity
                                ent = Entity()							#Create an Entity
                                ent.type = 'VAR'						#
                                ent.name = name						#
                                ent.variable.offset = compute_offset()	#
                                new_entity(ent)							#
                        else:  # flag = 0,  to kalese i "def_function" ara einai Argument
                                arg = Argument()		#Creation of a new argument. (Pinakas Symbolwn)
                                arg.name = name		#
                                arg.parMode = 'CV'		#
                                new_argument(arg)		#

                        while(lexres[0] == koma_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                if(lexres[0] == id_tk):
                                        name = lexres[1]
                                        lexres = lex()
                                        line = lexres[2]

                                        if (flag == 1):
                                              ent = Entity()							#Create an Entity
                                              ent.type = 'VAR'						#
                                              ent.name = name						#
                                              ent.variable.offset = compute_offset()	#
                                              new_entity(ent)							#
                                        else:
                                              arg = Argument()		#Creation of a new argument. (Pinakas Symbolwn)
                                              arg.name = name		#
                                              arg.parMode = 'CV'		#
                                              new_argument(arg)		#
                                        
                                else:
                                        print("ERROR: Den yparxei id meta apo koma", line)
                                        exit(-1)               
                
        def statement():
           global line 
           global lexres

           if(lexres[0]==id_tk or lexres[0]==print_tk or lexres[0]==return_tk):
                simple_statement()
           elif(lexres[0]==if_tk or lexres[0]==while_tk):
                structured_statement()
           else:
                print("ERROR: Den yparxei swsto statement", line)
                exit(-1)

        def statements():
           global lexres

           statement()
           while(lexres[0]==id_tk or lexres[0]==print_tk or lexres[0]==return_tk or lexres[0]==if_tk or lexres[0]==while_tk):
                statement()

        def simple_statement():
           global lexres

           if(lexres[0]==id_tk):
                assignment_stat()
           elif(lexres[0]==print_tk):
                print_stat()
           elif(lexres[0]==return_tk):
                return_stat()
        
        def structured_statement():
           global lexres

           if(lexres[0]==if_tk):
                if_stat()
           elif(lexres[0]==while_tk):
                while_stat()

        def assignment_stat():
                global lexres
                global line
                
                if(lexres[0] == id_tk):
                        myid = lexres[1]

                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == anathesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                if(lexres[0] == int_tk):
                                    lexres = lex()
                                    line = lexres[2]
                                    
                                    genQuad('inp',myid,'_','_')
                                    
                                    if(lexres[0] == arist_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]

                                        if(lexres[0] == input_tk):
                                            lexres = lex()
                                            line = lexres[2]

                                            if(lexres[0] == arist_parenthesi_tk):
                                                 lexres = lex()
                                                 line = lexres[2]
                                                
                                                 if(lexres[0] == deksia_parenthesi_tk):
                                                      lexres = lex()
                                                      line = lexres[2]
                                
                                                      if(lexres[0] == deksia_parenthesi_tk):
                                                          lexres = lex()
                                                          line = lexres[2]
                                                          
                                                          
                                                          if(lexres[0] == erwtimatiko_tk):
                                                              lexres = lex()
                                                              line = lexres[2]
                                                          else:
                                                              print("ERROR: Den yparxei ; stin assignment_stat",line)
                                                              exit(-1)
                                                      else:
                                                           print("ERROR: Den yparxei ) stin assignment_stat",line)
                                                           exit(-1)
                                                 else:
                                                      print("ERROR: Den yparxei ) stin assignment_stat",line)
                                                      exit(-1)
                                            else:
                                                      print("ERROR: Den yparxei ( stin assignment_stat",line)
                                                      exit(-1)
                                        else:
                                                print("ERROR: Den yparxei input stin assignment_stat",line)
                                                exit(-1)
                                    else:
                                           print("ERROR: Den yparxei ( stin assignment_stat",line)
                                           exit(-1)
                                
                                else:
                                    Eplace = expression()
                                    genQuad(':=', Eplace, '_', myid)

                                    if(lexres[0] == erwtimatiko_tk):
                                        lexres = lex()
                                        line = lexres[2]
                                    else:
                                        print("ERROR: Den yparxei ; meta apo expression stin assignment_stat",line)
                                        exit(-1)

                        else:
                                print("ERROR: Prepei na yparxei to symvolo = meta id.", line)
                                exit(-1) 
                else:
                        print("ERROR: den uparxei id",line)
                        exit(-1)
        def print_stat():
                global lexres
                global line
                
                if(lexres[0] == print_tk):
                        lexres = lex()
                        line = lexres[2]

                        if(lexres[0] == arist_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                Eplace = expression()
                                genQuad('out', Eplace, '_', '_')
                                
                                if(lexres[0] == deksia_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]
                                        
                                        if(lexres[0] == erwtimatiko_tk):
                                            lexres = lex()
                                            line = lexres[2]
                                        else:
                                            print("ERROR: Den yparxei ; meta apo expression stin print_stat",line)
                                            exit(-1)
                                else:
                                        print("ERROR: Den kleinei h parenthesi stin print_stat",line)
                                        exit(-1)
                        else:
                                print("ERROR: Den anoigei h parenthesi stin print_stat", line)
                                exit(-1)

                else:
                        print("ERROR: Den uparxei print",line)
                        exit(-1)

        def return_stat():
                global lexres
                global line
                
                if(lexres[0] == return_tk):
                        lexres = lex()
                        line = lexres[2]

                        if(lexres[0] == arist_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                Eplace = expression()
                                genQuad('retv', Eplace, '_', '_')
                                
                                if(lexres[0] == deksia_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]
                                        
                                        if(lexres[0] == erwtimatiko_tk):
                                            lexres = lex()
                                            line = lexres[2]
                                        else:
                                            print("ERROR: Den yparxei ; meta apo expression stin return_stat",line)
                                            exit(-1)
                                else:
                                        print("ERROR: Den kleinei h parenthesi stin return_stat",line)
                                        exit(-1)
                        else:
                                print("ERROR: Den anoigei h parenthesi stin return_stat", line)
                                exit(-1)

                else:
                        print("ERROR: Den uparxei return",line)
                        exit(-1)


        def if_stat():
                global lexres
                global line
                
                if(lexres[0] == if_tk):
                        lexres= lex()
                        line = lexres[2]
                        
                        if(lexres[0] == arist_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                C = condition()
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0]== deksia_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]

                                        if(lexres[0] == anwkatw_teleia_tk):
                                             lexres = lex()
                                             line = lexres[2]
                                             
                                             if(lexres[0] == anoigma_block_tk):
                                                    lexres = lex()
                                                    line = lexres[2]
                                                    
                                                    statements()

                                                    ifList = makeList(nextQuad())
                                                    genQuad('jump', '_', '_', '_')
                                                    backPatch(C[1], nextQuad())

                                                    if(lexres[0] == kleisimo_block_tk):
                                                        lexres = lex()
                                                        line = lexres[2]
                                                    else:
                                                        print("ERROR: Den yparxei #} meta ta statements kapoias if",line)
                                                        exit(-1)
                                             else:
                                                    statement()
                                                    
                                                    ifList = makeList(nextQuad())
                                                    genQuad('jump', '_', '_', '_')
                                                    backPatch(C[1], nextQuad())

                                             if(lexres[0] == else_tk):
                                                lexres = lex()
                                                line = lexres[2]
                                             
                                                if(lexres[0] == anwkatw_teleia_tk):
                                                    lexres = lex()
                                                    line = lexres[2]
                                                    
                                                    if(lexres[0] == anoigma_block_tk):
                                                          lexres = lex()
                                                          line = lexres[2]
                                                    
                                                          statements()
                                                          
                                                          backPatch(ifList, nextQuad())

                                                          if(lexres[0] == kleisimo_block_tk):
                                                              lexres = lex()
                                                              line = lexres[2]
                                                          else:
                                                              print("ERROR: Den yparxei #} meta ta statements kapoias if",line)
                                                              exit(-1)
                                                    else:
                                                          statement()

                                                          backPatch(ifList, nextQuad())

                                                else:
                                                    print("ERROR: Den yparxei : meta to else",line)
                                                    exit(-1)
                                              
                                             else:
                                                   backPatch(ifList, nextQuad())

                                        else:
                                              print("ERROR: Den yparxei : meta to condition tou if",line)
                                              exit(-1)

                                else:
                                        print("ERROR: Den kleinei h parenthesi meta to condition tou if", line)
                                        exit(-1)
                        else:
                                print("ERROR: Den exei anoiksei parenthesi prin to condition tou if", line)
                                exit(-1)
                else:
                        print("ERROR: Den uparxei if",line)
                        exit(-1)
                

        def while_stat():
                global lexres
                global line
                
                if(lexres[0] == while_tk):
                        lexres= lex()
                        line = lexres[2]
                        
                        if(lexres[0] == arist_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                Cquad=nextQuad()
                                C = condition()
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0]== deksia_parenthesi_tk):
                                        lexres = lex()
                                        line = lexres[2]

                                        if(lexres[0] == anwkatw_teleia_tk):
                                             lexres = lex()
                                             line = lexres[2]
                                             
                                             if(lexres[0] == anoigma_block_tk):
                                                    lexres = lex()
                                                    line = lexres[2]
                                                    
                                                    statements()

                                                    genQuad('jump', '_', '_', Cquad)
                                                    backPatch(C[1], nextQuad())

                                                    if(lexres[0] == kleisimo_block_tk):
                                                        lexres = lex()
                                                        line = lexres[2]
                                                    else:
                                                        print("ERROR: Den yparxei #} meta ta statements kapoias while",line)
                                                        exit(-1)
                                             else:
                                                    statement()

                                                    genQuad('jump', '_', '_', Cquad)
                                                    backPatch(C[1], nextQuad())


                                        else:
                                              print("ERROR: Den yparxei : meta to condition tou while",line)
                                              exit(-1)

                                else:
                                        print("ERROR: Den kleinei h parenthesi meta to condition tou while", line)
                                        exit(-1)
                        else:
                                print("ERROR: Den exei anoiksei parenthesi prin to condition tou while", line)
                                exit(-1)
                else:
                        print("ERROR: Den uparxei while",line)
                        exit(-1)

        def expression():
                global lexres
                global line
                
                optional_sign()

                T1place = term()

                while(lexres[0]==plus_tk or lexres[0]==minus_tk):
                        plusOrMinus = ADD_OP()
                        T2place = term()

                        w = newTemp()
                        genQuad(plusOrMinus, T1place, T2place, w)
                        T1place = w

                Eplace = T1place
                return Eplace

        def term():
                global lexres
                global line
                
                F1place = factor()
                
                while(lexres[0]==multiply_tk or lexres[0]==divide_tk):
                        mulOrDiv = MUL_OP()
                        F2place = factor()

                        w=newTemp()
                        genQuad(mulOrDiv, F1place, F2place, w)
                        F1place = w

                Tplace =F1place
                return Tplace
                
        def factor():
                global lexres
                global line
                
                if(lexres[0]==num_tk):
                        fact = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]==arist_parenthesi_tk):
                        lexres = lex()
                        line = lexres[2]

                        Eplace = expression()
                        fact = Eplace

                        if(lexres[0]==deksia_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                        else:
                                print("ERROR: Theloume dexia parenthesi ')' meta to expression stin FACTOR ",line)
                                exit(-1)
                elif(lexres[0]==id_tk):
                        fact_temp = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                        fact = idtail(fact_temp)
                        
                else:
                        print("ERROR: Theloume constant h expression h variable stin FACTOR",line)
                        exit(-1)
                
                return fact
        
        def idtail(name):
                global lexres
                global line
                
                if(lexres[0] == arist_parenthesi_tk ):
                        lexres = lex()
                        line = lexres[2]

                        actual_par_list()
                        w=newTemp()
                        genQuad('par', w, 'RET', '_')
                        genQuad('call', name, '_', '_')
                        
                        if(lexres[0]==deksia_parenthesi_tk):
                                lexres = lex()
                                line = lexres[2]
                                return w
                        else:
                                print("ERROR: Theloume ) stin IDTAIL",line)
                                exit(-1)
                else:
                        return name

        def actual_par_list():
                global lexres
                global line 
                
                if (lexres[0]==num_tk or lexres[0]==arist_parenthesi_tk or lexres[0]==id_tk):
                    
                    thisExpression = expression()
                    genQuad('par', thisExpression, 'CV', '_')
                    
                    while(lexres[0] == koma_tk):
                        lexres  = lex()
                        line = lexres[2]
                        
                        thisExpression = expression()
                        genQuad('par', thisExpression, 'CV', '_')


        def optional_sign():
                global lexres
                global line
                
                if(lexres[0] == plus_tk or lexres[0] == minus_tk):
                        
                        ADD_OP()
        
        def ADD_OP():
                global lexres 
                global line
                
                if(lexres[0]==plus_tk):
                        addOp = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        

                elif(lexres[0]==minus_tk):
                        addOp = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                return addOp


        def MUL_OP():
                global lexres 
                global line
                
                if (lexres[0] == multiply_tk):
                        oper = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif (lexres[0] == divide_tk):
                        oper = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                return oper

                
        def condition():
                global lexres
                global line

                Ctrue = []
                Cfalse = []

                BT1 = bool_term()

                Ctrue = BT1[0]
                Cfalse = BT1[1]

                while(lexres[0]==or_tk):
                        lexres=lex()
                        line = lexres[2]
                        
                        backPatch(Cfalse, nextQuad())
                        
                        BT2 = bool_term()

                        Ctrue = merge(Ctrue, BT2[0])
                        Cfalse = BT2[1]

                return Ctrue, Cfalse

                
        def bool_term():
                global lexres
                global line
                
                BTtrue = []
                BTfalse = []

                BF1 = bool_factor()

                BTtrue = BF1[0]
                BTfalse = BF1[1]

                while(lexres[0]==and_tk):
                        lexres=lex()
                        line = lexres[2]
                        
                        backPatch(BTtrue, nextQuad())
                        
                        BF2 = bool_factor()

                        BTfalse = merge(BTfalse, BF2[1])
                        BTtrue = BF2[0]

                return BTtrue, BTfalse

                
        def bool_factor():
                global lexres
                global line

                BFtrue = []
                BFfalse = []

                if(lexres[0]==not_tk):
                        lexres=lex()
                        line = lexres[2]
                        
                        if(lexres[0]==arist_agkili_tk):
                                lexres = lex()
                                line = lexres[2]
                                
                                C = condition()
                                
                                if(lexres[0]==deksia_agkili_tk):
                                        lexres = lex()
                                        line = lexres[2]

                                        BFtrue = C[1]
                                        BFfalse = C[0]

                                else:
                                        print("ERROR: Den yparxei kleisimo agkylis meta tin synthiki stin BOOLFACTOR ",line)
                                        exit(-1)
                        else:
                                print("ERROR: Theloume anoigma agkylis meta to not stin BOOLFACTOR", line)
                                exit(-1)

                elif(lexres[0]==arist_agkili_tk):
                        lexres = lex()
                        line = lexres[2]
                        
                        C = condition()
                        
                        if(lexres[0]==deksia_agkili_tk):
                                lexres = lex()
                                line = lexres[2]

                                BFtrue = C[0]
                                BFfalse = C[1]

                        else:
                                print("ERROR: Den yparxei kleisimo agkylis meta tin synthiki stin BOOLFACTOR", line)
                                exit(-1)
                else:
                        
                        Eplace1 = expression()
                        
                        relop = REL_OP()
                        
                        Eplace2 = expression()
                        
                        BFtrue=makeList(nextQuad())
                        genQuad(relop, Eplace1, Eplace2, '_')
                        BFfalse=makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')

                return BFtrue, BFfalse

        def REL_OP():
                global lexres 
                global line

                if(lexres[0]==equal_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]==lessthan_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]==lessORequal_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]==diaforo_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]== greaterthan_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                elif(lexres[0]==greaterORequal_tk):
                        relop = lexres[1]
                        lexres = lex()
                        line = lexres[2]
                        
                else:
                        print("ERROR: Leipei = h < h <= h <> h >= h > ",line)
                        exit(-1)

                return relop

        def call_main_part():
                global lexres 
                global line

                if(lexres[0] == if_tk):
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == name_tk):
                                lexres = lex()
                                line = lexres[2]

                                if(lexres[0] == equal_tk):
                                        lexres = lex()
                                        line = lexres[2]
                        
                                        if(lexres[0] == quotes_tk):
                                                lexres = lex()
                                                line = lexres[2]

                                                if(lexres[0] == main_tk):
                                                    lexres = lex()
                                                    line = lexres[2]

                                                    if(lexres[0] == quotes_tk):
                                                            lexres = lex()
                                                            line = lexres[2]
                                                
                                                            if(lexres[0] == anwkatw_teleia_tk):
                                                                lexres = lex()
                                                                line = lexres[2]

                                                                genQuad('begin_block','main','_','_')
                                                                main_function_call()
                                                                while(lexres[0] == id_tk):
                                                                     main_function_call()
                                                                genQuad('halt','_','_','_')
                                                                genQuad('end_block','main','_','_')

                                                                print_Symbol_table()
                                                                os.system("pause")

                                                                delete_scope()

                                                            else:
                                                                print("ERROR: Den yparxei : stin call_main_part",line)
                                                                exit(-1)
                                                    else:
                                                        print("ERROR: Den yparxei quote stin call_main_part",line)
                                                        exit(-1)
                                                else:
                                                   print("ERROR: Den yparxei main stin call_main_part",line)
                                                   exit(-1)
                                        else:
                                            print("ERROR: Den yparxei quote stin call_main_part",line)
                                            exit(-1)
                                else:
                                        print("ERROR: Den yparxei == stin call_main_part",line)
                                        exit(-1)

                        else:
                                print("ERROR: Den yparxei __name__ stin call_main_part",line)
                                exit(-1)
                else:
                         print("ERROR: H leksi if den yparxei stin call_main_part",line)
                         exit(-1)
        
        def main_function_call():
                global line 
                global lexres
                
                if(lexres[0] == id_tk):
                    genQuad('call', lexres[1], '_', '_')
                    lexres = lex()
                    line = lexres[2]

                    if(lexres[0] == arist_parenthesi_tk):
                          lexres = lex()
                          line = lexres[2]
                        
                          if(lexres[0] == deksia_parenthesi_tk):
                                    lexres = lex()
                                    line = lexres[2]
                                                
                                    if(lexres[0] == erwtimatiko_tk):
                                          lexres = lex()
                                          line = lexres[2]
                                
                                    else:
                                          print("ERROR: Den yparxei ; stin main_function_call",line)
                                          exit(-1)
                          else:
                               print("ERROR: Den kleinei h deksia parenthesi stin main_function_call",line)
                               exit(-1)
                    else:
                          print("ERROR: Den anoigei h aristeri parenthesi stin main_function_call",line)
                          exit(-1)

                else:
                         print("ERROR: H leksi id den yparxei stin main_function_call",line)
                         exit(-1)
                        
                        
        
        startRule()


def intCode(intF):
	'Write listOfAllQuads at intFile.int'
	for i in range(len(listOfAllQuads)):
		quad = listOfAllQuads[i]
		intF.write(str(quad[0]))
		intF.write(":  ")
		intF.write(str(quad[1]))
		intF.write("  ")
		intF.write(str(quad[2]))
		intF.write("  ")
		intF.write(str(quad[3]))
		intF.write("  ")
		intF.write(str(quad[4]))
		intF.write("\n")

intFile = open('intFile.int', 'w')
syntax_an()
#telos syntaktikou analyti
print("OK")
intCode(intFile)
intFile.close()

