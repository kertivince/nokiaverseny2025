import math as ma
import sympy as eq


#derékszögű háromszög: átfogók: R-1; R-2, befogó: R
#R=sqrt(pow(R-1, 2) + pow(R-2, 2))
# R= 1; 5   - egy nem lehet ábrából következően
print('1.: 5')


print('2.:')


task3 = 0
for i in range(1, 100):
    task3+=1/(ma.sqrt(i) + ma.sqrt(i+1))
print(f"3.: {task3}")

print('4.: 1')
print('5.:')


# ez egy két egyenletes egyenletrendszer(3 benne az ismeretlen) => módszer: össze kell adnunk a két egyenletet:
# I. m+a-t=170
#II. -m+a-t=130
#ezeket összeadva:
# 2a = 300
# a=150
print('6.: 150')



# 7. feladat
# ez egy 3 ismeretlenes egyenletrendszer
# elnevezem az állatokat macska = m; kutya = k; egér = e
# fölírom az így kapott egyenletrendszert:
#   I. m+e=10
#  II. e+k=20
# III. k+m=24
# az I-ből kifejezem m-et -> m=10-e
# ezt behelyettesítem a III. egyenletbe, majd rendezem azt:
# k+(10-e)=24
# k-e=14   ebből kifejezem k-t: k=14+e
# ezt behelyettesítem a II. egyenletbe:
# e+(14+e)=20
# 2e=6
# e=3     -- megvan, hogy az egér 3kg-ot nyom!
# kiszámolom, hogy mennyi a macska az I. egyenletből:
# m+3=10
# m=7   ----- megvan a macska: 7kg
# a III-ból kifejezem a kutyát:
# k+7=24
# k=17    ---- megvan a kutya: 17kg
#összesen: 17+7+3 = 27
print('7.: 27')


