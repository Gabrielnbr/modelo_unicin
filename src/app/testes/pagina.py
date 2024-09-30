from pandas import (
    Series,
    DataFrame
)

# Import de seleções básicas, numéricas e de data da biblioteca streamlit
from streamlit import (
    checkbox, multiselect, selectbox, select_slider, toggle,  # Seleções básicas
    number_input, slider,  # Seleções numéricas
    date_input  # Seleção de data
)

class Pagina:
    
    def __init__(
        self,
        data: Series | DataFrame,
        lista_selecao: list | str,
        ):
        
        self.data = data
        self.lista_selecao = lista_selecao or [
            "checkbox",
            "multiselect",
            "selectbox",
            "select_slider",
            "toggle",
            "number_input",
            "slider",
            "date_input"]
    
    def selecao_filtro(
        self,
        selecao: str
        ) -> str:
        
        if selecao in self.lista_selecao:
            return selecao
        else:
            raise ValueError(
                f"A opção selecionada {selecao} não consta na lista de selecao.\n"
                f"Escolha uma das seleções a seguir {self.lista_selecao}"
            )
    
    def filtro(self, data: Series | DataFrame, *args, **kwargs):
        ...
    
    def selecao_grafico(self, ):
        ...
    
    def grafico(self, data: Series | DataFrame, *args, **kwargs):
        ...
    