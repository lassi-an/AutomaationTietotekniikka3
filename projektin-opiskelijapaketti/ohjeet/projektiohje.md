# Ohjelmistotuotannon projekti tekoälyavusteisesti

Arviointiperusteet ovat [projektin arviointikriteereissä](projektin-arviointikriteerit.md) ja [arvosanan laskennassa](arvosanan-laskenta.md). Palautusajat ja yhteiset työskentelyohjeet ovat Moodlen kurssijärjestelysivulla.

## Tavoite ja tehtävä

Suunnittele, määrittele, toteuta, testaa ja esittele parisi kanssa toimiva ohjelmistokokonaisuus. Valitkaa itse aihe, joka kiinnostaa teitä ja jolle pystytte kuvaamaan selkeän käyttäjän, tarpeen ja hyödyn. Myös harrastukseen tai omaan arkeen liittyvä aihe sopii. Kaupallista kannattavuutta, teollista tietolähdettä tai automaatiokytkentää ei edellytetä.

Tavoitteena on osoittaa koko ohjelmistotuotannon ketju: käyttäjätarve ohjaa vaatimuksia, vaatimukset toteutusta ja testaus osoittaa niiden täyttymisen. Validoinnissa perustelette, vastaako ratkaisu alkuperäiseen tarpeeseen.

Tekoälyä saa ja on tarkoitus käyttää projektissa. Vastaatte sen avulla tekemistänne ratkaisuista, tarkistatte tuotokset ja osaatte selittää oman työnne. Teknologia ja ratkaisutapa ovat valittavissanne. Agenttiympäristö tai maksullinen AI-tilaus ei ole edellytys.

Kurssin automaatioesimerkeissä painottuvat tiedonkeruu, käsittely, analyysi ja visualisointi. PLC-ohjelmointi ei ole projektivaatimus. Pilvipalveluja ja Big Dataa käsitellään yhteisessä teoriassa, tehtävissä ja tentissä; niitä ei tarvitse toteuttaa omassa projektissa. Pilvitiliä tai pilveen käyttöönottoa ei vaadita.

## Rajaa toteutettava kokonaisuus

Valitkaa yksi keskeinen käyttäjän tavoite, joka voidaan toteuttaa päästä päähän ja näyttää toiminnassa. Pelkkä idea, käyttöliittymäluonnos tai AI:n tuottama koodi ilman toimivuuden näyttöä ei riitä.

Projektista pitää käydä ilmi:

- kenelle ratkaisu tehdään, mikä ongelma ratkaistaan ja mitä hyötyä siitä on;
- mitä käyttäjä voi valmiilla ohjelmistolla tehdä;
- mitkä ovat tärkeimmät testattavat vaatimukset ja hyväksymiskriteerit;
- miten ohjelmisto käynnistetään, miten sen toimintaa tarkistetaan ja mitkä ovat tunnetut rajoitukset;
- miten kumpikin opiskelija osallistui suunnitteluun, toteutukseen ja tarkistamiseen.

Jos tarvitsette dataa, voitte käyttää esimerkiksi itse tuotettua synteettistä dataa, tiedostoa tai paikallista simulaattoria. Kuvatkaa datan alkuperä, käyttöoikeus tai oma tuotantotapa sekä olennaiset oletukset ja rajoitukset. Projektin pitää olla opettajan kokeiltavissa README:n ohjeella ilman teidän henkilökohtaisia maksullisia tunnuksianne.

Rajattu ja perusteltu toteutus voi menestyä yhtä hyvin kuin laaja sovellus. Ominaisuuksien, koodirivien tai promptien määrä ei tuo sellaisenaan pisteitä.

## Työn vaiheet

### 1. Tarve, arvolupaus ja käyttäjäskenaariot

Kuvatkaa ongelma, käyttäjä ja nykyinen toimintatapa. Perustelkaa, mitä hyötyä ratkaisusta olisi. Kuvatkaa 1–3 konkreettista käyttäjäskenaariota: kuka tekee, mitä tavoittelee, missä tilanteessa ja millaisen tuloksen saa. Oma todellinen käyttötarve on kelvollinen lähtökohta.

### 2. Vaatimukset ja rajaus

Kirjatkaa projektin tavoite, toteutettava vähimmäiskokonaisuus, ulkopuolelle jätettävät asiat sekä keskeiset oletukset ja riskit. Määritelkää noin 3–5 tärkeintä toiminnallista vaatimusta ja tarpeelliset laatuvaatimukset. Määrä on rajausohje, ei pisteperuste.

Antakaa vaatimuksille tunnisteet, esimerkiksi V1 ja V2. Kirjatkaa jokaiselle hyväksymiskriteeri: millä havainnolla voidaan osoittaa, että vaatimus täyttyy? Vaatimuksia saa tarkentaa projektin edetessä; dokumentoikaa merkittävien muutosten syyt. Älkää muuttako toteutumatta jääneitä vaatimuksia jälkikäteen onnistuneiksi ilman perusteltua rajauspäätöstä.

### 3. Alkuprompt ja jatkuva AI-työskentely

Tallentakaa todellisuudessa käyttämänne alkuprompt Markdownina. Sen tulee perustua tavoitteeseen, käyttäjiin, vaatimuksiin ja rajauksiin. Alkupromptin ei tarvitse tuottaa koko sovellusta kerralla.

Agenttisessa ympäristössä luokaa repon juureen **`AGENTS.md`**, jossa kuvataan projektin pysyvät ohjeet: tavoite ja rajat, työskentelykäytännöt sekä muutosten katselmointi ja testaus. Ohjeen tulee vastata todellista työtapaa. Jos ympäristö ei lue tiedostoa automaattisesti, kuvatkaa, miten ohje annetaan sille.

Ilman agenttista ympäristöä kuvatkaa vastaava prosessi tiedostossa `docs/02-ai-tyoskentely.md`: miten annatte kontekstin, jaatte työn tehtäviin, tarkistatte ehdotukset ja siirrätte hyväksytyt ratkaisut toteutukseen. Tällöin `AGENTS.md` ei ole pakollinen. Näitä tapoja arvioidaan samoilla tavoitteilla.

Listatkaa kaikki projektissa käytetyt AI-työkalut, myös dokumentoinnissa käytetyt. Sopiva taulukko on:

| Työkalu | Malli tai versio, jos tiedossa | Käyttötarkoitus | Miten tuotoksia tarkistettiin? |
|---|---|---|---|
| Käytetty työkalu | Tiedossa oleva tieto tai ”ei tiedossa” | Konkreettinen käyttötapa | Oma tarkistuskäytäntö |

Kuvatkaa lisäksi yksi konkreettinen tilanne, jossa hyväksyitte, korjasitte tai hylkäsitte AI:n ehdotuksen. Perustelkaa ratkaisu havainnoilla. Koko keskusteluhistoriaa ei tarvitse palauttaa. Älkää syöttäkö työkaluihin salasanoja, avaimia tai henkilötietoja.

### 4. Toteutus ja yhteistyö Gitissä

Toteuttakaa toimiva kokonaisuus ja pitäkää dokumentaatio ajan tasalla. Käyttäkää yhteistä projektirepoa työn aikana, ei vain lopputuloksen palautuspaikkana. Tallentakaa ymmärrettäviä muutoksia ja katselmoikaa myös toistenne työtä. Molempien pitää voida osoittaa oma osallistumisensa. Commitien lukumäärää ei pisteytetä.

README kertoo käynnistyksen, riippuvuudet, tarvittavat asetukset, esimerkkikäytön ja testien suorittamisen. Tarvittavat asetusesimerkit eivät saa sisältää oikeita salaisuuksia. Merkitkää muualta otetun koodin ja aineiston lähteet sekä käyttöehdot niiden edellyttämällä tavalla.

### 5. Testaus ja validointi

Testatkaa tärkeimmät vaatimukset sekä vähintään yksi projektinne kannalta olennainen virhe- tai rajatapaus. Menetelmä voi olla automatisoitu testi tai toistettava käsin tehtävä koe. Menetelmä valitaan tavoitteen mukaan.

Kirjatkaa testin yhteys vaatimukseen, testitapa tai syöte, odotettu tulos, havaittu tulos ja johtopäätös. Raportoikaa myös epäonnistumiset ja tunnetut puutteet. AI:n ilmoitus ”testattu” ei yksin ole testinäyttö.

Validoinnissa palatkaa käyttäjäskenaarioon: pystyykö käyttäjä saavuttamaan alkuperäisen tavoitteen ja mitä hyötyä siitä syntyy? Kuvatkaa kokeilu tai muu perusteltu havainto. Ulkopuolista asiakasta ei vaadita; jos kokeilette itse, kertokaa tämän rajoitus. Tekninen testaus ja käyttäjätarpeen arviointi käsitellään erikseen.

## Repon vakiorakenne ja palautettavat dokumentit

Kaikki itse laatimanne projektin tekstidokumentit ovat Markdown-tiedostoja opiskelijaprojektin omassa Git-repossa. Koodi, data, kuvat ja asetustiedostot käyttävät tarkoitukseensa sopivia muotoja. Reflektio, Moodle-esitehtävät ja henkilökohtaiset vertaisarvioinnit palautetaan Moodlessa.

```text
projektin-nimi/
├── README.md
├── AGENTS.md                       # agenttisessa ympäristössä
├── .gitignore
├── docs/
│   ├── 01-projektikuvaus.md
│   ├── 02-ai-tyoskentely.md
│   ├── 03-testaus-ja-validointi.md
│   ├── 04-palautus.md
│   ├── 05-toimintasuunnitelma.md    # jos täydennätte projektipisteitä
│   └── kuvat/                      # tarvittaessa
└── toteutuksen tiedostot ja kansiot
```

| Tiedosto | Mitä siihen kirjoitetaan? |
|---|---|
| `README.md` | Projektin nimi ja tekijät, tarkoitus, käynnistys, käyttö ja testaus; toteutuksen ja testien sijainnit sekä linkit alla oleviin dokumentteihin |
| `01-projektikuvaus.md` | Tarve ja arvolupaus, käyttäjäskenaariot, vaatimukset ja hyväksymiskriteerit, rajaus, keskeinen rakenne sekä oletukset |
| `02-ai-tyoskentely.md` | Alkuprompt, työkaluluettelo, työnjako ja kummankin konkreettinen osuus, AI-tuotoksen tarkistusesimerkki; linkki `AGENTS.md`:hen tai vastaava prosessikuvaus |
| `03-testaus-ja-validointi.md` | Vaatimuksiin sidotut testit ja tulokset, validointi käyttäjätarpeeseen nähden sekä tunnetut puutteet |
| `04-palautus.md` | Palautuspäivä, videolinkki ja mahdolliset erityisohjeet arvioijalle |
| `05-toimintasuunnitelma.md` | Palautteen analyysi ja perusteltu jatkokehityssuunnitelma |

Numeroidut dokumentit ovat `docs/`-kansiossa. Älkää kopioiko samaa sisältöä useaan tiedostoon: käyttäkää linkkejä. Toteutuksen kansiot saavat noudattaa valitun teknologian käytäntöjä. Tyhjiä kansioita ei vaadita. Kirjoittakaa tiiviisti; dokumenttien sivumäärää ei arvioida.

## Projektivideo ja vertaisarviointi

Tehkää parina **5–7 minuutin video**. Esitelkää ongelma ja käyttäjätarve, yksi toimiva keskeinen käyttötapaus, yksi testauksen tulos ja tärkein tunnettu rajoitus. Molemmat opiskelijat selittävät oman osuutensa. Ruuduntallennus puheella riittää; editointia tai esiintymisen laatua ei pisteytetä.

Tallentakaa video oppilaitoksen OneDriveen ja lisätkää linkki `04-palautus.md`:hen. Videota ei tallenneta Gitiin. Varmistakaa opettajan ja määrättyjen vertaisarvioijien katseluoikeus. Videon tulee esittää samaa versiota kuin projektipalautus.

Jokainen opiskelija katsoo **kolmen muun parin videon** Moodlessa annetun jaon mukaan ja palauttaa jokaisesta oman arvionsa:

1. Mikä käyttötapaus näytettiin, ja mikä konkreettinen havainto tuki toimivuutta?
2. Mitä testauksesta ja rajoituksista kävi ilmi?
3. Mikä olisi yksi perusteltu kehityskohde?

Vertaisarviointi on henkilökohtainen suoritus, vaikka projekti tehdään parina. Vertaisarvioijat eivät määrää projektin arvosanaa. Palautteesta tunnistetaan kehittämismahdollisuuksia.

## Toimintasuunnitelma projektipisteiden täydentämiseen

Vertaispalautteen saamisen jälkeen voitte tehdä parina enintään yhden sivun toimintasuunnitelman saamanne palautteen perusteella. Suunnitelma voi täydentää enintään 12 projektipistettä projektin 60 pisteen rajan sisällä. Täydennys huomioidaan ennen projektin arvosanan määritystä; pisteytys on kuvattu arviointikriteereissä: palautteen analyysi, toimenpiteiden toteutuskelpoisuus ja onnistumisen tarkistaminen, kustakin 0–4 pistettä. Toteutusta tai uutta videota ei vaadita.

Valitkaa 1–3 olennaista kehityskohdetta. Kirjatkaa kullekin:

- mikä palautteen havainto on lähtökohtana ja miksi se on olennainen;
- mitä konkreettisesti muutettaisiin ja missä järjestyksessä;
- kuka vastaisi muutoksesta ja mikä on realistinen työmäärä;
- miten onnistuminen testattaisiin tai muuten todettaisiin.

Myös palautteen hylkääminen voidaan perustella. Jos ette saa vertaispalautetta, käyttäkää työpajassa toisen parin katselmointia. Tallentakaa suunnitelma tiedostoon `docs/05-toimintasuunnitelma.md` ja palauttakaa sen version tunniste Moodleen erikseen. Alkuperäisen projektin palautusversiota ei muuteta.

## Oma työ ja henkilökohtainen reflektio

Oma työ ja oppiminen arvioidaan dokumentoidun oman osuuden, Git-historian ja katselmointien, projektivideon oman osuuden sekä henkilökohtaisen reflektion perusteella. Kurssilla ei järjestetä erillisiä henkilökohtaisia demoja tai näyttökeskusteluja. Kuvaa konkreettinen työsi, perustele ratkaisut ja selitä niiden tarkistaminen projektidokumenteissa ja videolla.

Palauta lisäksi oma reflektiosi **Moodlen erilliseen tekstikenttään**. Reflektiota ei tallenneta yhteiseen repoon. Sopiva laajuus on noin 200–400 sanaa; sisältö ratkaisee. Käsittele:

- mitä itse teit ja miten se näkyy projektissa;
- yksi perusteltu onnistuminen ja yksi vaikeus tai virhe;
- miten AI auttoi tai johti harhaan ja miten tarkistit tuloksen;
- mitä opit ja mitä tekisit seuraavalla kerralla toisin.

Reflektio perustuu omiin kokemuksiisi. Jos käytät AI:ta kielenhuoltoon tai jäsentelyyn, kerro siitä tekstikentän lopussa. Älä korvaa omaa pohdintaa keksityillä kokemuksilla. Reflektio arvioidaan yhdessä dokumentoidun oman työn ja projektivideon oman osuuden kanssa.

## Aikataulu ja Moodle-palautus

Opetuspäivät ja projektin palautusten vahvistetut määräajat ovat Moodlen kurssijärjestelysivulla ja palautusaktiviteeteissa. Projektin eteneminen on seuraava:

1. Pari ja aihe valitaan, ja yhteinen Git-työskentely aloitetaan. Määrittely aloitetaan määrittelytyöpajassa; valmista projektikuvausta ei edellytetä ennen sitä.
2. Projektikuvaus, alkuprompt ja alustavat jatkuvat AI-ohjeet tallennetaan repoon; repon linkki palautetaan Moodleen.
3. Toteutusta ja määrittelyä tarkennetaan, testaus tehdään ja kummankin oma työ dokumentoidaan.
4. Arvioitava projektiversio dokumentteineen ja video palautetaan.
5. Kumpikin palauttaa henkilökohtaiset vertaisarvioinnit ja reflektion.
6. Mahdollinen toimintasuunnitelma palautetaan itsenäisesti vertaispalautteen jälkeen.

Ensimmäiselle opetuskerralle ei ole esitehtävää. Muiden kertojen esitehtävät ovat pakollisia mutta arvioimattomia, ja ne tehdään Moodlen ohjeiden mukaan. EXAM-tentin aikataulu ilmoitetaan erikseen.

Projektin yhteisessä Moodle-palautuksessa ilmoitetaan tekijät, repon URL, arvioitavan version **täydellinen commit-tunniste** ja videolinkki. Tagia voi käyttää apuna, mutta tallentakaa myös sen osoittama commit-tunniste. Varmistakaa opettajan pääsy yksityiseen repoon ennen määräaikaa. GitHub-tunnus ja käyttöoikeuksien järjestely julkaistaan Moodlessa vahvistettujen ohjeiden mukaan.

Toimintasuunnitelman täydentävä palautus ilmoittaa oman commit-tunnisteensa. Vanhaa tunnistetta ei korvata. Opettajan arviointi ja henkilökohtainen palaute annetaan oppilaitoksen järjestelmässä.

Jos repo, video tai käynnistys ei ole arvioijan käytettävissä, toimittakaa puuttuva pääsy tai korjattu palautustieto opettajan ohjeella. Myöhästyneiden, puuttuvien ja hylättyjen suoritusten täydennysajat sekä puuttuvien henkilökohtaisten palautusten täydennysohjeet julkaistaan erikseen ennen tehtävän avaamista; niistä ei aseteta tässä ohjeessa automaattista pistevähennystä.

## Tarkista ennen palautusta

- README johtaa kaikkiin arvioitaviin osiin ja käynnistysohje on kokeiltu.
- Vaatimusten, testien ja validoinnin yhteys on näkyvissä.
- Alkuprompt, jatkuva AI-työskentely ja käytetyt työkalut on dokumentoitu.
- Molempien tekeminen näkyy, ja kumpikin ymmärtää oman työnsä.
- Repo ja video ovat oikeilla käyttöoikeuksilla ja esittävät samaa palautusversiota.
- Projektidokumentit ovat Markdownia; reflektio palautetaan erikseen Moodleen.
