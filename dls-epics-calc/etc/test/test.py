#!/dls_sw/tools/bin/python2.4

# Test suite to use with pyUnit

from platform import node
from math import *
from string import *
from pkg_resources import require
require('dls.autotestframework')
from dls.autotestframework import *

################################################
# Test suite for the FW102 filter wheel
    
class CalcTestSuite(TestSuite):

    def createTests(self):        
        Target("simulation", self,
               iocDirectory="iocs/test1",
               iocBootCmd="bin/linux-x86/sttest1.sh",
               runIocInScreenUnderHudson=True,
               epicsDbFiles="db/test1.db" )

        # The tests
        CaseEvaluateExpressions(self)
     

sCalcRecord = "xxx:userStringCalc2"
calc = sCalcRecord + ".CALC"
result = sCalcRecord + ".VAL"
sresult = sCalcRecord + ".SVAL"

small = 1.e-9

A=1.
B=2.
C=3.
D=4.
E=5.
F=6.
G=7.
H=8.
I=9.
J=10.
K=11.
L=12.
AA = "string 1"
BB = "string 2"
CC = "string 3"
DD = "string 4"
EE = "string 5"
FF = "string 6"
GG = "string 7"
HH = "string 8"
II = "string 9"
JJ = "string 10"
KK = "string 11"
LL = "string 12"

exp = [
	("tan(A)", None),
	("sin(B)", None),
	("max(A,B,C)", None),
	("min(D,E,F)", None),
	("A<<2", "int(A)<<2"),
	("L>>1", "int(L)>>1"),
	("A?B:C", "(B,C)[A==0]"),
	("A&&B", "(A and B) != 0"),
	("A||B", "(A or B) != 0"),
#	("AA[0,'.']", "AA[0:find(AA,'.')]"),
	("A>B", None),
	("A>B?BB:AA[A,A]", "(BB,AA[nint(A):nint(A+1)])[(A>B)==0]"),
	("A>=4", None),
	("A=0?1:0", "(0,1)[A==0]"),
	("A+B", None),
	("(B=0)?(A+16384):A+B", "(A+B,A+16384)[B==0]"),
	("1.e7/A", None),
	("A>9?1:0", "(0,1)[A>9]"),
	("A%10+1", None),
	("!A", "not A"),
	("C+((A-E)/(D-E))*(B-C)", None),
	("A#B", "A!=B"),
	("E+nint(D*((A-C)/(B-C)))", None),
	("(A+1)*1000", None),
	("printf('!PFCU%02d ', a)+aa[0,1]", "('!PFCU%02d ' %A)+AA[0:1+1]"),
	("$P('!PFCU%02d E ', a) + $P('%d',b*100)", "('!PFCU%02d E ' % A) + ('%d'%(B*100))"),
	("B?0:!A", "(0,not A)[B==0]"),
	("1", None),
	("A?0:B", "(0,B)[A==0]"),
	("A&&B&&!I", "(((A and B) != 0) and (not I)) != 0"),
	("(A&B&C&D)=1", "(nint(A)&nint(B)&nint(C)&nint(D))==1"),
	("(A&B&C&D&E&F&G&H)=1", "(nint(A)&nint(B)&nint(C)&nint(D)&nint(E)&nint(F)&nint(G)&nint(H))==1"),
	("(A>15)&&B", "((A>15) and B) != 0"),
	("(ABS(A)>1)&&B", "((abs(A)>1) and B) != 0"),
	("(A)=1", "(A)==1"),
	("A*4095", None),
	("(A||B||C||D||E||F)?1:0", "(1,0)[(A or B or C or D or E or F)==0]"),
	("(A<B)?C:D", "(C,D)[(A<B)==0]"),
	("A/(10**(B-2))", None),
	("(F<0.01)?0:(((A+C-B-D)/F)*E)", "(0,(((A+C-B-D)/F)*E))[(F<0.01)==0]"),
	("((A+B)<0.01)?0:(((A-B)/(A+B))*E)", "(0,(((A-B)/(A+B))*E))[((A+B)<0.01)==0]"),
	("((A+B)<0.01)?0:(((A-B)/(A+B))*E)", "(0,(((A-B)/(A+B))*E))[((A+B)<0.01)==0]"),
	("(A - ((B*C)/D))", None),
	("A-B*C/D", None),
	("A/(10**(B-2))", None),
	("min(max(C,A/B),D)", None),
	("(A=B)?C:D", "(C,D)[(A==B)==0]"),
	("A?A+(B|C|D|E):F", "(A+(int(round(B))|int(round(C))|int(round(D))|int(round(E))),F)[A==0]"),
	("D?4:C?3:B?2:A?1:0", "(4,((3,(2,(1,0)[A==0])[B==0])[C==0]))[D==0]"),
	("a>0?1:0", "(1,0)[(A>0)==0]"),
#	("(AA['.',-1]=='EXSC') && A", None),
	("AA + BB", None),
	("A?'A':'!A'", "('A','!A')[A==0]"),
	("'$(P)$(SM)CalcMove.CALC PP MS'", None),
	("A=1", "A==1"),
	("A&(I||!J)&(K||!L)", "nint(A)&nint(I or not J)&nint(K or not L)"),
	("(A||!B)&(C||!D)&(E||!F)&(G||!H)", "nint(A or not B)&nint(C or  not D)&nint(E or not F)&nint(G or not H)"),
	("(A-1.0)", None),
	("A&&C?A-1:B", "(A-1,B)[(A and C)==0]"),
	("C+(A/D)*(B-C)", None),
	("nint(4095*((A-C)/(B-C)))", None),
#	("SSCANF(AA,'%*14c%f')", "?"),
	(".005*A/8", None),
	("A=0||a=2", "A==0 or A==2"),
	("A?2:1", "(2,1)[A==0]"),
	("AA+(BB)+CC", None),
	("A*1.0", None),
	("$P('RSET %d;RSET?',A)", "'RSET %d;RSET?' % A"),
#	("INT(AA)", atoi(AA)),
#	("DBL(AA)", "float(AA)"),
	("$P('SETP %5.2f;SETP?',A)", "'SETP %5.2f;SETP?' % A"),
	("$P('RAMP %d;RAMP?',A)", "'RAMP %d;RAMP?' % A"),
	("$P('RAMPR %5.2f;RAMPR?',A)", "'RAMPR %5.2f;RAMPR?' % A"),
#	("DBL(AA[14,17])", "float(AA[14,17+1])"),
	("DD+AA+EE+BB", None),
	("log(A)", None),
	("-(-2)**2", None),
	("--2**2", None),
	("-(-2)^2", "-(-2)**2"),
	("A--B",None),
	("A--B*C",None),
	("A+B*C",None),
	("D*((A-B)/C)", None),
	("A OR B", "int(round(A))|int(round(B))"),
	("B AND C", "int(round(B))&int(round(C))"),
#	("(2**24+1000) & ((2**23)-1)", None ),
#	("123456789 AND ((2**24)-1)", "123456789 & ((2**24)-1)" ),
	("123456789 AND 16777215", "123456789 & 16777215" ),
#	("2**24", None ),
]

def nint(x):
	return int(floor(x+.5))


################################################
# Intermediate test case class that provides some utility functions
# for this suite

class CalcCase(TestCase):
    def Hello(self):
        pass

    def InitialiseInputs(self):
        A2L = "ABCDEFGHIJKL"

        for i in range(12):
            caput(sCalcRecord + "." + A2L[i], eval(A2L[i]))
            caput(sCalcRecord + "." + A2L[i] + A2L[i], eval(A2L[i]+A2L[i]) )
        
################################################
# Test cases
    
# The current status of the power in CS04R
class CaseEvaluateExpressions(CalcCase):
    '''Evaluates a number of expressions'''

    def runTest(self):
        '''A set of test calculations.'''
        self.InitialiseInputs();

	for e in exp:
            self.putPv(calc,e[0])

            if (e[1]):
                r = eval(e[1])
                self.diagnostic( e[0] + "-->" + e[1], 1 )
            else:
                r = eval(e[0])
                self.diagnostic( e[0], 1 )
                
            if ((type(r) == type(1.0)) or (type(r) == type(1))):
                self.verifyPvFloat( result, r, small )
            elif (type(r) == type(True)):
                rtry = self.getPv(result)
                self.verify((abs(rtry) < small), (r == False))
            else:
                self.verifyPv( sresult, str(r) )
        
################################################
# Main entry point

if __name__ == "__main__":
    # Create and run the test sequence
    CalcTestSuite()

    
