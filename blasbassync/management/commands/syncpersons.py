# -*- coding: utf-8 -*-
import requests
from BeautifulSoup import BeautifulSoup, Tag,NavigableString

from django.core.management.base import BaseCommand, CommandError
from blasbase.models import Person, SpecialDiet, PersonAddress,PersonPhoneNumber,User,Function,Assignment
from datetime import datetime
from cards.models import MagnetCard
from django.conf import settings
import pycountry
import MySQLdb

from sys import stdout
import sys
from events.models import Event, EventInformation

class Command(BaseCommand):
    help = 'Syncronizes persons from mysql'
    def handle(self, *args, **options):
        print u"Öppnar mysqldatabasen"
        db = MySQLdb.connect(host="127.0.0.1", user=settings.OLD_DATABASE_USER, passwd=settings.OLD_DATABASE_PASSWORD,
                             db="litheblas", port=3307, charset='utf8')
        print u"Hämtar data för sektioner"
        instrument_dictionary = self.create_sections(db)
        print u"Hämtar data för funktioner"
        function_dictionary = self.create_functions(db)
        #print u"Hämtar data från persontabellen"
        #self.loop_through_persons(db, instrument_dictionary, function_dictionary)
        print u"Hämtar data från events"
        self.import_events(db)
        """
                Assignments
               Avatars
               Rättigheter
               Grupper
               test.posts


        """
    def create_functions(self,db):
        funktion = Function()
        funktion.name = "Funktioner"
        funktion.save()
        styrelse = Function()
        styrelse.name = "Styrelse"
        styrelse.parent = funktion
        styrelse.save()
        hedersmedlem = Function()
        hedersmedlem.name = "Hedersmedlem"
        hedersmedlem.save()

        function_dictionary = {}
        cur = db.cursor()
        cur.execute("SELECT namn, styr, beskr,funkid from funk")
        for row in cur.fetchall():
            tempFunc = Function()
            tempFunc.name = row[0]
            if row[1] == 'Y':
                tempFunc.parent=styrelse
            else:
                tempFunc.parent=funktion
            tempFunc.engagement = True
            tempFunc.description = row[2]
            tempFunc.save()
            function_dictionary[int(row[3])] = tempFunc
        return function_dictionary

    def create_instruments(self,sektid,sektion,db,instrument_dictionary):
        cur = db.cursor()
        cur.execute("SELECT lnamn,instrid from instrument where sekt = %s", (sektid,))
        for row in cur.fetchall():
            tempFunction = Function()
            tempFunction.name = row[0]
            tempFunction.description = ""
            tempFunction.parent = sektion
            tempFunction.membership = True
            tempFunction.save()
            instrument_dictionary[int(row[1])] = tempFunction
        if sektid == 10:
            tempFunction = Function()
            tempFunction.name = "Okänt instrument"
            tempFunction.description = ""
            tempFunction.parent = sektion
            tempFunction.membership = True
            tempFunction.save()

    def create_sections(self,db):
        litheblasFunc = Function()
        litheblasFunc.name = "Blåssektioner"
        litheblasFunc.description = "Medlem i en Lithe Blås-sektion"
        litheblasFunc.save()
        instrument_dictionary = {}
        cur = db.cursor()
        cur.execute("SELECT sektid,knamn,lnamn, listordning from sektion")
        for row in cur.fetchall():
            tempFunction = Function()
            tempFunction.name = row[1]
            tempFunction.description = row[2]
            tempFunction.parent = litheblasFunc
            tempFunction.save()
            self.create_instruments(row[0],tempFunction,db,instrument_dictionary)

        return instrument_dictionary
        """
         Information not taken from old database:
            hemsida
            listordning
        """


    def import_events(self,db):
        cur = db.cursor()
        cur.execute("SELECT id,dag,tid, plats, fritext FROM pagang where dag >='2010-01-01'")
        for row in cur.fetchall() :
            if row[4]:
                soup = BeautifulSoup(row[4])
                e = Event()
                for title in soup.findAll('h1'):
                    #tit = str(title.text).decode('utf-8')
                    #print tit.encode(sys.stdout.encoding, errors='replace')

                    e.name = title.text
                    e.start = datetime.combine(row[1],datetime.min.time()) #datetime.combine(row[1],row[2])
                    e.start = e.start + row[2]
                    e.save()
                    eventString = ""
                    next = title.nextSibling
                    while(next):
                        eventString += str(next)
                        next = next.nextSibling

                    #Remove all tags from eventString

                    ei = EventInformation()
                    ei.event = e
                    ei.content = eventString
                    ei.save()
                #if tit:
                #    pass
            """parser.feed(row[4])
            if parser.success and parser.name != "":
                print "Event:"
                print parser.name
                print "Row:"
                print row[4].encode(sys.stdout.encoding, errors='replace')
                e = Event()
                e.name = parser.name
                e.start = row[1]
                e.save()"""
            #for line in parser.data:
            #    print line.encode(sys.stdout.encoding, errors='replace')
            #                if row[1] == None:
            #                e.start = datetime(1990,1,1)
            #            else:



            #print parser.data

    def loop_through_persons(self,db,instrument_dictionary,function_dictionary):
        gluten = SpecialDiet.objects.get_or_create(name='Glutenallergi')[0]
        veg = SpecialDiet.objects.get_or_create(name='Vegetarian')[0]
        nykter = SpecialDiet.objects.get_or_create(name='Nykterist')[0]

        cur = db.cursor()
        cur.execute("SELECT fnamn,smek,enamn,kon,fodd,pnr_sista,studentid,fritext,allergi,gluten,veg,nykter,gatuadr,postnr,ort,land,hemnr,mobilnr,jobbnr,latlong,persid,blasmail,epost FROM person")
        total = cur.rowcount
        #Improviserad progressbar
        count = 1
        for row in cur.fetchall() :
            stdout.write("Adding person %d/%d   \r" % (count, total) )
            stdout.flush()
            count += 1
            person = Person()
            person.first_name = row[0]
            person.nickname = self.word_or_string(row[1])
            person.last_name = row[2]
            person.gender = self.translate_gender(row[3])
            person.born = row[4]
            person.deceased = None
            person.personal_id_number = self.word_or_string(row[5])
            person.liu_id = self.word_or_string(row[6])
            person.about = self.word_or_string(row[7])
            person.special_diets_extra = self.word_or_string(row[8])
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
            paddress.address = self.word_or_string(row[12])
            paddress.post_code = self.word_or_string(row[13])
            paddress.city = self.word_or_string(row[14])
            if row[15] and row[15] != "":
                paddress.country = self.translate_country(row[15])

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
            """ row[19] innehåller latlong men ingenstans att stoppa in den """
            """ row[20] innehåller persid """
            person.old_database_id = row[20]
            self.get_cards(db,row[20],person)
            """ row[21] innehåller blasmail """
            if row[21]:
                puser = User()
                puser.username = row[21]
                puser.is_active = True
                puser.person = person
                puser.save()
            self.get_instruments(db,row[20],person,instrument_dictionary)
            self.get_functions(db,row[20],person,function_dictionary)
            person.save()
            """               Information not taken from old database:

                        icqnr - Ta bort?
                        gras_medlem_till - Finns inget fält
                        arbete - Finns inget fält
                        icke_blasare - Rättigheter?
                        password - Vi hämtar nog inte den
                        nomail - Finns inget fält
                        admin - Rättigheter
                        sedd_av_anv - Vi hämtar nog inte den
                        latlong - Finns inget fält
                        epost_utskick - Finns inget fält
                        senast_kollad - Vi hämtar nog inte den



            """
    def get_functions(self,db,persid,person,function_dictionary):
        cur = db.cursor()
        cur.execute("SELECT pers,funk,startdatum,slutdatum from persfunk where pers=%s",(persid,))
        for row in cur.fetchall():
            tempA = Assignment()
            tempA.start = row[2]
            if str(row[3]) != '9999-12-31':
                tempA.end = row[3]
            tempA.function = function_dictionary[int(row[1])]
            tempA.person = person
            tempA.save()

    def get_instruments(self,db,persid,person,instrument_dictionary):
        cur = db.cursor()
        cur.execute("SELECT pers,datum,typ,instr from medlem where pers=%s ORDER BY datum",(persid,))
        last = None
        for row in cur.fetchall():
            if row[2] == 'prov':
                tempA = Assignment()
                tempA.start = row[1]
                tempA.person = person
                tempA.trial = True
                tempA.function = instrument_dictionary[int(row[3])]
                tempA.save()
                last=tempA
            elif row[2] == 'antagen':
                tempA = Assignment()
                tempA.start = row[1]
                tempA.person = person
                if last:
                    if last.end == None:
                        if str(row[1]) != '9999-12-31':
                            last.end = row[1]
                            last.save()
                tempA.function = instrument_dictionary[int(row[3])]
                tempA.save()
                last=tempA
            elif row[2] == 'gamling':
                if last:
                    if last.end == None:
                        if str(row[1]) != '9999-12-31':
                            last.end = row[1]
                            last.save()
                else:
                    tempA = Assignment()
                    if str(row[1]) != '9999-12-31':
                        tempA.end = row[1]
                    tempA.person = person
                    tempA.function = Function.objects.get(name="Okänt instrument")
                    tempA.save()

            elif row[2] == 'heder':
                tempA=Assignment()
                tempA.start = row[1]
                tempA.person = person
                tempA.function = Function.objects.get(name="Hedersmedlem")
                tempA.save()
                tempA.save()
                last = tempA

    def get_cards(self,db,persid,person):
        cur2 = db.cursor()
        cur2.execute("SELECT nummer,aktiv FROM kort WHERE persid=%s", (persid,))
        oldnumber = ""
        for row2 in cur2.fetchall():
            if row2[0] != oldnumber:
                #För att undvika dubletter
                oldnumber = row2[0]
                mk = MagnetCard()
                mk.person = person
                mk.card_data = row2[0]
                mk.enabled = row2[1]
                mk.description = "Automatically imported from old database"
                mk.save()
    def word_or_string(self,word):
        if word:
            return word
        else:
            return ""
    def translate_gender(self,gender):
        if gender == 'M':
            return 'm'
        elif gender == 'K':
            return 'f'
        else:
            return ""
    def translate_country(self,country):
        if country.lower() == 'belgien':
            return pycountry.countries.get(name='Belgium').alpha2
        if country.lower() == 'estland':
            return pycountry.countries.get(name='Estonia').alpha2
        if country.lower() == 'frankrike' or country.lower() == 'france':
            return pycountry.countries.get(name='France').alpha2
        if country.lower() == 'indien':
            return pycountry.countries.get(name='India').alpha2
        if country.lower() == 'italien':
            return pycountry.countries.get(name='Italy').alpha2
        if country.lower() == 'japan':
            return pycountry.countries.get(name='Japan').alpha2
        if country.lower() == 'austria' or country.lower() == u'österrike':
            return pycountry.countries.get(name='Austria').alpha2
        if country == 'USA':
            return pycountry.countries.get(name='United States').alpha2
        if country.lower() == 'tyskland':
            return pycountry.countries.get(name='Germany').alpha2
        if country.lower() == 'tjeckien':
            return pycountry.countries.get(name='Czech Republic').alpha2
        if country.lower() == 'storbritannien' or country.lower() == 'england':
            return pycountry.countries.get(name='United Kingdom').alpha2
        if country.lower() == 'schweiz':
            return pycountry.countries.get(name='Switzerland').alpha2
        if country.lower() == 'norge':
            return pycountry.countries.get(name='Norway').alpha2
        if country.lower() == 'mongoliet':
            return pycountry.countries.get(name='Mongolia').alpha2
        else:
            return pycountry.countries.get(name='Sweden').alpha2




