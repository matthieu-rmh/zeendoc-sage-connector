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
            "id_ligne": item["id_ligne"],
            "bon_commande": item["bon_commande"],
            "nom_br": item["nom_br"],
            # "date_commande" is missing from the response
            "date_br": datetime.fromisoformat(item["date_br"]
                                              ).strftime("%Y-%m-%d"),
            "fournisseur": item["fournisseur"],
            "pu_original": item["pu_original"],
            "quantite_originale": item["quantite_original"],
            # renamed the key here for orthograph purpose
            # "taux_tva_original" is missing
            # "total_ligne original" is missing
            # "remise_originale" is missing
            "ref_article_fournisseur":
                item["ref_article_fournisseur_retenue"],
            # "ref_article_fournisseur_retenue" : correct key name / value ? 
            "ref_article_erp": item["ref_article_erp"],
            "description_article": item["description_article"],
             } for data in receipts["Receptions"] for item in data["lines"] if data is not None            # a line has been of NoneType so we add this condition
            ]
