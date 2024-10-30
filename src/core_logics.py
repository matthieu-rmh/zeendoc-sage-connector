from sage.api_calls import get_receipt_lines
from datetime import datetime

def get_sage_receipt_lines():
    return get_receipt_lines()

def convert_receipt_lines(receipts):
    '''
    Convert receipts into usable lines to be sent to Zeendoc
    '''
    # We have to comply to the following format (taken from the 
    # 2024-10-03 Mapping SAGE L1000 GESCOM.xlsx file)

    # id_ligne
    # bon_commande
    # nom_br
    # date_commande
    # date_br
    # fournisseur
    # pu_original
    # quantite_originale
    # taux_tva_original
    # total_ligne_original
    # remise_originale
    # ref_article_fournisseur
    # ref_article_erp
    # description_article

    return [{
            "id_ligne": line_data["lines"][0]["id_ligne"],
            "bon_commande": line_data["lines"][0]["bon_commande"],
            "nom_br": line_data["lines"][0]["nom_br"],
            # "date_commande" is missing from the response
            "date_br": datetime.fromisoformat(line_data["lines"][0]["date_br"]
                                              ).strftime("%Y-%m-%d"),
            "fournisseur": line_data["lines"][0]["fournisseur"],
            "pu_original": line_data["lines"][0]["pu_original"],
            "quantite_originale": line_data["lines"][0]["quantite_original"],
            # renamed the key here for orthograph purpose
            # "taux_tva_original" is missing
            # "total_ligne original" is missing
            # "remise_originale" is missing
            "ref_article_fournisseur":
                line_data["lines"][0]["ref_article_fournisseur_retenue"],
            # "ref_article_fournisseur_retenue" : correct key name / value ? 
            "ref_article_erp": line_data["lines"][0]["ref_article_erp"],
            "description_article": line_data["lines"][0]["description_article"],
             } for line_data in receipts["Receptions"] if line_data is not None
            # a line has been of NoneType so we add this condition
            ]
