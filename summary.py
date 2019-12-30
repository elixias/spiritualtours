#split the packages
data = pd.read_csv("data_tsv_raw.txt","r",delimiter=",",names=['Title','Location','Country','Participants','Duration','Lowest','Rooms'])
df=data
df2=df['Rooms'].str.split(pat="\n",expand=True)
df=pd.concat([df,df2],axis=1)
df=df.drop(["Rooms"],axis=1)
df=pd.melt(df, id_vars=['Title','Location','Country','Participants','Duration','Lowest'], value_name='Rooms')
df=df.drop(["variable"],axis=1)
df=df[df['Rooms'].values != None]
df=pd.concat([df,df['Rooms'].str.split(",",expand=True)],axis=1)
df.columns = ['Title','Location','Country','Participants','Duration','Lowest','Rooms','Persons','RmType','RmLoc','RmPrice']
#the columns variables are not impt

import pandas as pd
import numpy as np
import re

<<<<<<< HEAD
data = pd.read_csv("data_tsv.txt","r",delimiter="\t",names=['Title','Location','Country','Participants','Duration','Lowest','Rooms'])
#,usecols=["Country","Participants","Duration","Lowest"]
#df = data[data['Country']!='ERR']
df = data.drop_duplicates(keep='first')
=======
data = pd.read_csv("data.txt","r",delimiter=",",names=['Title','Location','Country','Participants','Duration','Lowest','Rooms'])
#,usecols=["Country","Participants","Duration","Lowest"]
df = data[data['Country']!='ERR']

data.info()

df['Country'] = df['Country'].astype(str)
df['Country'] = df['Country'].apply(lambda x: x.replace('.',''))
>>>>>>> a3c94ee0d7be9da2f3c3d3f82172cdd8e4d3694e

"""correcting countries"""
df['Country'][df['Country']=="Maroc"]="Morocco"
df['Country'][df['Country']=="Ghana"]="Africa"
df['Country'][df['Country']=="Pais"]="Costa Rica"
df['Country'][df['Country']=="house"]="Portugal"
df['Country'][df['Country']=="SaintJustdAvray"]="France"
df['Country'][df['Country']=="Malaga"]="Spain"
df['Country'][df['Country']=="Manali"]="India"
df['Country'][df['Country']=="Frankreich"]="France"
df['Country'][df['Country']=="Belize"]="USA"
df['Country'][df['Country']=="Allgu"]="Germany"
df['Country'][df['Country']=="Rico"]="Puerto Rico"
df['Country'][df['Country']=="Baleares"]="Spain"
df['Country'][df['Country']=="Medicine"]="Nepal"
df['Country'][df['Country']=="Fuerteventura"]="Spain"
df['Country'][df['Country']=="Soto"]="Curacao"
df['Country'][df['Country']=="Center"]="Nepal"
df['Country'][df['Country']=="Sausal"]="Austria"
df['Country'][df['Country']=="Spanien"]="Spain"
df['Country'][df['Country']=="Namibia"]="Africa"
df['Country'][df['Country']=="Bolivia"]="USA"
df['Country'][df['Country']=="Kenya"]="Africa"
df['Country'][df['Country']=="Boracay"]="Philippines"
df['Country'][df['Country']=="Stok"]="Nubra Valley"
df['Country'][df['Country']=="Suratthani"]="Thailand"
df['Country'][df['Country']=="Tejakula"]="Bali"
df['Country'][df['Country']=="Tanzania"]="Africa"
df['Country'][df['Country']=="indonesia"]="Indonesia"
df['Country'][df['Country']=="Italia"]="Italy"
df['Country'][df['Country']=="Republic"]="Dominican Republic"
df['Country'][df['Country']=="Marokko"]="Morocco"
df['Country'][df['Country']=="Deutschland"]="Germany"
df['Country'][df['Country']=="Salvador"]="Brazil"
df['Country'][df['Country']=="Griechenland"]="Greece"
df['Country'][df['Country']=="Cullera"]="Spain"
df['Country'][df['Country']=="Uttarakhand"]="India"
df['Country'][df['Country']=="Ecocentro"]="Spain"
df['Country'][df['Country']=="Bay"]="Sri Lanka"
df['Country'][df['Country']=="Ibiza"]="Spain"
df['Country'][df['Country']=="Sanur"]="Bali"
df['Country'][df['Country']=="Espaa"]="Spain"
df['Country'][df['Country']=="Lanka"]="Sri Lanka"
df['Country'][df['Country']=="Argalasti"]="Greece"
df['Country'][df['Country']=="Goa"]="India"
df['Country'][df['Country']=="Kingdom"]="UK"
df['Country'][df['Country']=="Rishikesh"]="India"
df['Country'][df['Country']=="Leicestershire"]="UK"
df['Country'][df['Country']=="Samaria"]="Israel"
df['Country'][df['Country']=="Rica"]="Costa Rica"
df['Country'][df['Country']=="Cundinamarca"]="Colombia"
df['Country'][df['Country']=="Fran"]="France"
df['Country'][df['Country']=="York"]="New York"
df['Country'][df['Country']=="Zanzibar"]="Africa"
df['Country'][df['Country']=="Zealand"]="New Zealand"
df['Country'][df['Country']=="States"]="USA"
"""replacing empty participants"""
df['Participants'] = df['Participants'].fillna(0)
df['Participants'] = df['Participants'].astype(int)

"""Deriving a new feature CPD - Cost Per Day"""
df['CPD'] = df['Lowest'] / df['Duration']

"""Removing those with CPD > 1000 / outliers"""
dfPremium = df[df['CPD'] >= 1000]
"""
                                                  Title   ...         CPD
1306  4 Days Private Yoga Retreat for 8 People on Fl...   ...     2952.82
2039  5 Days Family Bonding with Yoga and Meditation...   ...     1200.00

These 2 records removed as their daily cost is above $1000 per day.
"""

df = df[df['CPD']< 1000]

#df['Duration'] = df['Duration'].fillna(1)
#df['Duration'] = df['Duration'].astype(int)

#df['Lowest'] = df['Lowest'].fillna(0)
#df['Lowest'] = df['Lowest'].astype(float)

"""End of Data Processing"""
df.info()
"""
Data columns (total 8 columns):
Title           1793 non-null object
Location        1793 non-null object
Country         1793 non-null object
Participants    1793 non-null int32
Duration        1793 non-null int64
Lowest          1793 non-null float64
Rooms           1793 non-null object
CPD             1793 non-null float64
dtypes: float64(2), int32(1), int64(1), object(4)

Total of 1793 Records
"""

import matplotlib.pyplot as plt
import seaborn as sns
import math

"""Data Insights"""
df['Country'].unique() #Countries that offer spiritual retreats
"""
['Indonesia', 'Thailand', 'India', 'Sri Lanka', 'Greece', 'USA',
       'Belgium', 'Cambodia', 'Mexico', 'Norway', 'China', 'Croatia',
       'Spain', 'Brazil', 'France', 'Austria', 'UK', 'Nepal', 'Egypt',
       'Germany', 'Italy', 'Peru', 'Morocco', 'Portugal', 'Israel',
       'Colombia', 'Netherlands', 'Costa Rica', 'Malta', 'Mauritius',
       'Australia', 'Ireland', 'New York', 'Africa', 'New Zealand',
       'Mull', 'Turkey', 'Jamaica', 'Guatemala', 'Philippines', 'Bali',
       'Vietnam', 'Dominican Republic', 'Nicaragua', 'Canada', 'Ecuador',
       'Bulgaria', 'Georgia', 'Samoa', 'Taiwan', 'Herzegovina',
       'Nubra Valley', 'Montenegro', 'Curacao', 'Sweden', 'Russia',
       'Japan', 'Jordan', 'Chile', 'Hawaii', 'Serbia', 'Madagascar',
       'Maldives', 'Puerto Rico', 'Argentina', 'Iceland', 'Bhutan',
       'Romania', 'Malaysia', 'Finland', 'Myanmar', 'Switzerland',
       'Emirates']
"""

#top 20 countries with highest listings
df['Country'].value_counts().head(20) 
"""
India         403
Indonesia     190
Thailand      173
Spain         161
USA           110
UK             69
Nepal          63
Portugal       54
Greece         44
Sri Lanka      43
Italy          40
Cambodia       39
Costa Rica     36
France         35
Mexico         29
Ireland        24
Morocco        21
Australia      20
Germany        19
Africa         14
"""

top20ListedCountries = df.Country.value_counts().head(20).index.values
df20 = df[df.Country.isin(top20ListedCountries)]

#Visualization
numRetreats = df20['Country'].value_counts()
sns.barplot(x=numRetreats,y=numRetreats.index)
plt.title("Retreat Locations with Highest # of Listings")
plt.ylabel("Location (Country)")
plt.xlabel("Number of Listings")
plt.show()

#Min, Average, Max Duration of Stay and Cheapest Pricing Worldwide
df[["Duration","Lowest","CPD"]].describe()
"""
          Duration        Lowest          CPD
count  1793.000000   1793.000000  1793.000000 <- Number of Records
mean      7.128834   1056.883402   162.570953 <- Mean Duration, Lowest Offered Package, Cost Per Day
std       5.982640   1030.629658   119.138936
min       1.000000     36.000000     7.386667 <- Lowest
25%       4.000000    448.000000    79.523333
50%       6.000000    770.060000   128.805000 <- Median Duration, Lowest Offered Package, Cost Per Day
75%       7.000000   1345.000000   210.000000
max      90.000000  12809.450000   925.000000 <- Highest
"""

#What are the maximum participants for the retreats?
df[df['Participants']>0]['Participants'].describe() #only want those with non-empty participants
"""
count    1126.000000 <- not all retreats specified max participants
mean       14.022202 <- mean participants
std         8.107415
min         1.000000
25%        10.000000
50%        12.000000 <- median participants
75%        18.000000
max       100.000000

Consideration of the actual capacity our land can accommodate takes precedence.
"""

#Which listings are the cheapest/most expensive/average?
df.sort_values('CPD').head(5)[["Title","Country","CPD"]]
"""
                                                  Title    Country        CPD
1123                 6 Days Yoga Holidays in Goa India       India   7.386667
2019        2 Days Nomad Yoga Holiday in Bali Indonesia  Indonesia  18.000000
1524  1 Week Tantra Meditation with Hatha Yoga in an...      India  21.050000
102   3 Days Meditation and Yoga Holidays in Goa India       India  22.160000
209   7 Days Revitalizing Rejuvenating Meditation Ay...      India  22.160000

Rooms Offered:
                                                  Rooms
1123  1 Persons,Shared twin room,Ashram,44.32\n1 Per...
2019  1 Persons,Shared quadruple room,Retreat center...
1524  1 Persons,Shared twin room,Ashram - shared bat...
102   1 Persons,Shared twin room,Ashram,66.48\n1 Per...
209   1 Persons,Private double room,Hotel,132.96\n1 ...
"""
df.sort_values('CPD').tail(5)[["Title","Country","CPD"]]
"""
                                                  Title    Country         CPD
1355  8 Days Luxurious Rejuvenation Meditation and Y...  Indonesia  816.758750
2042  4 Days Private Luxury  Exclusive Spiritual Cou...      Italy  831.000000
886   15 Days Luxurious Rejuvenation Meditation and ...  Indonesia  853.963333
1593  11 Days Luxurious Rejuvenation Meditation and ...  Indonesia  858.053636
32    4 Days Private Solo Healing Experience Meditat...        USA  925.000000

Rooms Offered:
                                                  Rooms
1355  1 Persons,Private villa,,6534.07\n2 Persons,Pr...
2042  1 Persons,Shared double room,Hotel - Per perso...
886   1 Persons,Private villa,,12809.45\n2 Persons,P...
1593  1 Persons,Private villa,,9438.59\n2 Persons,Pr...
32    1 Persons,Private single room,Retreat center -...
"""
df.sort_values('CPD').iloc[890:900][["Title","Country","CPD"]]
"""
                                                  Title    Country         CPD
1150  8 Days Amazing Meditation and Yoga Retreat in ...      India  128.460000
998   6 Days Embodied Presence Meditation and Yoga R...      Spain  128.460000
2112  8 Days Meditation and Wellness Yoga Retreat in...        USA  128.571429
338   8 Days Yoga  Meditation Retreat in Bali Indonesia  Indonesia  128.571429
239   8 Days Revitalizing Meditation and Yoga Retrea...        USA  128.571429
541   8 Days WellBeing and Yoga Retreat Algarve Port...   Portugal  128.614286
834   4 Tage Wandern Yoga und Entspannen Abschalten ...    Germany  128.805000
2021       5 Day Girlfriend Yoga Retreat in Florida USA        USA  129.000000
2090  7 Days Personal Retreat For Health Leisure and...        USA  129.000000
194   3 Days Weekend Nature and Vinyasa Yoga Retreat...      Spain  129.266667

                                                  Rooms
1150         1 Persons,Private double room,Hotel,770.76
998   1 Persons,Shared twin room,Retreat center - Fi...
2112  1 Persons,Shared double room,Retreat center - ...
338                   1 Persons,Private cottage,,900.00
239   1 Persons,Shared double room,Retreat center - ...
541   1 Persons,Shared twin room,Hotel - Standard sh...
834   1 Persons,Private single room,Hotel,515.22\n1 ...
2021  1 Persons,Private single room,Shared house,516...
2090  1 Persons,Shared twin room,Retreat center - St...
194   1 Persons,Shared double room,Hotel - Ensuite,3...
"""
df.sort_values('Lowest') #does not account for duration of stay

#Mean stats of top 20 Listed Countries by Country
df20[['Duration','Lowest','CPD','Country']].groupby('Country').mean()
df20[df20['Participants']>0][['Participants','Country']].groupby('Country').mean()
"""
             Duration       Lowest         CPD
Country
Africa       8.642857  2015.366429  221.363129
Australia    4.100000   628.040000  152.991843
Cambodia    11.615385   818.128205   98.330236
Costa Rica   8.305556  2094.365278  267.587362
France       5.914286   851.509714  149.878485
Germany      5.000000   616.921579  128.595145
Greece       7.272727  1050.682045  150.418730
India        9.317618   845.113672  103.778430
Indonesia    6.384211  1387.751579  205.562462
Ireland      3.791667   678.674583  190.726488
Italy        5.950000  1269.561500  230.474999
Mexico       5.172414  1148.762069  229.881515
Morocco      5.714286  1314.829524  231.613497
Nepal        7.126984   770.391587   93.049670
Portugal     5.407407   892.766481  169.879774
Spain        5.844720   994.960870  172.080623
Sri Lanka    7.883721  1052.385349  134.524510
Thailand     8.924855  1164.178150  143.730695
UK           3.478261   543.749275  155.626527
USA          5.300000  1416.800000  255.934594

            Participants
Country
Africa          9.666667
Australia      13.000000
Cambodia       16.333333
Costa Rica     14.470588
France         12.000000
Germany        16.117647
Greece         14.484848
India          13.730769
Indonesia      13.035398
Ireland        10.312500
Italy          13.600000
Mexico         11.866667
Morocco        15.000000
Nepal          13.789474
Portugal       11.032258
Spain          10.467213
Sri Lanka       9.526316
Thailand       22.039683
UK             13.486486
USA            13.325581
"""

#Median stats of top 20 Listed Countries by Country
df20[['Duration','Lowest','CPD','Country']].groupby('Country').median()
df20[df20['Participants']>0][['Participants','Country']].groupby('Country').median()
"""
            Duration    Lowest         CPD
Country
Africa           6.5  1667.835  204.642308
Australia        3.5   392.525   86.198750
Cambodia         6.0   450.000   60.000000
Costa Rica       7.0  1858.000  241.607143
France           5.0   730.170  134.806667
Germany          4.0   572.830  128.805000
Greece           7.0   776.420  121.880000
India            7.0   650.000   77.272727
Indonesia        5.0   858.060  178.087500
Ireland          3.0   434.890  120.033333
Italy            6.0  1119.040  188.221429
Mexico           5.0   999.000  231.250000
Morocco          6.0  1000.000  219.753333
Nepal            6.0   443.200   78.571429
Portugal         6.0   805.515  144.672857
Spain            6.0   875.320  155.120000
Sri Lanka        7.0   885.290  113.347500
Thailand         6.0   829.040  118.750000
UK               3.0   459.860  146.810000
USA              4.0   892.500  207.000000

            Participants
Country
Africa                 9
Australia             10
Cambodia              18
Costa Rica            15
France                10
Germany               13
Greece                15
India                 12
Indonesia             14
Ireland               15
Italy                 13
Mexico                10
Morocco               15
Nepal                 13
Portugal              10
Spain                 10
Sri Lanka             10
Thailand              20
UK                    12
USA                   14
"""

def plotHist(data, labels):
  plt.clf()
  ax = sns.distplot(data['CPD'],bins=50,kde=False,kde_kws={"alpha":0.8})
  range = getDivision(data['CPD'],100)
  range = np.append(range,[data['CPD'].median(),data['CPD'].mean()])
  ax.set_xticks(range)
  plt.xticks(rotation=90)
  med = plt.axvline(data['CPD'].median(),color='g')
  med.set_label("Median CPD")
  med = plt.axvline(data['CPD'].mean(),color='r')
  med.set_label("Mean CPD")
  ax.legend()
  plt.xlabel(labels['x'])
  plt.ylabel(labels['y'])
  plt.title(labels['title'])
  plt.show()

def getDivision(dataSeries, interval):
  interval = float(interval)
  return np.arange(round(dataSeries.min()/interval)*interval,math.ceil(dataSeries.max()/interval)*interval,interval)

dfIndia = df[df['Country']=='India']
#Price Distribution across retreats worldwide
#Figure 1
plotHist(df,{'x':'Lowest Cost Per Day in USD$','y':'# Packages Offered','title':'Price Distribution of Lowest Cost Per Day by Lowest Priced Accomodation Offered (USD) Across All Retreats'})
#Figure 2
plotHist(dfIndia,{'x':'Lowest Cost Per Day in USD$','y':'# Packages Offered','title':'Price Distribution of Lowest Cost Per Day by Lowest Priced Accomodation Offered (USD) Across India'}) #select only India

#CDF of the price of all retreats
x=np.sort(df20['CPD'])
y=np.arange(1,len(x)+1)/len(x)
plt.plot(x,y,marker='.',linestyle='none')
plt.margins(0.02)
plt.show()

#Worldwide, what is the price vs duration of stay?
#Figure 3
sns.lmplot(x='Lowest', y='Duration', data=df,  palette='Set1')
plt.xlabel('Lowest Price in USD$')
plt.ylabel('Duration of Stay (Days)')
plt.title("Duration of Stay VS Price Range (of the Cheapest Accomodation Available) in USD Worldwide")
plt.show()

#In India, what is the price vs duration of stay comparison?
#Figure 4
sns.lmplot(x='Lowest', y='Duration', data=dfIndia,  palette='Set1')
plt.xlabel('Lowest Price in USD$')
plt.ylabel('Duration of Stay (Days)')
plt.title("Duration of Stay VS Price Range (of the Cheapest Accomodation Available) in USD In India")
plt.show()

#Across all retreats, what is the distribution of cost per day?
#Figure 5
c = df20['Country'].unique()
c.sort() #order by country name
cpdtop20=df20[df20['CPD']<1000]
ax = sns.boxplot(x='CPD',y='Country',data=cpdtop20,order=c)
ax.set_xticks(getDivision(cpdtop20['CPD'],100))
plt.xlabel('Cost Per Day (CPD) in USD$')
plt.ylabel('Country')
plt.title("Price Range (of the Cost Per Day) in USD Per Country")
plt.show()

#Which are the premium retreats in India over USD$250?
dfIndia[dfIndia['CPD']>250][['Title','CPD','Rooms']]
"""
                                                  Title         CPD                                              Rooms
1325  8 Days Meditation and Tour Program Yoga Retrea...  282.500000  1 Persons,Shared twin room,Resort,1695.00\n2 P...
790   Powerful Awareness  Mindfulness Retreat  7 Day...  284.914286                 1 Persons,Private cottage,,1994.40
1167  6 Days Unique StressBuster Designed for Relief...  288.166667  1 Persons,Private single room,Resort,1729.00\n...
447   6 Days Spiritual Detox New Year  Life Changing...  315.780000  1 Persons,Private double room,Resort - and Cub...
490   6 Days Spiritual Goddess Life Changing Retreat...  315.780000  1 Persons,Private single room,Resort - and Cub...
1183  8 Days Yoga and Ayurveda Rejuvenation Holiday ...  353.428571  1 Persons,Shared twin room,Hotel,2474.00\n1 Pe...
2164  4 Days Yoga Meditation Ayurveda and Cooking Ho...  387.800000  2 Persons,Private double room,Shared various a...
1201  14 Days Ayurveda Detox and Yoga Retreat in Kar...  419.090769  1 Persons,Private single room,Shared villa,544...
971   8 Days Luxury Ayurvedic Wellbeing Coaching Ret...  513.535714  1 Persons,Private single room,Hotel - Superior...
1055  8 Days Luxury Ayurvedic Wellbeing Coaching Ret...  513.535714  1 Persons,Private single room,Hotel - Superior...
2174  8 Days Yoga Meditation Ayurveda and Cooking Ho...  517.066667  2 Persons,Private double room,Shared various a...
975   6 Days Detox Detour Program and Yoga Retreat i...  524.862000  1 Persons,Private single room,Hotel,2624.31\n2...
6     8 Days Fast Track Private Life Transforming Re...  542.857143  1 Persons,Private single room,Shared various a...
552   7 Days Private Yoga and Meditation Retreat wit...  596.668333  1 Persons,Private cottage,Private cottage - wi...
440   4 Days Luxury Private Spiritual Couple Retreat...  616.325000  2 Persons,Shared double room,Resort - and Cuba...
1739  8 Days Luxury Rejuvenation Package with Ayurve...  659.000000          1 Persons,Shared twin room,Resort,3295.00
444   4 Days Luxury Private Spiritual  Transformativ...  673.110000  1 Persons,Private bungalow,,2692.44\n2 Persons...
"""

#Which are the retreats in India at around the median CPD (Cost per day) range?
dfIndia.sort_values('CPD').iloc[195:205][['Title','CPD','Rooms']]
"""
                                                   Title        CPD                                              Rooms
669   7 Days Meditation Detox and Yoga Retreat in Ka...  75.000000  1 Persons,Shared double room,Shared house,450....
1543  3 Days Yoga and Sightseeing Retreat in Rishike...  75.000000  1 Persons,Private house,Single private room,15...
531     4 Days Yoga and Meditation Holiday in Goa India  75.342500  1 Persons,Shared twin room,Shared cottage,301....
86    14 Days 100Hour Meditation Teacher Training in...  76.707692  1 Persons,Private single room,Shared house - S...
517   7 Days Himalayan Yogic Lifestyle Retreat in Ri...  77.142857  1 Persons,Shared triple room,Retreat center,54...
1034  8 Days Yoga in Nature Meditation and Ayurveda ...  77.184286  1 Persons,Private single room,Resort,540.29\n2...
1120  12 Days 100Hour Ashtanga Yoga Teacher Training...  77.272727  1 Persons,Shared double room,Retreat center,85...
1235  15 Days Panchakarma Yoga and Meditation Retrea...  77.333333  1 Persons,Shared twin room,Retreat center,1160...
289   7 Days Meditation and Yoga Retreat in Gokarna ...  77.500000  1 Persons,Shared double room,Shared bungalow,4...
950   15 Days Meditation and Yoga Retreat in Uttarak...  77.560000  1 Persons,Shared twin room,Retreat center - Tw...
"""

def getRooms(record):
  recs = record.split(",")
  return [recs[0],recs[1],recs[-1]]

#split the packages available into more meaningful data
df2=df['Rooms'].str.split(pat="\n",expand=True)
df=pd.concat([df,df2],axis=1)
df=df.drop(["Rooms"],axis=1)
df=pd.melt(df, id_vars=['Title','Location','Country','Participants','Duration','Lowest','CPD'], value_name='Rooms')
df=df.drop(["variable"],axis=1)
df=df[df['Rooms'].values != None]
roomsFinal = pd.DataFrame([getRooms(i) for i in df['Rooms']])
df=pd.concat([df.reset_index(inplace=False),roomsFinal],axis=1,ignore_index=True)
df=df.drop([0,6,7,8],axis=1)
df.columns=["Title","Location","Country","Participants","Duration","PackagePax","RmType","PackageCost"]
df['PackagePax']=df['PackagePax'].str.split(expand=True)[0].astype(int)
df['RmType'] = df['RmType'].map(lambda x: x.strip().lower())
df['PackageCost'] = df['PackageCost'].astype(float)
df['PackageCostPerDay'] = df['PackageCost']/df['Duration']
df=df.sort_values(['Title','PackageCostPerDay'])
df.to_csv("data_roomprices.tsv",sep="\t",index=False)
dfIndia=df[df['Country']=='India']

#What are the different occupancy offered?
df['PackagePax'].unique() 
"""1,  2,  4, 10,  3,  6,  8,  5"""

#What is the mean pricing per day for a specific room type with 1 occupants?
df[df['PackagePax']==1].groupby(['PackagePax','RmType']).agg(['count','mean','median'])['PackageCostPerDay'].sort_values('median',ascending=False)
dfIndia[dfIndia['PackagePax']==1].groupby(['PackagePax','RmType']).agg(['count','mean','median'])['PackageCostPerDay'].sort_values('median',ascending=False)
#df.groupby(['PackagePax','RmType']).agg(['count','mean','median'])['PackageCostPerDay']
"""
Worldwide:
                                             count        mean      median
PackagePax RmType
1           private tree house                   2  349.750000  349.750000
            private villa                       38  345.432850  327.370893
            shared quad room                     1  258.333333  258.333333
            single room                          1  237.490000  237.490000
            private bungalow                    82  225.863084  230.828810
            private house                       40  209.848173  204.285714
            private twin room                  102  195.215726  192.928571
            private double room                624  213.609701  191.130000
            private yurt                         9  183.015704  188.360000
            private cabin                       21  208.495788  184.666667
            private studio                      14  203.556721  172.846667
            private apartment                   20  164.667340  172.846667
            guest room in main house             1  171.428571  171.428571
            shared room (double bed)             1  170.560000  170.560000
            single                               1  162.500000  162.500000
            shared double room                 462  180.323170  156.702857
            private hut                          1  154.370000  154.370000
            shared room                          2  151.666667  151.666667
            private room + bathroom              1  150.000000  150.000000
            private cottage                     40  202.958528  147.796667
            private single room               1419  184.490917  144.040000
            private room w private bathroom      1  140.000000  140.000000
            shared triple room                 172  162.424645  139.300000
            private triple room                 16  158.139472  136.679643
            shared quadruple room               71  149.004514  125.941667
            ocean single cottage                 1  116.340000  116.340000
            shared twin room                   671  126.678652  109.692000
            private room                         7  151.342844  108.333333
            bring your own tent                  1  107.142857  107.142857
            private tent                        29  122.815839  102.885714
            private lodge                       18  171.258025   96.168222
            ocean twin shared cottage            1   94.180000   94.180000
            shared double/twin room              1   84.200000   84.200000
            garden twin share                    1   83.100000   83.100000
            shared dorm                        270   99.938264   82.820952
            private recreational vehicle         1   73.866667   73.866667
            shared single room                   9  107.417693   64.664000
            garden 4-share                       1   60.940000   60.940000
            beach hut                            2   56.564667   56.564667
            river view twin shared room          1   49.860000   49.860000
            private quadruple room               5   76.289152   42.809091
            shared double rooms                  2   37.500000   37.500000
            tent/tienda de campaña               1   35.714286   35.714286

India:
1           private bungalow               3  433.358286  442.092000
            private hut                    1  154.370000  154.370000
            shared single room             3  135.258492  140.335000
            private lodge                  1  137.445714  137.445714
            private cottage               25  153.758321  125.499333
            private double room           61  128.111831  120.956667
            ocean single cottage           1  116.340000  116.340000
            private room                   1  108.333333  108.333333
            private twin room              6  114.139940  106.842857
            ocean twin shared cottage      1   94.180000   94.180000
            private tent                   2   92.750000   92.750000
            shared room                    1   83.333333   83.333333
            private single room          354  103.296817   83.250000
            garden twin share              1   83.100000   83.100000
            private house                  3   91.363492   75.000000
            shared triple room            14   84.860770   74.591095
            shared double room            91   78.922063   66.666667
            shared twin room             165   84.965538   66.666667
            garden 4-share                 1   60.940000   60.940000
            shared dorm                   52   56.900902   50.000000
            private villa                  4  101.710476   40.930833
            shared quadruple room          6   41.620873   36.999286
            private apartment              1   35.083333   35.083333
"""
#count=df.groupby('RmType').count()['Title'].sort()
#df.groupby('RmType').agg(['count','mean','median'])

#what types of accomodation are most offered worldwide (does not account for number of occupants)?
df.groupby('RmType').count().sort_values('Title',ascending=False)['Title'].head(10)
dfIndia.groupby('RmType').count().sort_values('Title',ascending=False)['Title'].head(10)
"""
Worldwide:
RmType
private double room      1691
private single room      1485
shared twin room          699
shared double room        513
private twin room         494
shared dorm               297
shared triple room        180
private bungalow          135
private triple room        95
shared quadruple room      85

India:
RmType
private single room       379
private double room       238
shared twin room          173
shared double room        101
shared dorm                52
private twin room          43
private cottage            39
private quadruple room     28
shared triple room         14
shared quadruple room      10

Worldwide, most packages offer private double rooms wherest in India more packages are for private single room.
"""

#For all packages offered, how many were packages for X occupants?
#df.groupby('PackagePax').agg(['mean','median','count'])
df.groupby('PackagePax').count()['Title']
"""
PackagePax
1     4164
2     1798
3      132
4       61
5        4
6        6
8        3
10       1

There are 4164 listings for 1 pax.
"""

#Worldwide, for each country, for 1 Occupant/private double rm, what is the average cost?
df[(df['PackagePax']<=2) & (df['RmType']=="private double room")].groupby(['PackagePax','Country'])['PackageCostPerDay'].mean()
df[(df['PackagePax']==1) & (df['RmType']=="private double room")].groupby(['PackagePax','Country'])['PackageCostPerDay'].mean()


#What is the mean pricing for rmtype to number of occupants?
#worldwide
df.pivot_table(index='RmType', columns='PackagePax', values='PackageCostPerDay',aggfunc='mean')
"""
PackagePax                                                1           2           3            4            5           6         8           10
RmType
2 private single rooms                                    NaN  179.714286         NaN          NaN          NaN         NaN       NaN         NaN
beach hut                                           56.564667         NaN         NaN          NaN          NaN         NaN       NaN         NaN
bring your own tent                                107.142857         NaN         NaN          NaN          NaN         NaN       NaN         NaN
doppelzimmer oder apartment                               NaN  266.658333         NaN          NaN          NaN         NaN       NaN         NaN
double room                                               NaN  252.722067         NaN          NaN          NaN         NaN       NaN         NaN
double room - 2 persons sharing (double bed only)         NaN  256.686667         NaN          NaN          NaN         NaN       NaN         NaN
ferienwohnung oder 2 doppelzimmer                         NaN         NaN         NaN   512.818333          NaN         NaN       NaN         NaN
ferienwohnung/apartment                                   NaN         NaN  387.800000          NaN          NaN         NaN       NaN         NaN
garden 4-share                                      60.940000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
garden twin share                                   83.100000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
guest room in main house                           171.428571         NaN         NaN          NaN          NaN         NaN       NaN         NaN
in a 2-room suite                                         NaN  354.560000         NaN          NaN          NaN         NaN       NaN         NaN
ocean single cottage                               116.340000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
ocean twin shared cottage                           94.180000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
private apartment                                  164.667340  235.683413         NaN   505.259444          NaN   588.62500   851.775         NaN
private bungalow                                   225.863084  268.806909  423.224026   522.498413          NaN         NaN       NaN         NaN
private cabin                                      208.495788  275.124405         NaN          NaN          NaN         NaN       NaN         NaN
private cottage                                    202.958528  248.155517         NaN          NaN          NaN         NaN       NaN         NaN
private dorm                                              NaN         NaN  119.664000   469.429048          NaN  1066.17375       NaN         NaN
private double room                                213.609701  331.003175  281.819905   562.775322   460.000000   552.00000       NaN         NaN
private house                                      209.848173  399.237262         NaN          NaN          NaN         NaN       NaN         NaN
private hut                                        154.370000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
private lodge                                      171.258025  257.242730         NaN   385.714286          NaN         NaN       NaN         NaN
private quadruple room                              76.289152         NaN  113.977739   601.410290          NaN         NaN       NaN         NaN
private recreational vehicle                        73.866667  129.266667         NaN          NaN          NaN         NaN       NaN         NaN
private room                                       151.342844  128.333333         NaN          NaN          NaN         NaN       NaN         NaN
private room + bathroom                            150.000000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
private room shared bathroom                              NaN  240.000000         NaN          NaN          NaN         NaN       NaN         NaN
private room w bathroom                                   NaN  280.000000         NaN          NaN          NaN         NaN       NaN         NaN
private room w private bathroom                    140.000000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
private single room                                184.490917  356.522043  387.000000          NaN          NaN         NaN       NaN         NaN
private studio                                     203.556721  371.732229         NaN          NaN          NaN         NaN       NaN         NaN
private tent                                       122.815839  305.239417  154.563000          NaN          NaN         NaN       NaN         NaN
private tree house                                 349.750000  699.750000         NaN          NaN          NaN         NaN       NaN         NaN
private triple room                                158.139472  254.525068  503.990799          NaN          NaN         NaN       NaN         NaN
private twin room                                  195.215726  261.580437  716.647000  1439.200000  1799.000000  2158.80000       NaN         NaN
private villa                                      345.432850  569.489255  900.196607   970.002589  1340.719286         NaN       NaN         NaN
private yurt                                       183.015704  283.309333         NaN   600.000000          NaN         NaN       NaN         NaN
quadruple room                                            NaN         NaN         NaN   585.000000          NaN         NaN       NaN         NaN
river view twin shared room                         49.860000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
shared dorm                                         99.938264  199.365074  281.006667   229.902222          NaN         NaN       NaN         NaN
shared double room                                 180.323170  268.297637         NaN   247.500000          NaN         NaN       NaN         NaN
shared double rooms                                 37.500000   75.000000         NaN          NaN          NaN         NaN       NaN         NaN
shared double/twin room                             84.200000  168.401667         NaN          NaN          NaN         NaN       NaN         NaN
shared quad room                                   258.333333         NaN         NaN          NaN          NaN         NaN       NaN         NaN
shared quadruple room                              149.004514  324.343037         NaN   296.428571          NaN         NaN       NaN         NaN
shared room                                        151.666667  356.235000         NaN          NaN          NaN         NaN       NaN         NaN
shared room (double bed)                           170.560000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
shared single room                                 107.417693         NaN         NaN          NaN          NaN         NaN       NaN         NaN
shared triple room                                 162.424645         NaN  281.132873   247.500000          NaN         NaN       NaN         NaN
shared twin room                                   126.678652  221.915090         NaN          NaN          NaN         NaN  1802.200  381.763529
single                                             162.500000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
single room                                        237.490000         NaN         NaN          NaN          NaN         NaN       NaN         NaN
tent/tienda de campaña                              35.714286         NaN         NaN          NaN          NaN         NaN       NaN         NaN
twin/couple room                                          NaN  129.960000         NaN          NaN          NaN         NaN       NaN         NaN
"""

#What is the mean pricing for rmtype-number of occupants?
#india
dfIndia.pivot_table(index='RmType', columns='PackagePax', values='PackageCostPerDay',aggfunc='mean')
"""
PackagePax                         1           2           3           4
RmType
2 private single rooms            NaN  179.714286         NaN         NaN
double room                       NaN  166.666667         NaN         NaN
garden 4-share              60.940000         NaN         NaN         NaN
garden twin share           83.100000         NaN         NaN         NaN
ocean single cottage       116.340000         NaN         NaN         NaN
ocean twin shared cottage   94.180000         NaN         NaN         NaN
private apartment           35.083333   58.473333         NaN         NaN
private bungalow           433.358286  645.929167         NaN         NaN
private cottage            153.758321  205.621623         NaN         NaN
private double room        128.111831  202.105345         NaN  497.033333
private house               91.363492  142.342857         NaN         NaN
private hut                154.370000         NaN         NaN         NaN
private lodge              137.445714  198.717143         NaN         NaN
private quadruple room            NaN         NaN  113.977739         NaN
private room               108.333333         NaN         NaN         NaN
private single room        103.296817  200.066392         NaN         NaN
private tent                92.750000  433.333333   63.150000         NaN
private triple room               NaN         NaN  269.500357         NaN
private twin room          114.139940  225.120554         NaN         NaN
private villa              101.710476         NaN         NaN         NaN
shared dorm                 56.900902         NaN         NaN         NaN
shared double room          78.922063  401.184567         NaN         NaN
shared quadruple room       41.620873  308.274405         NaN         NaN
shared room                 83.333333         NaN         NaN         NaN
shared single room         135.258492         NaN         NaN         NaN
shared triple room          84.860770         NaN         NaN         NaN
shared twin room            84.965538  144.854369         NaN         NaN
"""
	

#What is the mean duration and room costing for those rooms? (Taking into consideration the number of occupants booking the room together)
df.loc[:,df.columns!='Participants'].groupby(['PackagePax','RmType']).agg(['mean','count'])
#What is the median duration and room costing for those rooms? (Taking into consideration the number of occupants booking the room together)
df.loc[:,df.columns!='Participants'].groupby(['PackagePax','RmType']).median()