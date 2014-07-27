# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from blasbase.models import Person, SpecialDiet, PersonAddress,PersonPhoneNumber
from datetime import datetime
import pycountry
import MySQLdb

class Command(BaseCommand):
    help = 'Syncronizes persons from mysql'

    def handle(self, *args, **options):
        gluten = SpecialDiet.objects.get_or_create(name='Glutenallergi')[0]
        veg = SpecialDiet.objects.get_or_create(name='Vegetarian')[0]
        nykter = SpecialDiet.objects.get_or_create(name='Nykterist')[0]
        print u"Öppnar mysqldatabasen"
        db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="blasare", # your username
                      passwd="bajsare", # your password
                      db="litheblas",
                      port=3307,
                      charset='utf8' ) # name of the data base
        print u"Hämtar data från mysql"
        cur = db.cursor()
        cur.execute("SELECT fnamn,smek,enamn,kon,fodd,pnr_sista,studentid,fritext,allergi,gluten,veg,nykter,gatuadr,postnr,ort,land,hemnr,mobilnr,jobbnr FROM person")
        for row in cur.fetchall() :
            person = Person()
            person.first_name = row[0]
            if row[1]:
                person.nickname = row[1]
            else:
                person.nickname = ""
            person.last_name = row[2]
            if row[3] == 'M':
                person.gender = 'm'
            elif row[3] == 'K':
                person.gender = 'f'
            else:
                person.gender = ""
            person.born = row[4]
            person.deceased = None
            if row[5]:
                person.personal_id_number = row[5]
            else:
                person.personal_id_number = ""
            if row[6]:
                person.liu_id = row[6]
            else:
                person.liu_id = ""
            if row[7]:
                person.about = row[7]
            else:
                person.about = ""
            if row[8]:
                person.special_diets_extra = row[8]
            else:
                person.special_diets_extra = ""
            person.save()
            if row[9] == 'Y':
                person.special_diets.add(gluten)
            if row[10] == 'Y':
                person.special_diets.add(veg)
            if row[11] == 'Y':
                person.special_diets.add(nykter)
            paddress = PersonAddress()
            paddress.type = 'private'
            paddress.person = person
            if row[12]:
                paddress.address = row[12]
            else:
                paddress.address = ""
            if row[13]:
                paddress.post_code = row[13]
            else:
                paddress.post_code = ""
            if row[14]:
                paddress.city = row[14]
            else:
                paddress.city = ""
            """ Skitfult men jag är lat! """

            if row[15] and row[15] != "":
                if row[15].lower() == 'belgien':
                    paddress.country = pycountry.countries.get(name='Belgium').alpha2
                if row[15].lower() == 'estland':
                    paddress.country = pycountry.countries.get(name='Estonia').alpha2
                if row[15].lower() == 'frankrike' or row[15].lower() == 'france':
                    paddress.country = pycountry.countries.get(name='France').alpha2
                if row[15].lower() == 'indien':
                    paddress.country = pycountry.countries.get(name='India').alpha2
                if row[15].lower() == 'italien':
                    paddress.country = pycountry.countries.get(name='Italy').alpha2
                if row[15].lower() == 'japan':
                    paddress.country = pycountry.countries.get(name='Japan').alpha2
                if row[15].lower() == 'austria' or row[15].lower() == u'österrike':
                    paddress.country = pycountry.countries.get(name='Austria').alpha2
                if row[15] == 'USA':
                    paddress.country = pycountry.countries.get(name='United States').alpha2
                if row[15].lower() == 'tyskland':
                    paddress.country = pycountry.countries.get(name='Germany').alpha2
                if row[15].lower() == 'tjeckien':
                    paddress.country = pycountry.countries.get(name='Czech Republic').alpha2
                if row[15].lower() == 'storbritannien' or row[15].lower() == 'england':
                    paddress.country = pycountry.countries.get(name='United Kingdom').alpha2
                if row[15].lower() == 'schweiz':
                    paddress.country = pycountry.countries.get(name='Switzerland').alpha2
                if row[15].lower() == 'norge':
                    paddress.country = pycountry.countries.get(name='Norway').alpha2
                if row[15].lower() == 'mongoliet':
                    paddress.country = pycountry.countries.get(name='Mongolia').alpha2
            paddress.save()
            if row[16] != "" and row[16]:
                ptel = PersonPhoneNumber()
                ptel.phone_number = row[16]
                ptel.person = person;
                ptel.type = 'private'
                ptel.save()
            if row[17] != "" and row[17]:
                ptel = PersonPhoneNumber()
                ptel.phone_number = row[17]
                ptel.person = person;
                ptel.type = 'private'
                ptel.save()
            if row[18] != "" and row[18]:
                ptel = PersonPhoneNumber()
                ptel.phone_number = row[18]
                ptel.person = person;
                ptel.type = 'work'
                ptel.save()
            person.save()
            """Not yet added """
            """
               Assignments
               Avatars
               Magnet Cards
               Users
               Rättigheter
               Grupper
               Land
               test.posts


               Information not taken from old database:

                    litheblas.person:
                        icqnr - Ta bort?
                        blasmail - Username
                        gras_medlem_till
                        arbete
                        icke_blasare
                        password - Vi hämtar nog inte den
                        nomail
                        admin
                        sedd_av_anv - Vi hämtar nog inte den
                        latlong
                        epost_utskick
                        senast_kollad - Vi hämtar nog inte den



            Unika länder att lägga till:
            'Austria',
            'AUSTRIA',
            'Belgien',
            'England',
            'Estland',
            'France',
            'Frankrike',
            'HEMLIGT',
            'Indien',
            'Italien',
            'Japan',
            'Mongoliet',
            'Norge',
            'Schweden',
            'Schweiz',
            'Skåne',
            'Storbritannien',
            'Sverige',
            'SVERIGE',
            'Sweden',
            'Tjeckien',
            'Tyskland',
            'TYSKLAND',
            'USA',
            'Österrike'
               """







