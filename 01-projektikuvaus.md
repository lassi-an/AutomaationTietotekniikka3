# Projektikuvaus: Frisbeegolf-säävahti

## Käyttäjä, ongelma ja arvolupaus

Projektin tarkoituksena on helpottaa frisbeegolfin harrastajan pelikierroksen suunnittelua. Tuuli, sade ja lämpötila vaikuttavat merkittävästi pelaamiseen, mutta säätietojen ja sopivien ratojen etsiminen eri palveluista voi olla hankalaa.

Frisbeegolf-säävahti kokoaa säätiedot ja lähialueen frisbeegolfradat yhteen sovellukseen. Käyttäjä voi tarkistaa sääolosuhteet, saada arvion pelaamissäästä ja löytää sopivia ratoja.

## Käyttäjäskenaariot

**1. Pelikierroksen suunnittelu**

Käyttäjä valitsee paikkakunnan ja tarkistaa ajankohtaisen sään sekä sovelluksen antaman arvion pelaamisolosuhteista.

**2. Tuuliolosuhteiden tarkistaminen**

Käyttäjä tarkistaa tuulen nopeuden metreinä sekunnissa ja näkee, miten tuuli vaikuttaa sääarvioon.

**3. Frisbeegolfradan etsiminen**

Käyttäjä tarkastelee lähialueen frisbeegolfratoja, niiden etäisyyksiä, väylämääriä ja maksutietoja. Hän voi myös avata radan kartalla tai siirtyä sen verkkosivulle.

## Vaatimukset ja hyväksymiskriteerit

| Tunniste | Vaatimus | Hyväksymiskriteeri | Prioriteetti |
|---|---|---|---|
| V1 | Säätietojen hakeminen | Näyttää lämpötilan, tuulen ja sateen. | Korkea |
| V2 | Paikkakunnan valinta | Käyttäjä voi hakea ja valita paikkakunnan. | Korkea |
| V3 | Sääarvio | Sovellus arvioi sään sopivuutta frisbeegolfiin. | Korkea |
| V4 | Arvion perustelut | Käyttäjä näkee arvion taustalla olevat syyt. | Korkea |
| V5 | Ratojen hakeminen | Näyttää lähialueen ratoja ja niiden tietoja. | Korkea |
| V6 | Maksutiedot | Näyttää ratojen saatavilla olevat maksutiedot. | Korkea |
| V7 | Virhetilanteet | Näyttää ymmärrettävän virheilmoituksen ongelmatilanteissa. | Keskitaso |
| V8 | Verkkokäyttö | Sovellus toimii julkaistun verkkolinkin kautta. | Korkea |
| V9 | Sääennuste | Näyttää valitun paikkakunnan neljän seuraavan tunnin sääennusteen. | Keskitaso |

## Rajaus ja vähimmäiskokonaisuus

Projektin tavoitteena on toteuttaa helppokäyttöinen verkkosovellus, joka yhdistää frisbeegolfin kannalta tärkeimmät säätiedot ja ratatiedot.

**Projektissa toteutetaan:**
- Paikkakuntien haku ja valinta.
- Ajankohtaisten säätietojen hakeminen Open-Meteosta.
- Lämpötilan, tuulen, sateen ja pilvisyyden näyttäminen.
- Neljän seuraavan tunnin sääennuste.
- Sään sopivuuden arviointi ja perustelut.
- Lähialueen frisbeegolfratojen hakeminen.
- Ratojen etäisyyksien, väylämäärien ja maksutietojen näyttäminen.
- Linkit ratojen kartta- ja verkkosivutietoihin.
- Käyttöliittymän toteutus ja sovelluksen julkaiseminen.

## Toteutuksen rakenne

Sovellus toteutetaan Pythonilla ja Streamlitillä. Ohjelma on jaettu kahteen pääasialliseen tiedostoon:

- **app.py:** käyttöliittymä ja tietojen esittäminen.
- **saa.py:** säätietojen ja frisbeegolfratojen hakeminen sekä sääarviointi.

Projektissa käytetään seuraavia teknologioita:
- Python ja Streamlit.
- Open-Meteo-säärajapinta.
- DiscGolfAPI-ratatietojen hakemiseen.
- Git ja GitHub versionhallintaan.
- Visual Studio Code ohjelmointiin.
- Streamlit Community Cloud julkaisemiseen.

## Oletukset, riskit ja mahdollinen data

Säätiedot haetaan Open-Meteo-palvelusta ja ratatiedot DiscGolfAPI-rajapinnasta. Tietojen saatavuus ja ajantasaisuus riippuvat näistä ulkoisista palveluista.

Sääarvio perustuu ohjelmassa määriteltyihin lämpötila-, tuuli- ja sadeolosuhteisiin. Se on suuntaa antava eikä huomioi kaikkien pelaajien henkilökohtaisia mieltymyksiä.

Keskeisiä riskejä ovat rajapintojen toimintahäiriöt, puutteelliset ratatiedot ja internet-yhteyden katkeaminen. Sovellus käsittelee virhetilanteita näyttämällä käyttäjälle virheilmoituksen.

## Merkittävät rajausmuutokset ja niiden syyt

Projektin toteutuksen aikana alkuperäistä suunnitelmaa tarkennettiin. Laajan tulevien päivien sääennusteen sijaan keskityttiin ajankohtaiseen säähän ja neljän seuraavan tunnin ennusteeseen.

Lisäksi sovellukseen lisättiin frisbeegolfratojen haku, etäisyystiedot ja maksutiedot. Näin sovellus auttaa käyttäjää sekä arvioimaan pelaamissään että löytämään sopivan pelipaikan.

Rajaukset tehtiin, jotta tärkeimmät ominaisuudet saatiin toteutettua toimivasti käytettävissä olevan ajan puitteissa.

Projektin lopputuloksena on verkkoselaimessa toimiva Frisbeegolf-säävahti, joka yhdistää sää- ja ratatiedot samaan palveluun.
