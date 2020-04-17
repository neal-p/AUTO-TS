from numpy import linalg as la
import numpy as np
import sys

# Input Parameters

lowest=sys.argv[1].split('.')[0]
c1=int(sys.argv[2])
a1=int(sys.argv[3])
a2=int(sys.argv[4])
c2=int(sys.argv[5])
conf_search=sys.argv[6]
title=lowest.split('-rot')[0]

# Error exit if no input is given
class Element:
    ## This class is periodic table
    ## This class read atom name in various format
    ## This class return atomic properties

    def __init__(self,name):

        Periodic_Table = {
             "HYDROGEN":"1","H":"1","1":"1",
             "HELIUM":"2","He":"2","2":"2","HE":"2",
             "LITHIUM":"3","Li":"3","3":"3","LI":"3",
             "BERYLLIUM":"4","Be":"4","4":"4","BE":"4",
             "BORON":"5","B":"5","5":"5",
             "CARBON":"6","C":"6","6":"6",
             "NITROGEN":"7","N":"7","7":"7",
             "OXYGEN":"8","O":"8","8":"8",
             "FLUORINE":"9","F":"9","9":"9",
             "NEON":"10","Ne":"10","10":"10","NE":"10",
             "SODIUM":"11","Na":"11","11":"11","NA":"11",
             "MAGNESIUM":"12","Mg":"12","12":"12","MG":"12",
             "ALUMINUM":"13","Al":"13","13":"13","AL":"12",
             "SILICON":"14","Si":"14","14":"14","SI":"14",
             "PHOSPHORUS":"15","P":"15","15":"15",
             "SULFUR":"16","S":"16","16":"16",
             "CHLORINE":"17","Cl":"17","17":"17","CL":"17",
             "ARGON":"18","Ar":"18","18":"18","AG":"18",
             "POTASSIUM":"19","K":"19","19":"19",
             "CALCIUM":"20","Ca":"20","20":"20","CA":"20",
             "SCANDIUM":"21","Sc":"21","21":"21","SC":"21",
             "TITANIUM":"22","Ti":"22","22":"22","TI":"22",
             "VANADIUM":"23","V":"23","23":"23",
             "CHROMIUM":"24","Cr":"24","24":"24","CR":"24",
             "MANGANESE":"25","Mn":"25","25":"25","MN":"25",
             "IRON":"26","Fe":"26","26":"26","FE":"26",
             "COBALT":"27","Co":"27","27":"27","CO":"27",
             "NICKEL":"28","Ni":"28","28":"28","NI":"28",
             "COPPER":"29","Cu":"29","29":"29","CU":"29",
             "ZINC":"30","Zn":"30","30":"30","ZN":"30",
             "GALLIUM":"31","Ga":"31","31":"31","GA":"31",
             "GERMANIUM":"32","Ge":"32","32":"32","GE":"32",
             "ARSENIC":"33","As":"33","33":"33","AS":"33",
             "SELENIUM":"34","Se":"34","34":"34","SE":"34",
             "BROMINE":"35","Br":"35","35":"35","BR":"35",
             "KRYPTON":"36","Kr":"36","36":"36","KR":"36",
             "RUBIDIUM":"37","Rb":"37","37":"37","RB":"37",
             "STRONTIUM":"38","Sr":"38","38":"38","SR":"38",
             "YTTRIUM":"39","Y":"39","39":"39",
             "ZIRCONIUM":"40","Zr":"40","40":"40","ZR":"40",
             "NIOBIUM":"41","Nb":"41","41":"41","NB":"41",
             "MOLYBDENUM":"42","Mo":"42","42":"42","MO":"42",
             "TECHNETIUM":"43","Tc":"43","43":"43","TC":"43",
             "RUTHENIUM":"44","Ru":"44","44":"44","RU":"44",
             "RHODIUM":"45","Rh":"45","45":"45","RH":"45",
             "PALLADIUM":"46","Pd":"46","46":"46","PD":"46",
             "SILVER":"47","Ag":"47","47":"47","AG":"47",
             "CADMIUM":"48","Cd":"48","48":"48","CD":"48",
             "INDIUM":"49","In":"49","49":"49","IN":"49",
             "TIN":"50","Sn":"50","50":"50","SN":"50",
             "ANTIMONY":"51","Sb":"51","51":"51","SB":"51",
             "TELLURIUM":"52","Te":"52","52":"52","TE":"52",
             "IODINE":"53","I":"53","53":"53",
             "XENON":"54","Xe":"54","54":"54","XE":"54",
             "CESIUM":"55","Cs":"55","55":"55","CS":"55",
             "BARIUM":"56","Ba":"56","56":"56","BA":"56",
             "LANTHANUM":"57","La":"57","57":"57","LA":"57",
             "CERIUM":"58","Ce":"58","58":"58","CE":"58", 
             "PRASEODYMIUM":"59","Pr":"59","59":"59","PR":"59",
             "NEODYMIUM":"60","Nd":"60","60":"60","ND":"60", 
             "PROMETHIUM":"61","Pm":"61","61":"61","PM":"61", 
             "SAMARIUM":"62","Sm":"62","62":"62","SM":"62",
             "EUROPIUM":"63","Eu":"63","63":"63","EU":"63", 
             "GADOLINIUM":"64","Gd":"64","64":"64","GD":"64", 
             "TERBIUM":"65","Tb":"65","65":"65","TB":"65",
             "DYSPROSIUM":"66","Dy":"66","66":"66","DY":"66", 
             "HOLMIUM":"67","Ho":"67","67":"67","HO":"67", 
             "ERBIUM":"68","Er":"68","68":"68","ER":"68", 
             "THULIUM":"69","TM":"69","69":"69","TM":"69", 
             "YTTERBIUM":"70","Yb":"70","70":"70","YB":"70", 
             "LUTETIUM":"71","Lu":"71","71":"71","LU":"71",
             "HAFNIUM":"72","Hf":"72","72":"72","HF":"72",
             "TANTALUM":"73","Ta":"73","73":"73","TA":"73",
             "TUNGSTEN":"74","W":"74","74":"74",
             "RHENIUM":"75","Re":"75","75":"75","RE":"75",
             "OSMIUM":"76","Os":"76","76":"76","OS":"76",
             "IRIDIUM":"77","Ir":"77","77":"77","IR":"77",
             "PLATINUM":"78","Pt":"78","78":"78","PT":"78",
             "GOLD":"79","Au":"79","79":"79","AU":"79",
             "MERCURY":"80","Hg":"80","80":"80","HG":"80",
             "THALLIUM":"81","Tl":"81","81":"81","TL":"81",
             "LEAD":"82","Pb":"82","82":"82","PB":"82",
             "BISMUTH":"83","Bi":"83","83":"83","BI":"83",
             "POLONIUM":"84","Po":"84","84":"84","PO":"84",
             "ASTATINE":"85","At":"85","85":"85","AT":"85",
             "RADON":"86","Rn":"86","86":"86","RN":"86"}

        FullName=["HYDROGEN", "HELIUM", "LITHIUM", "BERYLLIUM", "BORON", "CARBON", "NITROGEN", "OXYGEN", "FLUORINE", "NEON", 
              "SODIUM", "MAGNESIUM", "ALUMINUM", "SILICON", "PHOSPHORUS", "SULFUR", "CHLORINE", "ARGON", "POTASSIUM", "CALCIUM", 
              "SCANDIUM", "TITANIUM", "VANADIUM", "CHROMIUM", "MANGANESE", "IRON", "COBALT", "NICKEL", "COPPER", "ZINC", 
              "GALLIUM", "GERMANIUM", "ARSENIC", "SELENIUM", "BROMINE", "KRYPTON", "RUBIDIUM", "STRONTIUM", "YTTRIUM", "ZIRCONIUM", 
              "NIOBIUM", "MOLYBDENUM", "TECHNETIUM", "RUTHENIUM", "RHODIUM", "PALLADIUM", "SILVER", "CADMIUM", "INDIUM", "TIN", 
              "ANTIMONY", "TELLURIUM", "IODINE", "XENON", "CESIUM", "BARIUM", "LANTHANUM", "CERIUM", "PRASEODYMIUM", "NEODYMIUM", 
              "PROMETHIUM", "SAMARIUM", "EUROPIUM", "GADOLINIUM", "TERBIUM", "DYSPROSIUM", "HOLMIUM", "ERBIUM", "THULIUM", "YTTERBIUM", 
              "LUTETIUM", "HAFNIUM", "TANTALUM", "TUNGSTEN", "RHENIUM", "OSMIUM", "IRIDIUM", "PLATINUM", "GOLD", "MERCURY", 
              "THALLIUM", "LEAD", "BISMUTH", "POLONIUM", "ASTATINE", "RADON"]

        Symbol=[ "H","He","Li","Be","B","C","N","O","F","Ne",
                "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
                "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
                "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
                "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
                "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
                "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","TM","Yb",
                "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
                "Tl","Pb","Bi","Po","At","Rn"]

        Mass=[1.008,4.003,6.941,9.012,10.811,12.011,14.007,15.999,18.998,20.180,
              22.990,24.305,26.982,28.086,30.974,32.065,35.453,39.948,39.098,40.078,
              44.956,47.867,50.942,51.996,54.938,55.845,58.933,58.693,63.546,65.390,
              69.723,72.640,74.922,78.960,79.904,83.800,85.468,87.620,88.906,91.224,
              92.906,95.940,98.000,101.070,102.906,106.420,107.868,112.411,114.818,118.710,
              121.760,127.600,126.905,131.293,132.906,137.327,138.906,140.116,140.908,144.240,
              145.000,150.360,151.964,157.250,158.925,162.500,164.930,167.259,168.934,173.040,
              174.967,178.490,180.948,183.840,186.207,190.230,192.217,195.078,196.967,200.590,
              204.383,207.200,208.980,209.000,210.000,222.000]

        # Van der Waals Radius, missing data replaced by 2.00
        Radii=[1.20,1.40,1.82,1.53,1.92,1.70,1.55,1.52,1.47,1.54,
               2.27,1.73,1.84,2.10,1.80,1.80,1.75,1.88,2.75,2.31,
               2.11,2.00,2.00,2.00,2.00,2.00,2.00,1.63,1.40,1.39,
               1.87,2.11,1.85,1.90,1.85,2.02,3.03,2.49,2.00,2.00,
               2.00,2.00,2.00,2.00,2.00,1.63,1.72,1.58,1.93,2.17,
               2.00,2.06,1.98,2.16,3.43,2.68,2.00,2.00,2.00,2.00,
               2.00,2.00,2.00,2.00,2.00,2.00,2.00,2.00,2.00,2.00,
               2.00,2.00,2.00,2.00,2.00,2.00,2.00,1.75,1.66,1.55,
               1.96,2.02,2.07,1.97,2.02,2.20]

        # Covalent Radii, missing data replaced by 1.50
        CovRad=[ 0.38,  0.32,  1.34,  0.9 ,  0.82,  0.77,  0.75,  0.73,  0.71,
                 0.69,  1.54,  1.3 ,  1.18,  1.11,  1.06,  1.02,  0.99,  0.97,
                 1.96,  1.74,  1.44,  1.36,  1.25,  1.27,  1.39,  1.25,  1.26,
                 1.21,  1.38,  1.31,  1.26,  1.22,  1.19,  1.16,  1.14,  1.1 ,
                 2.11,  1.92,  1.62,  1.48,  1.37,  1.45,  1.56,  1.26,  1.35,
                 1.31,  1.53,  1.48,  1.44,  1.41,  1.38,  1.35,  1.33,  1.3,
                 2.25,  1.98,  1.69,  1.5 ,  0.11,  1.5 ,  1.5 ,  1.5 ,  1.5 ,
                 1.5 ,  1.5 ,  1.5 ,  1.5 ,  1.5 ,  1.5 ,  1.5 ,  1.5 ,  1.6 ,
                 1.5 ,  1.38,  1.46,  1.59,  1.28,  1.37,  1.28,  1.44,  1.49,
                 1.48,  1.47,  1.46,  1.5 ,  1.5 ,  1.45]

        self.__name = int(Periodic_Table[name])
        self.__FullName = FullName[self.__name-1]
        self.__Symbol = Symbol[self.__name-1]
        self.__Mass = Mass[self.__name-1]
        self.__Radii = Radii[self.__name-1]
        self.__CovR  = CovRad[self.__name-1]

    def getFullName(self):
        return self.__FullName
    def getSymbol(self):
        return self.__Symbol
    def getUpperSymbol(self):
        return self.__Symbol.upper()
    def getMass(self):
        return self.__Mass
    def getNuc(self):
        return self.__name
    def getNelectron(self):
        return self.__name
    def getRadii(self):
        return self.__Radii
    def getCovR(self):
        return self.__CovR


def ReadG16(title):
    ## This function read coordinates from Gaussian .log
    with open('%s.log' % (title),'r') as logfile:
        log=logfile.read().splitlines()

    natom=0
    coord=[]
    xyz=[]
    atoms=[]
    for n,line in enumerate(log):
        if 'NAtoms' in line:
            natom=int(line.split()[1])
        if 'Input orientation' in line:
            coord=log[n+5:n+5+natom]
    for line in coord:
        c,e,t,x,y,z=line.split()
        n=Element(e).getNuc()
        x,y,z=float(x),float(y),float(z)
        atoms.append(n)
        xyz.append([x,y,z])
    xyz=np.array(xyz)
    return atoms,xyz

def Ang(xyz,a,b,c):
    #a<-b->c
    a=xyz[a]
    b=xyz[b]
    c=xyz[c]
    v1=a-b
    v2=c-b
    v1=v1/la.norm(v1)
    v2=v2/la.norm(v2)
    cosa=np.dot(v1,v2)
    alpha=np.arccos(cosa)*57.2958
    return alpha

def Maestro(c1,a1,a2,c2,lowest,title):
    atoms,xyz=ReadG16(lowest)
    angle1=Ang(xyz,c1,a1,a2)
    angle2=Ang(xyz,c2,a2,a1)
    a1=a1+1
    a2=a2+1
    c2=c2+1
    c1=c1+1
    maestroinput="""{0}.mae
{1}-out.mae
 MMOD       0      1      0      0     0.0000     0.0000     0.0000     0.0000
 DEBG    1003      0      0      0     0.0000     0.0000     0.0000     0.0000
 FFLD      16      1      0      0     1.0000     0.0000     0.0000     0.0000
 SOLV       3      1      0      0     0.0000     0.0000     0.0000     0.0000
 EXNB       0      0      0      0    12.0000    20.0000     4.0000     0.0000
 BDCO       0      0      0      0    89.4427 99999.0000     0.0000     0.0000
 READ       0      0      0      0     0.0000     0.0000     0.0000     0.0000
 FXBA      {2}     {3}     {4}      0 10000000.0000   {5:.3f}     0.0000     0.0000
 FXBA      {6}     {7}     {8}      0 10000000.0000   {9:.3f}     0.0000     0.0000
 CRMS       0      0      0      0     0.0000     3.0000     0.0000     2.0000
 LMCS   10000      0      0      0     0.0000     0.0000     3.0000    12.0000
 MCSS       2      0      0      0   500.0000     0.0000     0.0000     0.0000
 MCOP       1      0      0      0     0.0000    10.0000     0.0000     0.0000
 DEMX       0   1000      0      0   500.0000  1000.0000     0.0000     0.0000
 MSYM       0      0      0      0     0.0000     0.0000     0.0000     0.0000
 AUOP       0      0      0      0   500.0000     0.0000     0.0000     0.0000
 AUTO       0      2      1      1     0.0000    -1.0000     0.0000     2.0000
 CONV       2      0      0      0     0.0500     0.0000     0.0000     0.0000
 MINI       3      0   3000      0     0.0000     0.0000     0.0000     0.0000
""".format(title, title, c1, a1, a2, angle1, c2, a2, a1, angle2)
    return maestroinput


with open('{0}/{1}.com'.format(conf_search,title), 'w') as maestro:
    maestro.write(Maestro(c1,a1,a2,c2,lowest,title))
