from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_reset_click(self, **event_args):
    self.text_box_bruto.text = ""
    self.text_box_pio.text = ""
    self.text_box_zdr.text = ""
    self.text_box_vrab.text = ""
    self.text_box_dop_prid.text = ""
    self.text_box_dld.text = ""
    self.text_box_vkupno.text = ""
    self.text_box_neto.text = ""

  def button_presmetaj_click(self, **event_args):
    try:
      if self.text_box_bruto.text < 26422:
        alert("Минималната бруто плата во моментов изнесува 26422 денари.")
      else:
        bruto = self.text_box_bruto.text
        pio = round(bruto * 0.188)
        self.text_box_pio.text = pio
        zdr = round(bruto * 0.075)
        self.text_box_zdr.text = zdr
        vrab = round(bruto * 0.012)
        self.text_box_vrab.text = vrab
        dop_prid = round(bruto * 0.005)
        self.text_box_dop_prid.text = dop_prid
        vkupno_pridonesi = pio + zdr + vrab + dop_prid
        dld = round((bruto - vkupno_pridonesi - 8788) / 10)
        self.text_box_dld.text = dld
        self.text_box_vkupno.text = vkupno_pridonesi + dld
        neto = bruto - vkupno_pridonesi - dld
        self.text_box_neto.text = neto
    except:
      alert("Настана грешка. Не заборавајте да ја внесете бруто платата.")




