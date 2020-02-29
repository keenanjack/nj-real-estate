from django.db import models

# Create your models here.

class RawData (models.Model):
    municipality = models.CharField(max_length=255, null=True)
    block = models.CharField(max_length=255, null=True)
    lot = models.CharField(max_length=255, null=True)
    qual = models.CharField(max_length=255, null=True)
    propertylocation = models.CharField(max_length=255, null=True)
    propertyclass = models.CharField(max_length=255, null=True)
    ownername = models.CharField(max_length=255, null=True)
    owneraddress = models.CharField(max_length=255, null=True)
    ownercitystatezip = models.CharField(max_length=255, null=True)
    sqft = models.CharField(max_length=255, null=True)
    yrbuilt = models.CharField(max_length=255, null=True)
    buildingclass = models.CharField(max_length=255, null=True)
    priorblock = models.CharField(max_length=255, null=True)
    priorlot = models.CharField(max_length=255, null=True)
    priorqual = models.CharField(max_length=255, null=True)
    updated = models.CharField(max_length=255, null=True)
    zone = models.CharField(max_length=255, null=True)
    account = models.CharField(max_length=255, null=True)
    mortgageaccount = models.CharField(max_length=255, null=True)
    bankcode = models.CharField(max_length=255, null=True)
    sptaxcred1 = models.CharField(max_length=255, null=True)
    sptaxcred2 = models.CharField(max_length=255, null=True)
    sptaxcred3 = models.CharField(max_length=255, null=True)
    sptaxcred4 = models.CharField(max_length=255, null=True)
    mappage = models.CharField(max_length=255, null=True)
    additionallots = models.CharField(max_length=255, null=True)
    landdesc = models.CharField(max_length=255, null=True)
    buildingdesc = models.CharField(max_length=255, null=True)
    classcode = models.CharField(max_length=255, null=True)
    acreage = models.CharField(max_length=255, null=True)
    eplown = models.CharField(max_length=255, null=True)
    epluse = models.CharField(max_length=255, null=True)
    epldesc = models.CharField(max_length=255, null=True)
    eplstatute = models.CharField(max_length=255, null=True)
    eplinit = models.CharField(max_length=255, null=True)
    eplfurther = models.CharField(max_length=255, null=True)
    eplfacilityname = models.CharField(max_length=255, null=True)
    taxes1 = models.CharField(max_length=255, null=True)
    taxes2 = models.CharField(max_length=255, null=True)
    taxes3 = models.CharField(max_length=255, null=True)
    taxes4 = models.CharField(max_length=255, null=True)
    saledate = models.CharField(max_length=255, null=True)
    deedbook = models.CharField(max_length=255, null=True)
    deedpage = models.CharField(max_length=255, null=True)
    saleprice = models.CharField(max_length=255, null=True)
    nucode = models.CharField(max_length=255, null=True)
    #total assessed value / sales value. 
    ratio = models.CharField(max_length=255, null=True)
    typeuse = models.CharField(max_length=255, null=True)
    year1 = models.CharField(max_length=255, null=True)
    owner1 = models.CharField(max_length=255, null=True)
    street1 = models.CharField(max_length=255, null=True)
    owner1citystatezip = models.CharField(max_length=255, null=True)
    landassmnt1 = models.CharField(max_length=255, null=True)
    buildingassmnt1 = models.CharField(max_length=255, null=True)
    exempt1 = models.CharField(max_length=255, null=True)
    totalassmnt1 = models.CharField(max_length=255, null=True)
    assessed1 = models.CharField(max_length=255, null=True)
    year2 = models.CharField(max_length=255, null=True)
    owner2 = models.CharField(max_length=255, null=True)
    street2 = models.CharField(max_length=255, null=True)
    owner2citystatezip = models.CharField(max_length=255, null=True)
    landassmnt2 = models.CharField(max_length=255, null=True)
    buildingassmnt2 = models.CharField(max_length=255, null=True)
    exempt2 = models.CharField(max_length=255, null=True)
    totalassmnt2 = models.CharField(max_length=255, null=True)
    assessed2 = models.CharField(max_length=255, null=True)
    year3 = models.CharField(max_length=255, null=True)
    owner3 = models.CharField(max_length=255, null=True)
    street3 = models.CharField(max_length=255, null=True)
    owner3citystatezip = models.CharField(max_length=255, null=True)
    landassmnt3 = models.CharField(max_length=255, null=True)
    buildingassmnt3 = models.CharField(max_length=255, null=True)
    exempt3 = models.CharField(max_length=255, null=True)
    totalassmnt3 = models.CharField(max_length=255, null=True)
    assessed3 = models.CharField(max_length=255, null=True)
    year4 = models.CharField(max_length=255, null=True)
    owner4 = models.CharField(max_length=255, null=True)
    street4 = models.CharField(max_length=255, null=True)
    owner4citystatezip = models.CharField(max_length=255, null=True)
    landassmnt4 = models.CharField(max_length=255, null=True)
    buildingassmnt4 = models.CharField(max_length=255, null=True)
    exempt4 = models.CharField(max_length=255, null=True)
    totalassmnt4 = models.CharField(max_length=255, null=True)
    assessed4 = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    neigh = models.CharField(max_length=255, null=True)
    vcs = models.CharField(max_length=255, null=True)
    stydesc = models.CharField(max_length=255, null=True)
    style = models.CharField(max_length=255, null=True)

class Municipalities(models.Model):
    code = models.CharField(max_length=4)
    municipality = models.CharField(max_length=255)
    county = models.CharField(max_length=255)

class Propertyclassifications(models.Model):
    symbol = models.CharField(max_length=3)
    category = models.CharField(max_length=60)

class Qualificationcodes(models.Model):
    qual = models.CharField(max_length=5)
    description = models.CharField(max_length=255)