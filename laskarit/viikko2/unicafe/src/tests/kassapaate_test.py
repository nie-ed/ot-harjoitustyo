import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)


    def test_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassapaatteen_edulliset_maara_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassapaatteen_maukkaat_maara_oikea(self):
        self.assertEqual(self.kassa.maukkaat, 0)



    def test_edullinen_lounas_vaihtoraha_kun_kateista_riittavasti(self):
        maksu = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(maksu, 10)

    def test_edullinen_lounas_kassaraha_kun_kateista_riittavasti(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)    

    def test_edullinen_lounas_maara_kun_kateista_riittavasti(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)    


    def test_edullinen_lounas_vaihtoraha_kun_kateista_ei_riittavasti(self):
        maksu = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(maksu, 100)

    def test_edullinen_lounas_kassaraha_kun_kateista_ei_riittavasti(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)    

    def test_edullinen_lounas_maara_kun_kateista_ei_riittavasti(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset, 0)     




    def test_maukas_lounas_vaihtoraha_kun_kateista_riittavasti(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(maksu, 50)

    def test_maukas_lounas_kassaraha_kun_kateista_riittavasti(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_maukas_lounas_maara_kun_kateista_riittavasti(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat, 1)  


    def test_maukas_lounas_vaihtoraha_kun_kateista_ei_riittavasti(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(maksu, 300)

    def test_maukas_lounas_kassaraha_kun_kateista_ei_riittavasti(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukas_lounas_maara_kun_kateista_ei_riittavasti(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)



    def test_edullinen_lounas_onnistuu_kun_kortilla_riittavasti(self):
        value = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(value, True)

    def test_edullinen_lounas_kortin_saldo_kun_kortilla_riittavasti(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_edullinen_lounaiden_maara_kun_kortilla_riittavasti(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.edulliset, 1)  



    def test_edullinen_lounas_ei_onnistu_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        value = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(value, False)

    def test_edullinen_lounas_kortin_saldo_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_edullinen_lounaiden_maara_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.edulliset, 0)  





    def test_maukas_lounas_onnistuu_kun_kortilla_riittavasti(self):
        value = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(value, True)

    def test_maukas_lounas_kortin_saldo_kun_kortilla_riittavasti(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_maukas_lounaiden_maara_kun_kortilla_riittavasti(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.maukkaat, 1)  



    def test_maukas_lounas_ei_onnistu_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        value = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(value, False)

    def test_maukas_lounas_kortin_saldo_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_maukas_lounaiden_maara_kun_kortilla_ei_ole_riittavasti(self):
        self.maksukortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_lounas_ei_muuta_kassarahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukas_lounas_ei_muuta_kassarahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)



    def test_kortille_ladatessa_kassaraha_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_kortille_ladatessa_korttisaldo_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)


    def test_kortille_ladatessa_megatiivisen_kassaraha_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -20)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_ladatessa_negatiivisen_korttisaldo_ei_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -20)
        self.assertEqual(self.maksukortti.saldo, 1000)
