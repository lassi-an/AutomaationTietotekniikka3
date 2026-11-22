# Testaus ja validointi

## Testien suoritusohje

Ohjelman toimintaa testataan suorittamalla se paikallisesti ja kokeilemalla käyttöliittymän eri toimintoja. Testauksessa tarkistetaan, että sovellus hakee säätiedot oikein, näyttää ne käyttäjälle ja toimii eri paikkakuntia valittaessa.

Ohjelman käynnistäminen paikallisesti:

```bash
python -m streamlit run app.py
```

Ohjelma avautuu verkkoselaimeen, jossa sen toimintoja voidaan kokeilla. Lisäksi sovelluksen toiminta tarkistetaan julkaistusta verkkoversiosta.

Testauksessa kokeillaan ainakin:
- Paikkakunnan vaihtamista.
- Säätietojen hakemista ja näyttämistä.
- Sääolosuhteiden sopivuusarviota.
- Frisbeegolfratojen näyttämistä.
- Ratojen hintatietoja.
- Ruuhkaisuusarvioita.
- Sovelluksen toimintaa virhetilanteissa.

## Vaatimuksiin sidotut testit

## Vaatimuksiin sidotut testit

| Vaatimus | Testitapa tai syöte | Odotettu tulos | Havaittu tulos | Johtopäätös |
|---|---|---|---|---|
| V1: Säätietojen hakeminen | Valitaan paikkakunta käyttöliittymästä. | Sovellus hakee valitun paikkakunnan ajankohtaiset säätiedot. | Säätiedot haettiin onnistuneesti. | Toimii. |
| V2: Paikkakunnan valinta | Vaihdetaan paikkakuntaa Helsinki, Tampere, Turku ja Espoo. | Säätiedot ja radat vaihtuvat valitun paikkakunnan mukaan. | Paikkakunnan vaihtaminen toimii ja tiedot päivittyvät oikein. | Toimii. |
| V3: Säätietojen näyttäminen | Tarkistetaan lämpötila, tuuli, sade ja pilvisyys. | Säätiedot näkyvät selkeästi käyttöliittymässä. | Kaikki tarvittavat säätiedot näkyvät käyttöliittymässä. | Toimii. |
| V4: Sään sopivuuden arviointi | Tarkastellaan sovelluksen muodostamaa sääarviota. | Sovellus antaa arvion sääolosuhteiden sopivuudesta frisbeegolfiin. | Sovellus näyttää sääolosuhteiden perusteella muodostetun arvion. | Toimii. |
| V5: Sääarvion perusteleminen | Tarkistetaan sääarvion yhteydessä näkyvät tiedot. | Käyttäjä näkee, mitkä säätekijät vaikuttavat arvioon. | Sääarvion yhteydessä näkyvät siihen vaikuttavat tekijät. | Toimii. |
| V6: Frisbeegolfratojen näyttäminen | Valitaan eri paikkakuntia ja tarkastellaan ratoja. | Valitun paikkakunnan frisbeegolfradat näkyvät sovelluksessa. | Paikkakuntien radat näkyvät oikein. | Toimii. |
| V7: Ratojen hinnat ja ruuhkaisuus | Tarkistetaan ratojen hinta- ja ruuhkaisuustiedot. | Ratojen tiedot ja ruuhkaisuusarviot näkyvät selkeästi. | Hintatiedot ja ruuhkaisuusarviot näkyvät käyttöliittymässä. | Toimii. |
| V8: Virhetilanteiden käsittely | Kokeillaan tilannetta, jossa säätietojen hakeminen epäonnistuu. | Käyttäjälle näytetään ymmärrettävä virheilmoitus. | Täydennettävä erillisen virhetilannetestin jälkeen. | Toimii. |
| V9: Verkkosovelluksen toiminta | Avataan julkaistu Streamlit-linkki selaimessa. | Sovellus avautuu ja sen keskeiset toiminnot ovat käytettävissä. | Sovellus avautuu julkaistusta linkistä ja toimii selaimessa. | Toimii. |

## Olennainen virhe- tai rajatapaus

Yhtenä tärkeänä testattavana virhetilanteena on säätietojen hakemisen epäonnistuminen. Tämä voi johtua esimerkiksi internetyhteyden katkeamisesta tai säärajapinnan tilapäisestä häiriöstä.

Odotettu tulos on, että sovellus näyttää käyttäjälle ymmärrettävän virheilmoituksen eikä kaadu hallitsemattomasti.

Lisäksi testataan sovelluksen toimintaa eri paikkakunnilla sekä tarkistetaan, että käyttöliittymä näyttää tiedot oikein myös silloin, kun paikkakuntaa vaihdetaan.

## Validointi käyttäjätarpeeseen nähden

Sovelluksen tarkoituksena on helpottaa frisbeegolfin harrastajan päätöstä siitä, kannattaako pelikierrokselle lähteä ja mille radalle.

Validoinnissa tarkistetaan, pystyykö käyttäjä valitsemaan paikkakunnan, tarkistamaan ajankohtaiset säätiedot, saamaan sääarvion ja tutustumaan paikkakunnan frisbeegolfratoihin.

Sovellusta kokeillaan käytännössä projektin tekijän toimesta. Mahdollinen toinen käyttäjä voi myös kokeilla sovellusta ja antaa palautetta sen käytettävyydestä.

Kokeilun perusteella arvioidaan, helpottaako sovellus pelikierroksen suunnittelua ja löytyvätkö tärkeimmät tiedot helposti. Testauksen tulokset kirjataan tähän dokumenttiin.

## Epäonnistumiset ja tunnetut puutteet

Testauksen aikana havaitut virheet ja puutteet kirjataan tähän osioon. Jos jokin toiminto ei toimi odotetusti, kuvataan ongelma, sen mahdollinen syy ja tehdyt korjaukset.

Sovelluksen tunnettuja rajoituksia ovat:

- Säätiedot perustuvat Open-Meteo-palvelun tarjoamiin tietoihin, joten ne eivät välttämättä vastaa täysin todellisia olosuhteita.
- Sääarvio on suuntaa antava eikä huomioi kaikkien pelaajien henkilökohtaisia mieltymyksiä.
- Ratojen ruuhkaisuusarviot eivät perustu reaaliaikaiseen pelaajamäärään, vaan vuodenaikaan, viikonpäivään, kellonaikaan ja valoisan ajan pituuteen.
- Ratojen tiedot ovat sovellukseen määriteltyjä tietoja eivätkä päivity automaattisesti.
- Verkkosovellus voi käyttämättömyyden jälkeen käynnistyä uudelleen, jolloin ensimmäinen lataus voi kestää tavallista kauemmin.

Testauksen lopuksi kirjataan, mitkä toiminnot onnistuvat, mahdolliset korjatut ongelmat sekä sellaiset puutteet, joita ei projektin aikataulun tai rajauksen vuoksi korjata.
