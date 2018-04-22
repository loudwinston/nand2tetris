#!/usr/bin/python
import re


def stripcomments(str):
	return re.sub(r'\/\/.*\n?', '\n', str)


def contains(str, char):
	return bin(str.find(char) != -1)[2:]


def convertRegisterToBinary(str):
	if not str:
		return '000'

	binary = []
	binary.append(contains(str, 'A'))
	binary.append(contains(str, 'D'))
	binary.append(contains(str, 'M'))
	return ''.join(binary)

def convertOperator(str):
	if (str == '+'):
		return '1'
	else:
		return '0';


def convertJump(str):
	if not str:
		return '000'
	binDict = {
		'JGT': '001',
		'JEQ': '010',
		'JGE': '011',
		'JLT': '100',
		'JNE': '101',
		'JLE': '110',
		'JMP': '111'
	}

	return binDict[str]

operand_b = '([ADM]+)'
assignee = '([ADM])'
jump_expression = '\;([\w]+)'


# '($assignee=)?$operand_a($operator$operand_b)?($jump_expression)?'




# ($operator$operand_b)?($jump_expression)?'


# str = (
# 	'($assignee=)?$operand_a($operator$operand_b)?($jump_expression)?'
# 	.replace('$operand_a', operand_a)
# 	.replace('$operator', operator)
# 	.replace('$operand_b', operand_b)
# 	.replace('$assignee', assignee)
# 	.replace('$jump_expression', jump_expression)
# )





#print str

c_expression = re.compile(
	r'(((?P<assignee>[ADM])=)?(?P<operand_a>[ADM])((?P<operator>[\+\-])(?P<operand_b>[ADM]))|0)?(;(?P<jump>[\w]+))?'
)	
c_expression_match = c_expression.match('M=D+A;JLT');

if c_expression_match:

	assignee =  c_expression_match.group('assignee')
	operand_a =  c_expression_match.group('operand_a')
	operator =  c_expression_match.group('operator')
	operand_b =  c_expression_match.group('operand_b')
	jump =  c_expression_match.group('jump')



	binString = convertRegisterToBinary(assignee) + convertRegisterToBinary(operand_a) + convertOperator(operator) + convertRegisterToBinary(operand_b) + convertJump(jump)


	print c_expression_match.group('assignee')
	print c_expression_match.group('operand_a')
	print c_expression_match.group('operator')
	print c_expression_match.group('operand_b')
	print c_expression_match.group('jump')

	print binString
else:
	print 'Nope!'



# # c_expression = re.match( r'(?P<assignment>(?P<assignee>[ADM])=(?P<operand_a>[ADM])([\+\-](?P<operand_b>[ADM]))*)*(\;(?P<jump_condition>[\w]+))*', line, re.M|re.I)

# # filepath = 'add/Add.asm'  
# filepath = 'test.asm'  
# with open(filepath) as fp:  
# 	for line in fp:
#    		line = stripcomments(line).strip();
#    		if line:
# 			a_expression = re.match( r'@([\w])+', line, re.M|re.I)
# 			c_expression_match = c_expression.match(line, re.M|re.I);
# 			if a_expression:
# 				print a_expression.group()
# 				# print str(bin(int(a_expression.group(1).strip(' "'))))[2:].zfill(15)
# 			elif c_expression_match:
# 				print 'saw c_expression' + c_expression_match.group()
# 			else:
# 				print 'Unknown line: ' + line