# Testaus ja validointi

## Testien suoritusohje

Ohjelmisto testataan suorittamalla se paikallisesti ja kokeilemalla sen toimintoja. Automaattiset testit suoritetaan Pytestillä.

Testien suorittaminen:

```bash
python -m pytest
```

Ohjelman käynnistäminen:

```bash
streamlit run app.py
```

Käyttöliittymässä kokeillaan paikkakunnan valintaa, säätietojen näyttämistä ja sääolosuhteiden arviota.

## Vaatimuksiin sidotut tulokset

| **Vaatimus** | **Testitapa tai syöte** | **Odotettu tulos** | **Havaittu tulos** | **Johtopäätös** |
| ------------ | ----------------------- | ------------------ | ------------------ | --------------- |
| V1: Sään hakeminen | Valitaan paikkakunta käyttöliittymästä. | Ohjelma hakee valitun paikkakunnan säätiedot. | Ei vielä testattu. | Täydennetään testauksen jälkeen. |
| V2: Säätietojen näyttäminen | Tarkistetaan lämpötila, tuulen nopeus ja sateen määrä. | Kaikki kolme säätietoa näkyvät käyttöliittymässä. | Ei vielä testattu. | Täydennetään testauksen jälkeen. |
| V3: Olosuhteiden arviointi | Tarkistetaan erilaisilla säätiedoilla muodostuva arvio. | Ohjelma näyttää arvion: hyvä, kohtalainen tai huono. | Ei vielä testattu. | Täydennetään testauksen jälkeen. |
| V4: Arvion perustelu | Tarkistetaan arvion yhteydessä näkyvä selitys. | Ohjelma kertoo, miksi olosuhteet ovat hyvät tai huonot. | Ei vielä testattu. | Täydennetään testauksen jälkeen. |
| V5: Virhetilanteen käsittely | Kokeillaan tilannetta, jossa säätietojen hakeminen epäonnistuu. | Käyttäjälle näytetään ymmärrettävä virheilmoitus. | Ei vielä testattu. | Täydennetään testauksen jälkeen. |

## Olennainen virhe- tai rajatapaus

Yhtenä tärkeänä virhetilanteena testataan säätietojen hakemisen epäonnistumista. Tämä voi tapahtua esimerkiksi silloin, kun internetyhteys ei toimi tai sääpalvelu ei ole käytettävissä.

Odotettu tulos on, että ohjelma näyttää käyttäjälle ymmärrettävän virheilmoituksen eikä kaadu.

## Validointi käyttäjätarpeeseen nähden

Ohjelmiston tarkoituksena on auttaa frisbeegolfin harrastajaa arvioimaan, millaiset sääolosuhteet ovat pelaamiseen sopivat.

Validoinnissa kokeillaan, pystyykö käyttäjä valitsemaan paikkakunnan, tarkistamaan säätiedot ja saamaan niiden perusteella ymmärrettävän arvion pelaamiseen sopivista olosuhteista.

Kokeilijana toimii projektin tekijä tai mahdollinen toinen opiskelija. Kokeilun jälkeen kirjataan, saavutettiinko käyttäjän tavoite ja oliko ohjelmasta hyötyä.

Kokeilun rajoituksena on, että sääennusteet eivät aina vastaa todellista säätä. Ohjelman antama arvio on suuntaa antava.

## Epäonnistumiset ja tunnetut puutteet

Ei ole vielä päivitän jos muistan
