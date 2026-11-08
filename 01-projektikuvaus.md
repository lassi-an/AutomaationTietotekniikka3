# Projektikuvaus: Frisbeegolf-säävahti

## Käyttäjä, ongelma ja arvolupaus

Projektin käyttäjänä on frisbeegolfin harrastaja, joka haluaa tietää, ovatko sääolosuhteet sopivat frisbeegolfin pelaamiseen.

Frisbeegolfissa sää vaikuttaa merkittävästi pelikokemukseen. Esimerkiksi kova tuuli voi vaikeuttaa kiekon hallintaa, sade voi tehdä pelaamisesta epämukavaa ja kylmä sää voi heikentää pelikokemusta.

Tällä hetkellä pelaajan täytyy usein tarkistaa sää eri palveluista ja arvioida itse, kannattaako radalle lähteä.

**Frisbeegolf-säävahdin tarkoituksena on helpottaa päätöksentekoa.** Sovellus näyttää ajankohtaiset säätiedot ja antaa niiden perusteella arvion siitä, ovatko olosuhteet hyvät, kohtalaiset vai huonot frisbeegolfin pelaamiseen.

## Käyttäjäskenaariot

**Skenaario 1: Pelaaja suunnittelee pelikierrosta**

Frisbeegolfin harrastaja haluaa lähteä pelaamaan iltapäivällä. Hän avaa sovelluksen ja tarkistaa lämpötilan, tuulen nopeuden ja sateen mahdollisuuden. Sovellus kertoo, että sääolosuhteet ovat hyvät pelaamiseen.

**Skenaario 2: Pelaaja tarkistaa tuuliolosuhteet**

Pelaaja haluaa tietää, onko tuuli liian voimakas frisbeegolfiin. Hän tarkistaa sovelluksesta tuulen nopeuden ja saa arvion siitä, kuinka paljon tuuli voi vaikeuttaa pelaamista.

**Skenaario 3: Pelaaja vertailee tulevia päiviä**

Pelaaja suunnittelee viikonlopun pelikierrosta. Hän tarkistaa tulevien päivien sääennusteen ja vertailee, minä päivänä olosuhteet olisivat parhaat frisbeegolfiin.

## Vaatimukset ja hyväksymiskriteerit

| Tunniste | Vaatimus | Hyväksymiskriteeri | Prioriteetti |
|---|---|---|---|
| V1 | Sovellus hakee säätiedot säärajapinnasta. | Sovellus näyttää lämpötilan, tuulen nopeuden ja sateen tiedot. | Korkea |
| V2 | Sovellus näyttää säätiedot käyttäjälle selkeästi. | Käyttäjä näkee säätiedot sovelluksen käyttöliittymästä. | Korkea |
| V3 | Sovellus arvioi sään sopivuutta frisbeegolfiin. | Sovellus antaa arvion: hyvä, kohtalainen tai huono. | Korkea |
| V4 | Sovellus perustelee sääarvion. | Käyttäjä näkee, mitkä säätekijät vaikuttivat arvioon. | Korkea |
| V5 | Sovellus näyttää sääennusteen tuleville tunneille tai päiville. | Käyttäjä pystyy tarkastelemaan tulevia sääolosuhteita. | Keskitaso |
| V6 | Sovellus käsittelee virhetilanteet. | Jos säätietoja ei saada haettua, käyttäjälle näytetään ymmärrettävä virheilmoitus. | Keskitaso |

## Rajaus ja vähimmäiskokonaisuus

Projektin vähimmäistavoitteena on toteuttaa toimiva sovellus, jolla käyttäjä voi tarkistaa sääolosuhteet ja saada arvion niiden sopivuudesta frisbeegolfiin.

**Toteutetaan:**
- Säätietojen hakeminen Open-Meteo-säärajapinnasta.
- Lämpötilan, tuulen nopeuden ja sateen näyttäminen.
- Sään sopivuuden arviointi frisbeegolfiin.
- Arvion perusteleminen sääolosuhteiden avulla.
- Yksinkertainen sääennusteen visualisointi.
- Virhetilanteiden käsittely.

**Jätetään projektin ulkopuolelle:**
- Käyttäjätilit ja kirjautuminen.
- Mobiilisovellus.
- Ilmoitukset puhelimeen.
- Frisbeegolfratojen karttapalvelu.
- Maksulliset sääpalvelut.
- Koneoppimiseen perustuva sääarviointi.

## Toteutuksen rakenne

Sovellus toteutetaan Python-ohjelmointikielellä.

Suunnitellut teknologiat:
- **Python:** sovelluksen ohjelmointikieli.
- **Streamlit:** käyttöliittymän toteutus.
- **Open-Meteo API:** säätietojen hakeminen.
- **Plotly:** sääennusteen visualisointi.
- **Pytest:** ohjelman toimintojen testaaminen.
- **Git ja GitHub:** versionhallinta ja projektin dokumentointi.

Ohjelma jaetaan selkeisiin osiin:
1. Säätietojen hakeminen säärajapinnasta.
2. Säätietojen käsittely.
3. Frisbeegolfiin sopivuuden arviointi.
4. Käyttöliittymä ja säätietojen esittäminen.
5. Ohjelman testaaminen.

## Oletukset, riskit ja mahdollinen data

Säätiedot haetaan Open-Meteo-palvelun rajapinnasta. Palvelusta saadaan esimerkiksi lämpötila-, tuuli- ja sadetietoja.

Sovelluksen sääarvio perustuu ennalta määriteltyihin säärajoihin. Esimerkiksi voimakas tuuli voi laskea arviota, koska se vaikeuttaa kiekon lentoradan hallintaa.

Projektin mahdollisia riskejä:
- Säärajapinta ei ole käytettävissä.
- Internet-yhteys ei toimi.
- Sääennuste ei vastaa täysin todellisia olosuhteita.
- Sään sopivuuden arviointi on suuntaa antava eikä huomioi kaikkia pelaajan henkilökohtaisia mieltymyksiä.

## Merkittävät rajausmuutokset ja niiden syyt

Projektin alkuperäistä ideaa voidaan tarkentaa toteutuksen aikana. Mahdolliset muutokset ja niiden syyt kirjataan tähän osioon.

Tällä hetkellä projektin tavoitteena on toteuttaa yksinkertainen ja toimiva frisbeegolfiin tarkoitettu säävahti, joka auttaa käyttäjää arvioimaan, kannattaako sääolosuhteiden puolesta lähteä pelaamaan.
