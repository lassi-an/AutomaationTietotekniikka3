# Projektin arviointikriteerit

Tämä dokumentti täydentää [projektiohjetta](projektiohje.md). Arvosanojen muunnosrajat ja painotetun keskiarvon laskenta on kuvattu [arvosanan laskennassa](arvosanan-laskenta.md).

## Arvioinnin perusta

Arviointi kohdistuu tarpeen, vaatimusten, toteutuksen, testauksen ja validoinnin muodostamaan kokonaisuuteen. Aiheenvalinta on vapaa. Harrasteaihe ja teollinen aihe arvioidaan samoilla perusteilla. Teknologia, maksullinen työkalu, agenttiympäristö, AI-tuotoksen määrä tai näyttävä video eivät itsessään tuo lisäpisteitä.

Sovittu malli: projekti, oma työ ja oppiminen sekä EXAM-tentti saavat kukin arvosanan 0–5. Painot ovat 60 %, 15 % ja 25 %. Näiden arvosanoista lasketaan painotettu keskiarvo; eri osasuoritusten raakapisteitä ei summata kurssipisteiksi. Tämän dokumentin 60 ja 15 pistettä ovat projektin ja oman työn sisäiset arviointiasteikot, eivät arvosanan laskentaan suoraan lisättäviä kurssipisteitä.

[Arvosanan laskenta](arvosanan-laskenta.md) sisältää hyväksytyt muunnosrajat, hyväksymisehdot ja pyöristyssäännön. Jokainen osasuoritus hyväksytään erikseen.

## 1. Parin yhteinen projekti, 0–60 pistettä

Arvioidaan viisi osa-aluetta. Jokaisesta annetaan 0, 3, 6, 9 tai 12 pistettä seuraavien kuvausten mukaan. Valitaan korkein taso, jonka olennainen näyttö kokonaisuutena täyttyy; lyhyt perustelu kertoo mahdolliset puutteet. Sama näyttö ei saa pisteitä kahteen kertaan: esimerkiksi testiraportin sisältö arvioidaan D:ssä ja sen löydettävyys E:ssä.

| Osa-alue ja näyttö | 6 p: perustaso | 9 p: hyvä taso | 12 p: erinomainen taso |
|---|---|---|---|
| **A. Tarve, määrittely ja rajaus** — `01-projektikuvaus.md` ja toteutus | Käyttäjä, ongelma ja hyöty ovat ymmärrettäviä. Keskeiset vaatimukset ovat testattavia ja rajaus toteutuskelpoinen. | Käyttäjäskenaariot, prioriteetit ja hyväksymiskriteerit muodostavat johdonmukaisen kokonaisuuden. Merkittävät valinnat ja muutokset on perusteltu. | Vaihtoehtoja ja olennaisia oletuksia on arvioitu perustellusti. Rajaus, riskit ja kriteerit tukevat vakuuttavasti käyttäjän tavoitetta. |
| **B. AI:n tavoitteellinen ohjaus ja tarkistaminen** — `02-ai-tyoskentely.md`, `AGENTS.md` tai vastaava prosessi sekä konkreettinen esimerkki | Alkuprompt liittyy määrittelyyn. Työkalut ja jatkuva prosessi on kuvattu. Yksi todellinen esimerkki osoittaa ihmisen tekemän tarkistuksen ja ratkaisun perustelun. | AI-tehtävät on rajattu tarkoituksenmukaisesti ja tuotoksia katselmoidaan ja testataan. Esimerkki osoittaa, miten havainto vaikutti hyväksymiseen, korjaukseen tai hylkäämiseen. | Prosessin toimivuutta ja rajoituksia on analysoitu. Työskentelyä on mukautettu perustellusti havaintojen mukaan, ja vaikutus ratkaisuun on näkyvä. |
| **C. Toteutuksen toimivuus ja rakenne** — käynnistettävä palautusversio ja sen keskeinen käyttötapaus | Keskeinen käyttötapaus toimii. Toteutus on ymmärrettävästi jäsennetty, ja vähintään yksi olennainen virhe- tai rajatapaus on hallittu. Rajoitukset on tunnistettu. | Olennaiset vaatimukset toteutuvat johdonmukaisesti. Rakenne tukee ylläpitoa, ja keskeiset virhetilanteet käsitellään tarkoituksenmukaisesti. | Toteutus on valitussa rajauksessa luotettava ja hyvin perusteltu. Rakenne ja virheiden käsittely osoittavat harkittuja ratkaisuja; tunnetut rajat on osoitettu näytöin. |
| **D. Testaus ja validointi** — `03-testaus-ja-validointi.md`, testit ja tulokset | Tärkeimmät vaatimukset on testattu ja tulokset kirjattu. Mukana on olennainen virhe- tai rajatapaus. Käyttäjätarpeen täyttymistä arvioidaan konkreettisen kokeilun perusteella. | Vaatimusten ja testien yhteys sekä odotetut ja havaitut tulokset ovat toistettavia. Epäonnistumiset ja kattavuuden rajat käsitellään. Validointi perustelee saadun hyödyn ja puutteet. | Testauksen kattavuuden valinnat ja jäännösriskit on analysoitu. Tekniset näytöt ja käyttäjätarpeen validointi tukevat perusteltuja johtopäätöksiä ja kehitystoimia. |
| **E. Git-yhteistyö ja toimitettavuus** — README, sovittu dokumenttirakenne, historia, lähteet ja video | Repo on käytetty työssä, molempien osuus on tunnistettavissa ja käynnistys onnistuu ohjeella. Markdown-dokumentit löytyvät sovitusti ja vastaavat pääosin toteutusta. Video näyttää palautusversion keskeisen käytön. | Muutokset ja työnjako ovat ymmärrettäviä, katselmoinnista on näyttö ja toimitus on toistettava. Dokumentit, versio, video ja tarvittavat aineistot muodostavat yhtenäisen kokonaisuuden. | Repo mahdollistaa vaivattoman perehtymisen, kokeilun ja jatkokehityksen. Versiohistoria ja katselmointi osoittavat hallittua yhteistyötä; dokumentaatio on tiivistä, täsmällistä ja luotettavaa. |

**3 pistettä:** osa-alueesta on tunnistettava yritys ja osittaista näyttöä, mutta 6 pisteen perustasosta puuttuu olennainen osa. Esimerkiksi vaatimukset ovat enimmäkseen tulkinnanvaraisia, AI:n tarkistus jää väitteeksi tai testituloksia ei pystytä toistamaan. Opettaja nimeää puuttuvan näytön.

**0 pistettä:** arvioitavaa näyttöä ei ole tai se ei osoita osa-alueen tavoitetta. Pääsyongelma selvitetään ennen kuin sitä tulkitaan osaamisen puuttumiseksi.

Yhteisen projektin hyväksymisraja: **vähintään 30/60 pistettä ja jokaisessa osa-alueessa vähintään 6 pistettä**. Ehto tekee näkyväksi koko tuotantoketjun vähimmäistason. Puuttuvaa toimivaa ydinkäyttötapausta tai olennaista osaamisnäyttöä ei voi korvata muiden osa-alueiden korkeilla pisteillä.

## 2. Toimintasuunnitelman täydennys, 0–12 pistettä

Hyvä alkuperäinen työ voi saada 60/60 pistettä ilman täydennyssuunnitelmaa. Toimintasuunnitelma on vapaaehtoinen mahdollisuus osoittaa palautteen analysointia ja jatkokehityksen suunnittelua. Se ei edellytä muutosten toteuttamista.

Hyväksytty toimintasuunnitelman arviointi: kolme kriteeriä, kustakin 0–4 p, yhteensä enintään 12 p:

| Kriteeri | 0 p | 2 p: perustaso | 4 p: erinomainen taso |
|---|---|---|---|
| **Palautteen analyysi ja priorisointi** | Palautetta ei käsitellä tai sitä vain kopioidaan. | Olennainen havainto tunnistetaan ja kehityskohde valitaan perustellen. | Havaintojen merkitys suhteessa tavoitteisiin analysoidaan ja kehityskohteet priorisoidaan perustellusti. Myös hylättävä palaute perustellaan tarvittaessa. |
| **Toimenpiteiden toteutuskelpoisuus** | Toimenpide puuttuu tai jää yleiseksi toiveeksi. | Muutos on konkreettinen ja rajattu. | Toimenpiteet, etenemisjärjestys, vastuut ja realistinen työmäärä muodostavat toteuttamiskelpoisen suunnitelman. |
| **Onnistumisen tarkistaminen** | Tarkistustapaa ei kuvata. | Muutoksen onnistumiselle on ymmärrettävä kriteeri. | Kriteeri, testitapa tai muu näyttö ja tavoiteltu käyttäjähyöty liittyvät selkeästi tunnistettuun puutteeseen. |

Yksi piste tarkoittaa osittaista perustason näyttöä. Kolme pistettä tarkoittaa perustason ylittävää, mutta erinomaisesta tasosta vielä puutteellista näyttöä. Arvioidaan suunnitelman laatua, ei saadun palautteen määrää tai myönteisyyttä.

Laskutapa: **parin lopulliset projektipisteet = min(60, alkuperäiset projektipisteet + toimintasuunnitelman pisteet)**. Esimerkiksi 42 + 12 = 54 p ja 57 + 12 = 60 p. Suunnitelma ei alenna alkuperäisiä pisteitä. Sama parin yhteinen pistemäärä tulee kummallekin, kun molemmat osallistuvat suunnitelmaan; osallistuminen kirjataan suunnitelmaan. Jos vain toinen laatii suunnitelman, täydennys arvioidaan hänen hyväkseen ja kirjataan Moodlessa henkilökohtaisesti yhteisen projektiosuuden täydennyksenä.

Suunnitelma on erillinen suunnittelunäyttö: se **ei muuta alkuperäisen toteutuksen tai testauksen osa-aluetasoja eikä poista niiden vähimmäisrajoja**. Jos jokin osa-alue jää alle 6 pisteen, tarvitaan sen puuttuvan näytön täydentäminen erikseen. Toimintasuunnitelma ei korvaa oman työn ja oppimisen vähimmäisnäyttöjä, puuttuvia pakollisia palautuksia tai tentin hyväksyntää. Myöhästyneen tai hylätyn suorituksen täydentäminen on eri menettely, jonka aikataulu vahvistetaan erikseen.

## 3. Oma työ ja oppiminen projektissa, 0–15 pistettä

Kumpikin opiskelija saa omat pisteensä. Näyttönä käytetään dokumentoitua omaa osuutta, Git-historiaa ja katselmointeja, projektivideon omaa osuutta sekä Moodlen henkilökohtaista reflektiota. Erillisiä henkilökohtaisia demoja tai näyttökeskusteluja ei järjestetä. Pelkkä parin valmis tuotos tai commitien määrä ei osoita yksilön osaamista.

| Osa-alue | 3 p: perustaso | 4 p: hyvä taso | 5 p: erinomainen taso |
|---|---|---|---|
| **Oma työ ja ratkaisujen ymmärtäminen** | Osoittaa oman konkreettisen työnsä ja selittää ratkaisun sekä sen tarkistamisen. | Perustelee omat valintansa suhteessa vaatimuksiin ja tunnistaa ratkaisun rajoitukset. | Vertaa perustellusti vaihtoehtoja ja analysoi ratkaisunsa vaikutusta kokonaisuuteen. |
| **Yhteistyö ja henkilökohtainen vastuu** | Osallistuu projektiin ja toisen työn tarkistamiseen; oma osuus ja työnjako ovat tunnistettavia. | Tukee parin etenemistä ja osoittaa, miten oma katselmointi, testaus tai ongelmanratkaisu paransi yhteistä työtä. | Arvioi ja kehittää työnjakoa sekä yhteisiä käytäntöjä perustellusti konkreettisten havaintojen avulla. |
| **Reflektio ja opitun arviointi** | Kuvaa omin havainnoin onnistumisen, vaikeuden, AI:n roolin ja opitun. | Yhdistää havainnot konkreettisiin tilanteisiin ja perustelee, mitä tekisi seuraavaksi toisin. | Analysoi osaamisensa kehittymistä, tarkistusvastuuta ja toimintatapojen vaikutuksia sekä johtaa niistä toteuttamiskelpoisia muutoksia. |

Kussakin osa-alueessa **0 p** tarkoittaa puuttuvaa näyttöä, **1 p** hyvin niukkaa tai yleistä kuvausta ja **2 p** osittaista näyttöä, josta puuttuu perustason olennainen osa. Arviointi perustuu palautettuun aineistoon. Epäselvä tai puuttuva näyttö täydennetään tarvittavalla dokumentilla, videon oman osuuden tarkennuksella tai reflektiolla opettajan palautusohjeen mukaan; erillistä näyttökeskustelua ei edellytetä.

Oman työn ja oppimisen hyväksymisraja: **jokaisesta osa-alueesta vähintään 3 pistettä**, yhteensä vähintään 9/15 p. Vahva reflektio ei yksin korvaa puuttuvaa omaa työtä tai sen ymmärtämistä.

## 4. Muut suoritukset ja tasapuolisuus

- Kolmen videon henkilökohtainen vertaisarviointi ja oma reflektio kuuluvat projektin suoritukseen. Vertaisarviointien tekeminen tarkistetaan; niistä ei anneta erillisiä pisteitä. Reflektion laatu kuuluu henkilökohtaiseen arviointiin, ei parin yhteisiin pisteisiin.
- Videon tehtävä on näyttää toiminta ja tekijöiden osuus. Äänen, kuvan tai esiintymisen tuotannollista laatua ei arvioida, kun sisältö on ymmärrettävä. Tarvittava vaihtoehtoinen esitystapa sovitaan opettajan kanssa samojen osaamistavoitteiden perusteella.
- Manuaalinen ja automatisoitu testaus voivat osoittaa saman tavoitteen. Ulkopuolista asiakasta, oikeaa teollisuusdataa tai pilvipalvelun käyttöä ei vaadita korkeisiinkaan projektipisteisiin.
- Maksullinen tai agenttinen AI-ympäristö ei ole etu pisteytyksessä. Arvioidaan ohjauksen, tarkistamisen ja perustelujen laatua.
- Moodle-esitehtävät ovat erillistä palautetta antavaa harjoittelua. Ensimmäiselle kerralle ei ole esitehtävää. Ne ovat pakollisia mutta arvioimattomia: niiden tekemistä seurataan, mutta niistä ei anneta pisteitä tai arvosanaa. Täydentämistapa ilmoitetaan tehtävän yhteydessä.
- Puuttuvat pakolliset palautukset ja käyttöoikeusongelmat ilmoitetaan yksilöitynä. Korjausaika sekä myöhästymis- ja uusintakäytäntö julkaistaan ennen tehtävän avaamista. Näistä ei oleteta automaattisia pistevähennyksiä tässä ohjeessa.

## Vertaisarvioinnin rooli

Vertaisarvioijat antavat havaintoihin perustuvaa palautetta videosta; heidän antamiaan arvioita ei keskiarvoisteta projektin arvosanaksi. Projektin peruspisteet antaa opettaja hyväksytyn arviointitaulukon ja alkuperäisen palautusversion näytön perusteella. Vertaispalautteen väite ei yksin osoita vaatimuksen täyttymistä tai puuttumista.

Jokaisen tekemä vertaisarviointi on projektiohjeen mukainen henkilökohtainen suoritus. Nykyisessä mallissa sen tekeminen tarkistetaan ilman erillisiä arviointipisteitä. Jokainen arvioi kolme muuta projektivideota; määrä on hyväksytty.

Saadun palautteen vaikutus pisteisiin kulkee toimintasuunnitelman kautta: opettaja arvioi palautteen käsittelyn ja jatkokehityksen suunnittelun, enintään 12 pistettä projektin 60 pisteen rajan sisällä. Myös kriittisen palautteen perusteltu hylkääminen voi osoittaa osaamista. Puuttuvan palautteen tilalla tarjotaan vastaava katselmointi, jotta täydennysmahdollisuus ei riipu toisten palautuksista.
