import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()
        self._maxY = None
        self._maxH = None

    def handleWorstCase(self, e):
        self._maxY = self._view._txtYears.value
        self._maxH = self._view._txtHours.value
        self._nercSel = self._idMap[self._view._ddNerc.value]
        risultato = self._model.ricorsione([], self.maxY, self._maxH, self._nercSel.id)


    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
