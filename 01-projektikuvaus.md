# Projektikuvaus: Frisbeegolf-säävahti

## Käyttäjä, ongelma ja arvolupaus

Projektin tarkoituksena on helpottaa frisbeegolfin harrastajan päätöstä siitä, kannattaako sääolosuhteiden puolesta lähteä pelaamaan. Frisbeegolfissa sää vaikuttaa paljon pelikokemukseen. Esimerkiksi voimakas tuuli voi vaikeuttaa kiekon hallintaa, sade tekee pelaamisesta epämukavampaa ja kylmä sää voi vähentää pelimukavuutta.

Säätietojen tarkistaminen eri palveluista ja niiden arvioiminen itse voi olla turhan vaivalloista. Tämän vuoksi toteutetaan Frisbeegolf-säävahti, joka kokoaa tärkeimmät säätiedot yhteen paikkaan ja antaa niiden perusteella arvion pelaamiseen sopivista olosuhteista.

Sovelluksen avulla käyttäjä voi tarkistaa valitun paikkakunnan ajankohtaisen sään, arvioida sen sopivuutta frisbeegolfiin sekä tutustua paikkakunnan frisbeegolfratoihin ja niiden arvioituun ruuhkaisuuteen.

## Käyttäjäskenaariot

**Skenaario 1: Pelaaja suunnittelee pelikierrosta**

Frisbeegolfin harrastaja suunnittelee lähtevänsä pelaamaan. Hän avaa Frisbeegolf-säävahdin, valitsee paikkakunnan ja tarkistaa ajankohtaiset säätiedot. Sovellus antaa arvion siitä, ovatko olosuhteet hyvät frisbeegolfiin.

**Skenaario 2: Pelaaja tarkistaa tuuliolosuhteet**

Pelaaja haluaa tietää, kuinka voimakas tuuli on ennen kierrokselle lähtemistä. Sovelluksesta hän näkee tuulen nopeuden ja saa sääarvion, jossa tuulen vaikutus pelaamiseen on huomioitu.

**Skenaario 3: Pelaaja etsii sopivaa frisbeegolfrataa**

Pelaaja valitsee haluamansa paikkakunnan ja tarkastelee sovelluksessa listattuja frisbeegolfratoja. Hän näkee ratojen nimet, mahdolliset maksut sekä arvioidun ruuhkaisuuden. Näiden tietojen avulla hän voi valita itselleen sopivan radan.

## Vaatimukset ja hyväksymiskriteerit

| Tunniste | Vaatimus | Hyväksymiskriteeri | Prioriteetti |
|---|---|---|---|
| V1 | Sovellus hakee ajankohtaiset säätiedot säärajapinnasta. | Sovellus näyttää valitun paikkakunnan lämpötilan, tuulen nopeuden ja sateen tiedot. | Korkea |
| V2 | Käyttäjä voi valita paikkakunnan. | Käyttäjä voi valita sovelluksesta eri paikkakuntia ja saa niitä vastaavat säätiedot. | Korkea |
| V3 | Sovellus arvioi sään sopivuutta frisbeegolfiin. | Sovellus antaa sääolosuhteiden perusteella arvion pelaamisen sopivuudesta. | Korkea |
| V4 | Sovellus näyttää sääarvion perustelut. | Käyttäjä näkee säätekijät, jotka vaikuttavat pelaamisen sopivuuteen. | Korkea |
| V5 | Sovellus näyttää paikkakunnan frisbeegolfratoja. | Käyttäjä näkee valitun paikkakunnan ratojen nimet ja mahdolliset maksutiedot. | Korkea |
| V6 | Sovellus arvioi ratojen ruuhkaisuutta. | Radoille näytetään arvio ruuhkaisuudesta eri ajankohtien perusteella. | Keskitaso |
| V7 | Sovellus käsittelee virhetilanteita. | Jos säätietojen hakeminen epäonnistuu, käyttäjälle näytetään ymmärrettävä virheilmoitus. | Keskitaso |
| V8 | Sovellus toimii verkkoselaimessa. | Käyttäjä pystyy avaamaan sovelluksen julkaistusta linkistä ilman Pythonin tai ohjelmointiympäristön asentamista. | Korkea |

## Rajaus ja vähimmäiskokonaisuus

Projektin tavoitteena on toteuttaa yksinkertainen ja toimiva sovellus, joka kokoaa frisbeegolfiin liittyvät sää- ja ratatiedot yhteen paikkaan. Sovelluksen tulee olla helppokäyttöinen ja antaa käyttäjälle riittävästi tietoa pelikierroksen suunnittelua varten.

**Projektissa toteutetaan:**

- Ajankohtaisten säätietojen hakeminen Open-Meteo-säärajapinnasta.
- Paikkakunnan valinta.
- Lämpötilan, tuulen nopeuden, sateen ja pilvisyyden näyttäminen.
- Sään sopivuuden arviointi frisbeegolfiin.
- Sääarvion perusteleminen.
- Paikkakunnan frisbeegolfratojen esittäminen.
- Ratojen mahdollisten maksutietojen näyttäminen.
- Ratojen arvioidun ruuhkaisuuden esittäminen.
- Sovelluksen käyttöliittymän toteuttaminen Streamlitillä.
- Sovelluksen julkaiseminen verkossa.

**Projektin ulkopuolelle jätetään:**

- Käyttäjätilit ja kirjautuminen.
- Mobiilisovelluksen erillinen toteutus.
- Puhelimeen lähetettävät ilmoitukset.
- Frisbeegolfratojen karttapalvelu.
- Käyttäjien reaaliaikaiset ruuhkatiedot.
- Koneoppimiseen perustuva sääarviointi.
- Laaja sääennusteiden tarkastelu useille tuleville päiville.

## Toteutuksen rakenne

Sovellus toteutetaan Python-ohjelmointikielellä. Käyttöliittymä rakennetaan Streamlitillä, jonka avulla ohjelma voidaan myös julkaista verkkosovelluksena.

Sovelluksen keskeiset teknologiat:

- **Python:** sovelluksen ohjelmointikieli.
- **Streamlit:** käyttöliittymän toteutus.
- **Open-Meteo API:** ajankohtaisten säätietojen hakeminen.
- **Git ja GitHub:** projektin versionhallinta ja tiedostojen tallentaminen.
- **Visual Studio Code:** ohjelmointiympäristö.
- **Streamlit Community Cloud:** sovelluksen julkaiseminen verkossa.

Ohjelma on jaettu eri tiedostoihin, jotta sen rakenne pysyy selkeänä. Säätietojen hakeminen tapahtuu erillisessä `saa.py`-tiedostossa ja käyttöliittymän sekä tietojen esittämisen toiminnallisuus on `app.py`-tiedostossa.

## Oletukset, riskit ja mahdollinen data

Sovellus hakee ajankohtaiset säätiedot Open-Meteo-palvelusta. Säätiedot perustuvat sääpalvelun tarjoamaan dataan, joten ne eivät välttämättä vastaa täysin paikan päällä vallitsevia olosuhteita.

Sään sopivuuden arviointi perustuu ohjelmassa määriteltyihin sääolosuhteisiin. Arvio on suuntaa antava, eikä se huomioi kaikkien pelaajien henkilökohtaisia mieltymyksiä tai esimerkiksi yksittäisen frisbeegolfradan maaston vaikutuksia.

Ratojen ruuhkaisuusarviot perustuvat vuodenaikaan, viikonpäivään, kellonaikaan ja valoisan ajan pituuteen. Kyseessä ei ole reaaliaikainen tieto radalla olevista pelaajista, vaan ohjelman tekemä arvio siitä, milloin radalla voisi olla enemmän tai vähemmän pelaajia.

Projektin mahdollisia riskejä:

- Säärajapinta ei ole käytettävissä.
- Internet-yhteys ei toimi.
- Säätiedot eivät vastaa täysin todellisia olosuhteita.
- Ruuhkaisuusarvio ei vastaa todellista radan tilannetta.
- Sovelluksen verkkopalvelu voi olla hetkellisesti poissa käytöstä tai käynnistyä uudelleen käyttämättömyyden jälkeen.

## Merkittävät rajausmuutokset ja niiden syyt

Projektin alkuperäinen suunnitelma sisälsi myös tulevien päivien sääennusteen tarkastelun. Toteutuksen aikana projektia rajattiin niin, että sovelluksen tärkeimmäksi toiminnoksi muodostui ajankohtaisten säätietojen tarkistaminen ja niiden perusteella tehtävä sääarvio.

Lisäksi sovellukseen lisättiin paikkakuntakohtaiset frisbeegolfradat ja niiden arvioitu ruuhkaisuus. Tämä teki sovelluksesta käytännöllisemmän frisbeegolfia harrastavalle käyttäjälle, sillä sääolosuhteiden lisäksi käyttäjä voi tarkastella myös mahdollisia pelipaikkoja.

Rajauksia tehtiin, jotta projektin kokonaisuus pysyisi toteutuskelpoisena käytettävissä olevan ajan puitteissa ja jotta tärkeimmät toiminnot saataisiin toteutettua ja testattua kunnolla.

Projektin lopullisena tavoitteena on toimiva ja helposti käytettävä Frisbeegolf-säävahti, joka auttaa käyttäjää suunnittelemaan pelikierrosta ja valitsemaan sopivan pelipaikan.

