# Testaus ja validointi

## Videolla testatut toiminnat

Videolla testasin muutamia paikkakuntia ja niiden säätietojen hakemista. Sovellus löytää hyvin radat ja säätiedot, mutta se ei esimerkiksi sisällytä kaikkia ratoja paikkakunnilta, kuten Hervannan frisbeegolf rata. Syy voi olla, joko radan uutuus tai muuten puuttuu tietokannasta. Myös itse lisäsin sovellukseen yhden uuden radan Espooseen, joten niitä voi manuaalisesti lisätä. Myöskään ei näy sovelluksessa onko radoilla ruuhkaisaa juuri kyseisenä aikana kun käyttäjä hakee säätietoja. 

## Testien suoritusohje

Sovellusta testataan käynnistämällä se paikallisesti ja kokeilemalla käyttöliittymän toimintoja. Lisäksi testataan julkaistua verkkoversiota.

Ohjelman käynnistäminen:

```powershell
python -m streamlit run app.py
```

Testauksessa tarkistetaan:
- Paikkakuntien haku ja valinta.
- Ajankohtaisten säätietojen näyttäminen.
- Neljän seuraavan tunnin sääennuste.
- Sääarvion ja sen perustelujen toiminta.
- Frisbeegolfratojen hakeminen ja näyttäminen.
- Ratojen etäisyys-, väylä- ja maksutiedot.
- Virhetilanteiden käsittely.
- Julkaistun verkkosovelluksen toiminta.

## Vaatimuksiin sidotut testit

| Vaatimus | Testitapa tai syöte | Odotettu tulos | Havaittu tulos | Johtopäätös |
|---|---|---|---|---|
| V1: Säätietojen hakeminen | Valitaan paikkakunta. | Sovellus hakee ajankohtaiset säätiedot. | Säätiedot näkyvät sovelluksessa. | Toimii. |
| V2: Paikkakunnan valinta | Haetaan Helsinki, Tampere, Turku ja Espoo. | Käyttäjä voi valita eri paikkakuntia. | Paikkakuntien haku ja valinta toimivat. | Toimii. |
| V3: Säätietojen näyttäminen | Tarkistetaan lämpötila, tuuli, sade ja pilvisyys. | Kaikki tiedot näkyvät selkeästi. | Säätiedot näkyvät käyttöliittymässä. | Toimii. |
| V4: Sääarvio | Tarkastellaan muodostettua sääarviota. | Sovellus arvioi pelaamisolosuhteet. | Sääarvio muodostuu sääolosuhteiden perusteella. | Toimii. |
| V5: Arvion perustelut | Tarkistetaan sääarvion perustelut. | Arvion taustalla olevat tekijät näkyvät. | Perustelut näytetään käyttäjälle. | Toimii. |
| V6: Ratojen hakeminen | Valitaan eri paikkakuntia. | Lähialueen frisbeegolfradat näkyvät. | Ratoja haetaan valitun paikkakunnan perusteella. | Toimii. |
| V7: Maksutiedot | Tarkistetaan ratojen maksutiedot. | Maksutiedot näkyvät suomeksi. | Maksutiedot näytetään ratojen yhteydessä. | Toimii. |
| V8: Virhetilanteet | Kokeillaan epäonnistunutta säähakua. | Käyttäjälle näytetään ymmärrettävä virheilmoitus. | Erillinen virhetilannetestin tulos kirjataan testauksen jälkeen. | Testattava. |
| V9: Verkkosovelluksen toiminta | Avataan julkaistu Streamlit-linkki. | Sovellus toimii selaimessa. | Sovellus avautuu julkaistusta linkistä. | Toimii. |
| V10: Tuntiennuste | Tarkistetaan neljän seuraavan tunnin ennuste. | Ennuste näyttää kellonajan, lämpötilan, tuulen ja sateen. | Ennuste näkyy käyttöliittymässä. | Toimii. |

## Olennainen virhe- tai rajatapaus

Yksi tärkeä testattava virhetilanne on säätietojen hakemisen epäonnistuminen. Syynä voi olla esimerkiksi internetyhteyden katkeaminen tai säärajapinnan häiriö.

Odotettu tulos on, että sovellus näyttää käyttäjälle ymmärrettävän virheilmoituksen eikä kaadu hallitsemattomasti.

Lisäksi testataan paikkakunnan vaihtamista ja sitä, että uudet sää- ja ratatiedot vastaavat valittua paikkakuntaa.

## Validointi käyttäjätarpeeseen nähden

Sovelluksen tavoitteena on helpottaa frisbeegolfkierroksen suunnittelua. Validoinnissa tarkistetaan, pystyykö käyttäjä hakemaan paikkakunnan, tarkistamaan sään, saamaan arvion pelaamisolosuhteista ja löytämään lähialueen ratoja.

Sovellusta kokeillaan käytännössä projektin tekijän toimesta. Käytettävyyttä voidaan lisäksi arvioida toisen käyttäjän palautteen avulla.

Validoinnin perusteella arvioidaan, löytyvätkö tärkeimmät tiedot helposti ja helpottaako sovellus pelikierroksen suunnittelua.

## Epäonnistumiset ja tunnetut puutteet

Sovelluksen tunnettuja rajoituksia ovat:

- Säätiedot riippuvat Open-Meteo-palvelun saatavuudesta ja tarkkuudesta.
- Sääarvio on suuntaa antava eikä huomioi kaikkien pelaajien henkilökohtaisia mieltymyksiä.
- Ratojen tiedot riippuvat DiscGolfAPI-palvelun tietokannasta eivätkä välttämättä sisällä kaikkia Suomen ratoja. Tämä on testattu ja kaikkia ratoja ei löydy varsikaan, jos ne ovat uudempia.
- Maksutiedot voivat olla puutteellisia tai muuttua ajan myötä.
- Sovellus näyttää enintään kymmenen lähintä hakutuloksista löytyvää rataa.
- Verkkosovellus voi käyttämättömyyden jälkeen käynnistyä uudelleen, jolloin ensimmäinen lataus voi kestää tavallista kauemmin.

Testauksen jälkeen kirjataan mahdolliset havaitut virheet, tehdyt korjaukset ja projektin aikataulun vuoksi ratkaisematta jääneet puutteet.
